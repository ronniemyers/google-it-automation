def replace_ending(sentence, old, new):
  if sentence[-len(old):]==old:
    i = -len(old)
    new_sentence = sentence[:i] + new
    return new_sentence
  return sentence

print(replace_ending("It's raining cats and cats", "cats", "dogs"))
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
print(replace_ending("The weather is nice in May", "may", "april"))
print(replace_ending("The weather is nice in May", "May", "April"))  