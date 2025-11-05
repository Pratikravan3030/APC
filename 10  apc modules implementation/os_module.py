import os

current_dir = os.getcwd()
print(f"Current Directory: {current_dir}")

# Create a new directory
if not os.path.exists("example_dir"):
    os.mkdir("example_dir")
    print("Created directory 'example_dir'")
else:
    print("Directory 'example_dir' already exists")

# Rename the directory
#os.rename('example_dir','python_dir')
#print("Renamed directory to 'python_dir'")

# List all files and directories in current directory
print("Contents of current directory:")
print(os.listdir())

# Remove the directory
os.rmdir('example_dir')

os.scandir(current_dir)
print("Iterting through directory contents:")
for entry in os.scandir(current_dir):
    print(entry)


