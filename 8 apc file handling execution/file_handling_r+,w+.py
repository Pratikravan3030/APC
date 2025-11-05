filename = 'sample.txt'

with open(filename, 'w') as f:
    f.write('Hello World!\nSecond Line.')

# r+ mode: Read and write, file must exist
print("Using r+ mode:")
with open("filename", 'r+') as f:
    content = f.read()
    print("Original content:", content)
    f.seek(0)
    f.write('Updated Line.\n')
    f.seek(0)
    print("After writing:", f.read())

# w+ mode: Write and read, file is created/truncated
print("\nUsing w+ mode:")
with open(filename, 'w+') as f:
    f.write('This line is written in w+ mode.\n')
    f.seek(0)
    print("After writing:", f.read())