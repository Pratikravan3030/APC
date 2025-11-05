from pathlib import Path

# Create a Path object for a file
file_path = Path("example.txt")

# Check if the file exists
if file_path.exists():
    print(f"{file_path} exists.")
else:
    print(f"{file_path} does not exist.")

# Get the absolute path
print("Absolute path:", file_path.resolve())

# Get the file name and extension
print("File name:", file_path.name)
print("File extension:", file_path.suffix)
