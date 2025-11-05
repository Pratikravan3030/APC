# set

days1 ={"Mon","Tue","Wed","Thu","Fri","Sat","Sun"}
print(days1)

days2=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
print(days2)

print("\n")

months = {"Jan","Feb","Mar","Apr","May","Jun"}
print(months)
months.add("Jul")
print(months)
months.remove("Feb")    
print(months)
months.discard("Mar") 
print(months)
months.clear() 
print(months)

print("\n")

# set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set([1,1,2,3,4,4,5,6,6,7,8,8,8,9,9,10])
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)
print("Set3:", set3)


