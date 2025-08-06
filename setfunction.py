# create a set
settype1 = {18, 45, 3}
print("Original set:", settype1)

#add
settype1.add("JavaScript")
print("After add:", settype1)

#copy
settype2 = settype1.copy()
print("Copied set:", settype2)

#update 
settype1.update(["Ruby", "Go"])
print("After update:", settype1)

#discard 
settype1.discard("Java")  
print("After discard (Java):", settype1)

#pop 
popped_item = settype1.pop()
print("Popped item:", popped_item)
print("After pop:", settype1)

#clear
settype1.clear()
print("After clear:", settype1)
