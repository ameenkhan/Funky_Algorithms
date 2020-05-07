# Determine if a string has all unique characters

def is_unique(str):
  if len(str) == 1:
    return True

  occur = set()
  
  for c in str:
    if c in occur:
      return False
    occur.add(c)
  
  return True 

print(is_unique("ameen")) # false
print(is_unique("abcd"))  # true