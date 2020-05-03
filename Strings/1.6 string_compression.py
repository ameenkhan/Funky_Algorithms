# String compression
# aabcccaa --> a2b1c3a2

def str_compr(str1):
  c = str1[0]
  occurence = 0
  compr = list()

  for letter in str1:
    if c == letter:
      occurence += 1
    else:
      compr.extend([c, occurence])
      occurence = 1
      c = letter
  compr.extend([c, occurence])
  
  return ''.join(str(x) for x in compr)

print(str_compr("abbcccaa")) # a1b2c3a2

