a=input("enter the word")
if a:
    b=a[0]
    m=b+a[1:].replace(b,'$')
    print("new word",m)
else:
    print("word not found")
