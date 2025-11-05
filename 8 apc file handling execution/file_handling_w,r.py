# Open a file for writing
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("This file is sepcifically made for understanding the concept of file handling\n")

# Open the file for reading
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)