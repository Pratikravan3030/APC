# Directory hanldling
import os
os.makedirs('new_directory')  # We can Create a new directory 


os.chdir('new_directory')  # We can Change the current working directory


print("Current Directory:", os.getcwd())  # We can Print the current working directory


os.listdir('.')  # We can List files in the current directory


os.rmdir('new_directory')  # We can Remove the directory