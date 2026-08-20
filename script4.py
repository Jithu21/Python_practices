# 1. Electricity bill calculation: units= int(input("Enter your bill here"))
if units <=100:
    print(units*5)
elif units >201 and units <=300:
    print(units * 7)
elif units >301 and units <=400:
    print(units * 9)
elif units  > 400:
    print(units *10)
else:
    print("Invalid inputs")



# 2.Employee Bonus
Experiences = int(input("Enter the number of experiences: "))
if Experiences >= 4:
    print("20% of the Bonus")
else:
    print("10% of the Bonus")



# 3.student Scholarship
Marks = int(input("Marks Obtained"))
Income = int(input("Family Income"))
if Marks >= 80:
    if Income <= 300000:
        print("Eligible for full scholarship")
    else:
        print("Eligible for partial scholarship")
else:
    print("Not Eligible")




# 4. ATM Withdrawal

account_balance = int(input("Account balance: "))
withdrawal_amount = int(input("Withdrawal amount: "))

if withdrawal_amount > 0:
    if withdrawal_amount <= account_balance:
        if withdrawal_amount % 100 == 0:
            print("Withdrawal successful")
        else:
            print("Enter amount in multiples of 100")
    else:
        print("Insufficient balance")
else:
    print("Enter positive number")



# 5. Second largest number

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))
if num1 > num2 and num1 < num3:
    print("num1 is the second largest number")
if num2 > num1 and num2 < num3:
    print("num2 is the second largest number")
if num3 > num1 and num3 < num2:
    print("num3 is the second largest number")




# 6. Triangle validation

triangle_firstside = int(input("Enter a triangle number: "))
triangle_secondside = int(input("Enter a triangle number: "))
triangle_thirdside = int(input("Enter a triangle number: "))
if triangle_firstside == triangle_secondside and triangle_secondside == triangle_thirdside:
    print("Triangle numbers are equal")
elif triangle_firstside == triangle_secondside or triangle_secondside == triangle_thirdside or triangle_thirdside == triangle_firstside:
    print("Triangle numbers are Isosceles")
elif triangle_firstside != triangle_secondside !=triangle_thirdside:
    print("Triangle numbers are not equal and not isosceles and its Scalene")
else:
    print("valid Number ")








