lst=[5,18,77,108,930]
x=int(input("Enter the number to be added : \n"))
for i in range(len(lst)):
    if x > lst[i] and x < lst[i+1]:
        lst.insert(i+1,x)
print(lst)
