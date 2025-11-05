with open('append.txt', 'a') as file:
    # Data to append
    data = "This line is appended in a new file created.\n"
    file.write(data)

print("Data appended successfully.")

with open('example.txt', 'a') as file:
    # Data to append
    data = "This line is appended in an existing file named as 'example'.\n"
    file.write(data)

print("Data appended successfully.")