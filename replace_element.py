lst=[]
for i in range(0,7):
    input_string=str(input("Enter string: "))
    lst=lst+[input_string]

print(lst)


find= str(input("Find element: "))
new_str = str(input("New string: "))

if find in lst:
        index = lst.index(find)
        lst[index] = new_str

else:
    print("String is missing")

print(lst)



