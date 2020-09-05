# creates a new python script in the current working directory, adds the line of comments to it declared by the 'comments' variable, and returns the size of the new file
import os
def create_python_script(filename):
    comments = "# Start of a new Python Program"
    with open(filename, 'w') as new_file:
        new_file.write(comments)
        fpath = os.path.abspath(filename)
        print(fpath)

    filesize=os.path.getsize(fpath)
    return(filesize)
print(create_python_script("program.py"))
