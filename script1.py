# ATM Withdrawal

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