# OS Path Modules in Python
import os

os.path.exists('things.txt')  # Check if a file exists


os.path.isdir('things')  # Check if a directory exists


os.path.join('dir', 'things.txt')  # Join directory and file names into a single path


os.path.basename('/Users/pratikravan/Desktop/ACP-LAB/things.txt')  # Get the base name of a file from a path


os.path.dirname('/Users/pratikravan/Desktop/ACP-LAB/things.txt')  # Get the directory name from a path


os.path.split('/Users/pratikravan/Desktop/ACP-LAB/things.txt')  # Split the path into directory and file name