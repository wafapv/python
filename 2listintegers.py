a=[]
b=[]
n=int(input('enter max number elemants in first list :'))
for i in range(0, n):
    num = int(input())
    a.append(num)
n=int(input('enter max number elemants in first list :'))
for i in range(0, n):
    num = int(input())
    b.append(num)
print('length of string a',len(a) ,'length of string b ',len(b))
if(len(a)==len(b)):
   print('length is same')
else:
    print('length is not same')
s1=sum(a)
s2=sum(b)
if(s1==s2):
    print('sum is equal')
else:
    print('sum not equal')
if(a==b):
    print('list of elemants are same')
else:
    print('list of elemants not same ')

