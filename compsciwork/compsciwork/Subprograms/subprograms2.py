def under50(num):
    name = input("Enter your name: ")
    print(f"Hello {name}")

def over50(num):
    print(num/2)

num = int(input("Enter a number between 1 and 100: "))

if num < 1 or num > 100:
    print("Please input a number between 1 and 100")
elif num < 50:
    under50(num)
elif num >= 50:
    over50(num)