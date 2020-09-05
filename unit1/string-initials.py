def initials(phrase):
# Separate phrase into words
  words = phrase.split()
  result = ""
# Index first character [0] in each word
  for word in words:
    result += word[0].upper()
# Join first character and return

  return result

print(initials("Universal Serial Bus"))