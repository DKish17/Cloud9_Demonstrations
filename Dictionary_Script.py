"""
The purpose of this script is to generate a list of dictionaries 
from files in our working directory then print said list
"""

import os
# imports os library that allows user to interact with native OS

working_dir = os.getcwd()
#will get the current working directory

my_files = []
#creates an empty list to store our files


for dir_path, dir_names, file_name in os.walk(working_dir):
#scans current working directory for files

    for file in file_name:
#iterates through files
        
        file_path = os.path.join(dir_path, file)
#path gets the file's path        
#join takes all the elements of an iterable and joins them into a single string      
       
        file_size = os.path.getsize(file_path)
#gets the file size        
        
        my_files.append({"name": file, "size": file_size})
#creates and appends the dictionary to the list

for file in my_files:
#iterates through the list

    print(file)
#prints the dictionary
"""
How easy was that!
"""