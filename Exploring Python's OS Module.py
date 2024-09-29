# Exploring Python's OS Module

import os

def list_directory_contents(path):
    if not os.path.exists(path):
        print("Error: invalid directory.")
    elif not os.access(path, os.R_OK):
        print("Error: program lacks permission to access this directory.")
    else:
        try:
            print(os.listdir(path))
        except Exception as e:
            print(f"An error occured: {e}")
    

path = input("Enter the directory path: ")
list_directory_contents(path)