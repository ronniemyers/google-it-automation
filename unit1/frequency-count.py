def count_letters(text):
  result = {}
  text = text.lower()

  for letter in text:
      if letter.isalpha():
        if letter in result.keys():
          result[letter] += 1
        else:
          result[letter] = 1
  return result

print(count_letters("AaBbCc"))
print(count_letters("Math is fun! 2+2=4"))
print(count_letters("This is a sentence."))