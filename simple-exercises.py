# number = int(input("Enter number"))


while number!=100:

    print(number)
    number = int(input("Enter number"))




# #----------------------------------------------------

num = int(input("Enter number"))


while True:

    if num==100:
        break


    print(number)
    number = int(input("Enter number"))


#------------------------------------------------------


for i in range(0,16,2):
    print(i)


#-------------------------------------------------------

ls=[]

for i in range(0,10):
    while True:
        try:
            number = int(input("Enter number: "))
            ls = ls + [number]
            break
        except ValueError:
            print("You have to enter integer")


#function for substraction
def sum (L):
    "Sum of even numbers"
    s = 0
    #for i in range(0,len(list)):
    for l in L:
        if l%2==0:
            s+=l

    return(s)

#function for replacing negative nums
def replace (L):
    "Replaced negative numbers"
    for i in range(0,len(L)):
        if L[i]<0:
            L[i]= 0

    return L


print(ls)
print(sum.__doc__)
print(sum(ls))
print(replace.__doc__)
print(replace(ls))









