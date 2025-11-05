per=float(input("Enter your percentage: "))

if per>=90:
    print("Excellent performance")
elif per>=80:
    print('Very good performance')
elif per>=70:
    print("good performance")
elif per>60:
    print('average performance')
else:
    print('poor performance')