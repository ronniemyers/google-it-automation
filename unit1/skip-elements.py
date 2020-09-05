def skip_elements(elements):
  skip = elements[0::2]

  if elements == []:
    return "List is empty!"
  return skip

print(skip_elements([]))
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))