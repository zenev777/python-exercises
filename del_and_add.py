# изтрива избран низ и вмъква нов низ в избрана позиция в списъка
del_str= str(input("Find and delete element: "))
add_new_str = str(input("Add element: "))
index_of_newstr = int(input("Index of the new element: "))

if del_str in lst:
        lst.remove(del_str)
        lst.insert(index_of_newstr,add_new_str)
else:
    print("String is missing")

print(lst)