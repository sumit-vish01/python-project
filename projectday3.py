#creating atm using python basics
pin = int(input("Enter your pin :"))

attempt = 1

while pin != 9870 and attempt < 3:
    print("invalid pin , try again")
    pin = int(input("Enter your pin:"))

    attempt += 1

if pin == 9870:
    print("Your account balance is = 10000")

account_balance = 10000
amount = 10000

def withdraw_money(amount):
    global account_balance

if amount > account_balance:
    print("u have didot sufficient balance")
    print(f"ur current balance: {account_balance}")
elif amount <= 0:
    print("please comfir u are right correct amount")
else:
    account_balance = account_balance - amount
    print(f"succesfully ${amount} withdraw amount")
    print(f"your balance ${account_balance}")

print("--- first trail: $2000 withdraw ---")
withdraw_money(2000)
print("\n--- second trail: 4000 withdraw (balance amount)---")
withdraw_money(4000)
