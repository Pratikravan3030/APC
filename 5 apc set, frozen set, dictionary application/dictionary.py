# dictionary
dict1={"Name":"Ishaan","Age":19,"City":"Kolhapur","College":"DYPCET"}
print("Dictionary:", dict1)

Employee=dict({'Name':"Ishaan",'Age':19,'City':"Kolhapur",'College':"DYPCET"})
print("Employee Dictionary:", Employee)

print("Name :", Employee['Name'])
print("Age :", Employee['Age'])
print("City :", Employee['City'])

# dict funcs
print("Keys:", Employee.keys())
print("Values:", Employee.values())
print("Items:", Employee.items())
print("Length of Employee Dictionary:", len(Employee))

Employee['Salary'] = 100000
print("Updated Employee Dictionary:", Employee)

Employee['Age'] = 20
print("Updated Age in Employee Dictionary:", Employee)
Employee.pop('City')

print("After removing City:", Employee)
Employee.get('College')

print("College:", Employee.get('College'))

Employee.update({'Department': 'IT'})
Employee.clear()