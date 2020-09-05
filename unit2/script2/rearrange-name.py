import re
def rearrange_name(name):
  result = print(re.search(r"^(\w*).(\w*)$", "Lovelace, Ada"))
  if result is None:
    return name
  return "{} {}".format(result[2], result[1])