a = []
b = []
n=int(input('enter max number elemants :'))
for i in range(0, n):
    num = int(input())
    a.append(num)
    if(num>100):
        b.append('over')
    else:
        b.append(num)
print(a)
print(b)
    
