#!/bin/sh
export HADOOP_CLASSPATH=$(hadoop classpath)

echo --- Deleting
rm WordCount2.jar
rm classes/WordCount2*.class

echo --- Compiling
javac -classpath ${HADOOP_CLASSPATH} -d "./classes/" "WordCount2.java"        
if [ $? -ne 0 ]; then
    exit
fi

echo --- Jarring
jar -cvf WordCount2.jar -C "./classes/" .

echo --- Running
PATTERNS=/tmp/patterns.txt
INPUT=/tmp/input_data.txt
OUTPUT=/user/${USER}/word_count_v2_output/

hdfs dfs -rm -R $PATTERNS
hdfs dfs -rm -R $INPUT
hdfs dfs -rm -R $OUTPUT

hdfs dfs -copyFromLocal patterns.txt /tmp
hdfs dfs -copyFromLocal input_data.txt /tmp

time hadoop jar WordCount2.jar WordCount2 -Dwordcount.case.sensitive=false $INPUT $OUTPUT -skip $PATTERNS

hdfs dfs -ls $OUTPUT
