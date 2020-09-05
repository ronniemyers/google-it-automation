# creates a new directory inside the current working directory, then creates a new empty file inside the new directory, and returns the list of files in that directory

import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  print(os.path.exists(directory))
  # Create the new file inside of the new directory
  open(filename, "w")
  # Return the list of files in the new directory
  list = os.listdir()
  print(list)
print(new_directory("PythonPrograms", "script.py"))