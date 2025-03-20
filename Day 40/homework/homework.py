name1=input("enter your name: ")
name2=input("enter your name: ")
name3=input("enter your name: ")

lst=[]

lst.append(name1)
lst.append(name2)
lst.append(name3)

for i in range(len(lst)):
    print(lst[i])