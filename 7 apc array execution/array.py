import array as arr


int_array = arr.array('i', [1, 2, 3, 4, 5])
print("Integer Array:", int_array,"\n")

float_array = arr.array('f', [1.1, 2.2, 3.3, 4.4, 5.5])
print("Float Array:", float_array,"\n")

print("First element of int_array:", int_array[0],"\n")

print("Second element of float_array:", float_array[1],"\n")

int_array[0] = 10
print("Modified Integer Array:", int_array,"\n")

print("Sliced Integer Array (first 3 elements):", int_array[:3])

#functions
int_array2 = arr.array('i', [1, 2, 3, 4, 5,6,7,8,9,10])
int_array2.append(11)
print("Appended Integer Array:", int_array2,"\n")

int_array2.pop(0)
print("After popping first element:", int_array2,"\n")

int_array2.remove(5)
print("After removing element 5:", int_array2,"\n")

int_array2.reverse()
print("Reversed Integer Array:", int_array2,"\n")

int_array2.insert(0, 0)
print("After inserting 0 at the beginning:", int_array2,"\n")

int_array2.extend(arr.array('i', [12, 13, 14]))
print("After extending with [12, 13, 14]:", int_array2,"\n")