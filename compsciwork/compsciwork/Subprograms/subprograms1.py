def over20(total):
    i = 0
    while i < total:
        print(i)
        i += 2

def under20(total):
    for i in range(0, total+1):
        print(i)

num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
num3 = int(input("Enter number: "))

total = num1+num2+num3

if total > 20:
    over20(total)
elif total < 20:
    under20(total)