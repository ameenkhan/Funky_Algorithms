# Determine if one string is permutation of the other

def check_permutation(str1, str2):
  if len(str1) != len(str2):
    return False
  
  occur = dict()

  for c in str1:
    occur[c] = occur.get(c,0) + 1
  
  for c in str2:
    if occur.get(c, 0) == 0:
      return False
    else:
      occur[c] = occur.get(c) - 1
  
  return True

print(check_permutation("ameen", "neema")) # true
print(check_permutation("ameen", "notme")) # false