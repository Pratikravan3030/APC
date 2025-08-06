listtype1=[18, 45, 3]
print (listtype1)
#append
listtype1.append("JavaScript")
print(listtype1)

#insert
listtype1.insert(2, "C#")
print(listtype1)

#copy
listtype2 = listtype1.copy()
print(listtype2)

#count
count_of_python = listtype1.count("Python")
print("Count of Python in listtype1:", count_of_python)

#extend
listtype1.extend(["Ruby", "Go"])
print(listtype1)

#remove
listtype1.remove("Java")
print(listtype1)

#pop
popped_item = listtype1.pop(3)  
print("Popped item:", popped_item)

#index
index_of_python = listtype1.index("Python")
print("Index of Python in listtype1:", index_of_python)

#reverse
listtype1.reverse()
print("List after reverse:", listtype1)

#sort
listtype1.sort(key=str)  
print("List after sort:", listtype1)


#clear
listtype1.clear()
print("List after clear:", listtype1)





