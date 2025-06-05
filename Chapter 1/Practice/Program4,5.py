# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that

import os
# Get the current working directory
current_directory = os.getcwd() 
# List all files and directories in the current directory
contents = os.listdir(current_directory)
# Print the contents
for item in contents:
    print(item)