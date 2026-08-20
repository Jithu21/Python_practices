num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))
if num1 > num2 and num1 < num3:
    print("num1 is the second largest number")
if num2 > num1 and num2 < num3:
    print("num2 is the second largest number")
if num3 > num1 and num3 < num2:
    print("num3 is the second largest number")