"""
Get all the permutations of a string. For example if str = abc:

abc, acb, bac, bca, cba, cab
---

Logic:

a (bc)      | a (bcd)
  ab (c)    |   ab (cd)
    = abc   |     abc (d)
  ac (b)    |       = abcd
    = acb   |     abd (c)
            |       = abdc
b (ac)      |   ac (bd)
  ba (c)    |     acb (d)
    = bac   |       = acbd
  bc (a)    |     acd (b)
    = bca   |       = acdb
            | ....  
c (ab)      | b (acd)
  ca (b)    |   ba (cd)
    = cab   |     bac (d)
  cb (a)    |       = bacd
    = cba   |     bad (c)
"""

def permutations(prefix, suffix, res):
  if len(suffix) == 0:
    res.append(prefix)
  
  else:
    for i in range(len(suffix)):
      permutations(prefix + suffix[i], suffix[:i] + suffix[i+1:], res)

def permute(str):
  res = list()
  permutations('', str, res)
  return(res)

print('Permutations of abc:')
print(permute('abc'))