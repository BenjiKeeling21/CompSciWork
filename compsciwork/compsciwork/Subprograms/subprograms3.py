def AddTogether(num1, num2, num3):
    return(num1+num2+num3)

def Average(num1, num2, num3):
    return((num1+num2+num3)/3)

def Highest(num1, num2, num3):
    list = [num1, num2, num3]
    return max(list)

def Lowest(num1, num2, num3):
    list = [num1, num2, num3]
    return min(list)

print("Please enter 3 numbers:")
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))

choice = int(input("\n1) Add together\n2) Average\n3) Highest\n4) Lowest\n\nEnter Selection: "))

if choice == 1:
    print(AddTogether(num1, num2, num3))
elif choice == 2:
    print(Average(num1, num2, num3))
elif choice == 3:
    print(Highest(num1, num2, num3))
elif choice == 4:
    print(Lowest(num1, num2, num3))
else:
    print("Error! please try again")