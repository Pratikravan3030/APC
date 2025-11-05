friends=["Ishaan","Pratik","Vedant","Gandhar","Simoni","Varada","Diya"]
print(friends)

friends.remove("Diya")
print(friends)

friends.append("Shreya")
print(friends)

friends.count("Gandhar")
print(friends)

app=input("Enter the item you want to append:")
friends.append(app)

ins=input("Enter the item you want to insert:")
pos=int(input("Enter the position where you want to insert:")) 
friends.insert(pos, ins)
print(friends)

friends.sort()
print(friends)

friends.reverse()
print(friends)

rem=int(input("Enter the index of the item you want to remove:"))
friends.pop(rem)
print(friends)
