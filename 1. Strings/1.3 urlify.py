# replace all spaces within a string with a '%20' given the 
# string and the number of non space characters

def urlify(convert, chars):
  url = list()

  for c in convert:
    if chars == 0:
      break
    elif c == " " and chars > 0:
      url.append("%20")
    else:
      url.append(c)
      chars -= 1
  
  return ''.join(url)

print(urlify("A mee n  ", 5)) #A%20mee%20n
