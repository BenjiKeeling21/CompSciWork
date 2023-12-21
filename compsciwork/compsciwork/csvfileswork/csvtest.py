file = open("numbers.csv" , "a")
total = 0
for i in range(3):
    num = int(input("Enter number: "))
    total += num
    data = str(total)+"\n"
    file.write(data)
file.close()