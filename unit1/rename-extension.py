filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

# rename all files with extension hpp to extension h
e = [e.replace('.hpp', '.h') for e in filenames]

print(e)