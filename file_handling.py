# 1) Create things.txt
with open("things.txt", "w") as file:
    file.write("Apple\nBanana\nCherry\nMango\n")

# 2) Read from things.txt (read) and print
with open("things.txt", "r") as file:
    content = file.read()
    print("Content of things.txt:\n", content)

# 3) Write that content to result.txt
with open("result.txt", "w") as file:
    file.write(content)

# 4) Read result.txt using read()
with open("result.txt", "r") as file:
    print("\nresult.txt with read():")
    print(file.read())

# 5) Read result.txt using readline()
with open("result.txt", "r") as file:
    print("\nresult.txt with readline():")
    print(file.readline())   # first line
    print(file.readline())   # second line

# 6) Read result.txt using readlines()
with open("result.txt", "r") as file:
    print("\nresult.txt with readlines():")
    print(file.readlines())  # list of all lines

# 7) Use seek() to WRITE at a specific position, then seek(0) and read all again
with open("result.txt", "r+") as file:
    print("\nPointer at start (tell):", file.tell())
    file.seek(7)                 # move to byte 7 (inside "Banana")
    file.write("\nORANGE\n")         # overwrite text
    print("Pointer after write (tell):", file.tell())
    file.seek(0)                 # back to start
    print("\nresult.txt AFTER seek+write, full content:")
    print(file.read())           # read entire file again
