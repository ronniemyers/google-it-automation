def print_seconds(hours, minutes, seconds):
  hours = hours*3600
  minutes = minutes*60
  sum = hours+minutes+seconds
  
  print(sum)
  
print(print_seconds(1,2,3))