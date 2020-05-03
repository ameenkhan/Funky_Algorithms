# Given two strings, find out if they are one edit away
# edit can be remove, replace or insert one character

def replace_char(str1, str2):
  # There can only be one character diff
  diff = False
  for i in range(len(str1)):
    if str1[i] != str2[i]:
      if diff: return False
      else: diff = True
  return True

def insert_char(str1, str2):
  diff = False
  ptr_1 = 0
  ptr_2 = 0
  while ptr_1 < len(str1) and ptr_2 < len(str2):
    if str1[ptr_1] != str2[ptr_2]:
      if diff: 
        return False
      else:
        diff = True
      ptr_2 += 1
    else:
      ptr_1 += 1
      ptr_2 += 1
  return True

def one_away(str1, str2):
  if str1 == str2: return True

  if len(str1) == len(str2):
    return replace_char(str1, str2) # replace
  
  if len(str1) + 1 == len(str2):
    return insert_char(str1, str2) # insert a char into str1
  elif len(str1) == len(str2) + 1:
    return insert_char(str2, str1) # "remove" a char from str1 == inserting a char into str2
  else:
    return False

print(one_away("pale", "ple"))    # True
print(one_away("ple", "pale"))    # True
print(one_away("pale", "pali"))   # True

print(one_away("ple", "pafle"))   # False
print(one_away("ple", "pri"))     # False
