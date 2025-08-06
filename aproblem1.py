# Write a PYTHON program to evaluate the student performance
#If % is >=90 then Excellent performance If % is >=80 then Very Good performance
#If % is >=70 then Good performance If % is >=60 then average performance else Poor performance.


n=int(input("Enter a percentage: "))

if n>=90 :
    print("Excellent performance" )
    
elif n>=80 :
    print("Very Good performance")

elif n>=70 :
    print("Good performance") 
    
elif n>=60 :
    print("average performance ")
          
else :
    ("Poor performance.")