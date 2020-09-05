def pig_latin(text):
  say = ""
  words = text.split()

  for word in words:
   x = word[1:] + word[0] + "ay" + " "
   say = say + x + ""
  return say[:-1]

print(pig_latin("hello how are you"))