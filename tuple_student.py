students = ('rishabh', 'avi', 'sam')

print('1. Input Names\n2. Search Names\n3.Exit')

while True:
    ind = int(input("Enter Index: "))

    if ind == 1:
        name = input("Enter name: ")
        students += (name,)
    
    elif ind == 2:
        name = input("Search name: ")
        if name in students:
            print("Name is present")
        else:
            print("Name is absent")

    else:
        break

# OUTPUT 
# 1. Input Names
# 2. Search Names
# 3.Exit
# Enter Index: 1
# Enter name: nobita
# Enter Index: 2
# Search name: nobita
# Name is present
# Enter Index: 3

# Code by Rishabh Shah
