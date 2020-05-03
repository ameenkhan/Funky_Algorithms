matr = [
  [0,1,2,3],
  [4,5,6,7],
  [8,9,10,11],
  [12,13,14,15]
]
"""
to rotate:

left    -> top
bottom  -> left
right   -> bottom
old top -> right

"""
def rotate_matr(matr):
  n = len(matr)
  for layer in range(int(n/2)):
    first = layer
    last = n-1-layer
    for i in range(first, last):
      offset = i - first
      
      top = matr[first][i]

      matr[first][i]           = matr[last-offset][first]
      matr[last-offset][first] = matr[last][last-offset]
      matr[last][last-offset]  = matr[i][last]
      matr[i][last]            = top
      print(matr)
  
  print()
  print(matr)

print(matr)
rotate_matr(matr)
