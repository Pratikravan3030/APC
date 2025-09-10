import array as arr

a = arr.array('i', [1, 2, 3, 4, 5])

# Insert
a.append(10)
print("After inserting 10:", a.tolist())

# Pop
popped = a.pop()
print("Popped element:", popped)

# Stats
print("Sum:", sum(a))
print("Average:", sum(a) / len(a))
print("Max:", max(a))
print("Min:", min(a))
print("Length:", len(a))

# Sort (convert to list, then back to array)
a = arr.array('i', sorted(a))
print("Sorted array:", a.tolist())

# Reverse
a.reverse()
print("Reversed array:", a.tolist())
