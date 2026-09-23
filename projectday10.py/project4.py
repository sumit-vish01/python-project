# ATM Simulation

pin = input("Enter your PIN: ") 

if pin == "1234":
    print("Login succesfull")


    Balance = 100000

    while True:
       print("\n -----ATM  MENU------")
       print("1. Check Balance")
       print("2. Deposit")
       print("3. Withdraw")
       print("4. Exit")


# amount = int(input("Enter deposit amount"))
# Balance =  Balance + amount

# if 2 > amount:
#    print("balance  + deposit_amount")
       choice = input("Enter your choice: ")

       if choice  ==  "1":
             print("Your balance is:", Balance)

        #depost
       elif choice  == "2":
            amount = int(input("Enter deposit amount: "))

            if amount > 0:
                  Balance = Balance + amount
                  print("DEposited amount succfully")
                  print("Your new balance is:", Balance)

            else:
                  print("Please enter a vaild amount")


       elif choice == "3":
             amount = int(input("Enter your withdraw amount: "))

             if amount > 0:
                  if amount <= Balance:
                      Balance = Balance - amount
                      print("Withdraw succesfully completed")
                      print("Your current balance is:", Balance)
                  else:
                    print("Insufficient amount please enter sufficient amount.")
             else:
                 print("Please enter a valid amount")
          #exit
       elif choice == "4":
            print("Thanking for choosing")
            break
       else:
            print("Invalid choice. please select 1-4.")


else:
  print("Wrong pin")


             


             