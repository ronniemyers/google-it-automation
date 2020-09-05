file = open("spider.txt")
print(file.readline())
print(file.read())

file.close() #it's good to close the file after you finish
with open("spider.txt") as file: #good to automatically close it
  print(file.readline())