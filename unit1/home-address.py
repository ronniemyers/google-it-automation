def format_address(address_string):
  house_number = ""
  street_name = ""
  address = address_string.split()

  for i in address:
    if i.isdigit():
      house_number = i
    else:
      street_name += i
      street_name += " "
      
  return "house number {} on street named {}".format(house_number, street_name)

print(format_address("123 Main Street"))
print(format_address("1001 1st Ave"))
print(format_address("55 North Center Drive"))
