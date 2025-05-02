from bank_account import BankAccount

user_id = input("Enter your user ID: ")
account = BankAccount(user_id)
account.create_account()

while True:
    print("\nChoose an option:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1–4): ")

    if choice == '1':
         print("Your balance is:", account.get_balance())
    elif choice == '2':
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    elif choice == '3':
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
