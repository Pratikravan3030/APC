size = int(input("Enter the size of the list: "))
list = []
for i in range(size):
    element = input(f"Enter element {i+1}: ")
    list.append(element)
print("The list is:", list)

print("List length:", len(list))
print("First element:", list[0])
print("Last element:", list[-1])
print("List sorted:", sorted(list))
print("List reversed:", list[::-1])


