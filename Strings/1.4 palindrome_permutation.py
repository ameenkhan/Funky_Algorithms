# given a string check if it is a permutation of a palindrome
# a palindrome must have all characters with an even occurence
# if the palindrome has an odd length then only one character can have odd occurence

def palindrome_permutation(val):
  occur = dict()

  for c in val:
    occur[c] = occur.get(c, 0) + 1
  
  if len(val) %2 == 0: # even length = no odd occurneces for a character
    for occurence in occur.values():
      if occurence %2 != 0:
        return False
    return True
  
  else: # odd = only one character can have an odd occurence
    middle = True
    for occurence in occur.values():
      if occurence %2 != 0:
        if middle:
          middle = False
        else:
          return False
    return True

print(palindrome_permutation("tacocat")) # odd char - res should be True
print(palindrome_permutation("tzcocat")) # odd char - res should be False

print(palindrome_permutation("amamtrtr")) # even char - res should be True
print(palindrome_permutation("amamtrtt")) # even char - res should be False