# Create a fresh file to work with
with open("modes.txt", "w") as f:
    f.write("Line1\nLine2\nLine3\n")

# --- r (read only, file must exist) ---
with open("modes.txt", "r") as f:
    print("\nMode r (read only):")
    print(f.read())

# --- r+ (read and write, file must exist, overwrites from current position) ---
with open("modes.txt", "r+") as f:
    print("\nMode r+ (read & write):")
    print("Before:", f.read())
    f.seek(6)              # move to after "Line1\n"
    f.write("EDITED\n")    # overwrite from here
    f.seek(0)
    print("After:", f.read())

# --- w (write only, creates/overwrites file) ---
with open("modes.txt", "w") as f:
    f.write("NewContent\n")   # overwrites everything
with open("modes.txt", "r") as f:
    print("\nMode w (write only, overwrite):")
    print(f.read())

# --- w+ (read & write, creates/overwrites file) ---
with open("modes.txt", "w+") as f:
    f.write("Hello W+\n")
    f.seek(0)
    print("\nMode w+ (read & write, overwrite):")
    print(f.read())

# --- a (append only, file pointer at end, creates if not exist) ---
with open("modes.txt", "a") as f:
    f.write("Appended A\n")
with open("modes.txt", "r") as f:
    print("\nMode a (append only):")
    print(f.read())

# --- a+ (read & append, file pointer at end, creates if not exist) ---
with open("modes.txt", "a+") as f:
    f.write("Appended A+\n")
    f.seek(0)
    print("\nMode a+ (read & append):")
    print(f.read())
