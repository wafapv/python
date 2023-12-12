x=int(input("Enter the number:"))
a=0
b=1
print("Fibonacci series:",a,b,end=" ") 
for i in range(1,x-1):
    a,b=b,a+b
    print(b,end=" ")
