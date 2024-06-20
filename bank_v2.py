def menu():
    menu_options = input("""

            [1] deposit
            [2] withdraw
            [3] transactions history
            [4] manage accounts
            [5] manage users
            [6] exit

    """)
    return(menu_options)

def deposit(deposit, balance, transaction_history, /):
    if deposit >= 0:
        balance += deposit
        print(f"\033[92m\nDeposit complete of R${deposit:.2f}\033[0m")
        transaction_history += f"\tDeposit: R${deposit:.2f}\n"
    else:
        print(f"\033[91m\nFailed attempt! You can't deposit an invalid amount\033[0m")

    return (balance, transaction_history)

def withdraw(*, withdraw, balance, transaction_history, number_of_transactions, limit, MAX_TRANSACTIONS):
    if number_of_transactions < MAX_TRANSACTIONS:
        if balance <= 0:
            print(f"\033[91m\nYou don't have enough money\033[0m")
        else:
            if withdraw > limit:
                print(f"\033[91m\nYou can't withdraw more than R$500,00\033[0m")
            elif withdraw > balance:
                print(f"\033[91m\nYou are trying to withdraw more than your balance\033[0m")
            else:
                balance -= withdraw
                number_of_transactions += 1
                print(f"\033[92m\nWithdrawal transaction complete of R${withdraw:.2f}\033[0m")
                transaction_history += f"\tWithdraw: R${withdraw:.2f}\n"
    return (balance, transaction_history, number_of_transactions)
           
def transactions(balance, /, *, transaction_history):
    print(f"Your balance is R${balance:.2f}\n")
    print(f"past transactions:\n{transaction_history}")

def manage_user(users):
    users = users
    while True: 
        action = input(""" What do you want to do?

                [1] Add new user
                [2] List users
                [3] Delete user
                [4] Return to main menu
                        
                """)
    
        if action == "4":
            print("returning to main menu...")
            return users
        elif action == "1":
            cpf = input("""\nPlease enter your CPF:
                        
                        Like the following format without dots and dash XXXXXXXXXXX

                        """)
            if len(cpf) == 11 and cpf.isdigit():
                found = False
                for user in users:
                    if user['cpf'] == cpf:
                        found = True
                        break
                if not found:
                    name = input("\nPlease enter your name: ")
                    date_of_birth = input("\nPlease enter your date of birth (dd-mm-yyyy): ")
                    address = input("\nPlease enter your address: ")
                    password = input("\nPlease enter your password: ")
                    users.append({"cpf":cpf, "name":name, "date_of_birth":date_of_birth, "address":address, "password":password})
                    print("\033[92m\nUser added successfully\033[0m")
                else:
                    print("\033[91m\nThis user already exists\033[0m")
            else:
                print("\033[91m\nInvalid CPF type\033[0m")
        
        elif action == "2":
            users_len = len(users)
            if users_len == 0:
                print("\033[91m\nThere are no users yet\033[0m")
            else:
                for user in users:
                    print(f"CPF: {user['cpf']}- Name: {user['name']}\n")
        
        elif action == "3":
            cpf = input("""Please enter the user's CPF you want to delete:
                        
                        Like the following format without dots and dash XXXXXXXXXXX

                        """)
            if len(cpf) == 11 and cpf.isdigit():
                found = False
                for user in users:
                    if user['cpf'] == cpf:
                        found = True
                        user_same = user
                        break
                if found:
                    #I want the specific name associated with the cpf
                    check = input(f"\nIs your name correct? {user_same["name"]}[y/n]: ")
                    if check == "y":
                        password_check = input("\nPlease enter your password: ")
                        if password_check == user_same["password"]:
                            # get the index of the user
                            index = users.index(user_same)
                            users.pop(index)
                            print("\033[92m\nUser deleted successfully\033[0m")
                        else:
                            print("\033[91m\nWrong password\033[0m")
                    else:
                        print("\033[91m\nWrong name...\033[0m")
                else:
                    print("\033[91m\nThis user doesn't exists\033[0m")
            else:
                print("\033[91m\nInvalid CPF type\033[0m")

    return users

def manage_account(users, accounts):
    agency = "0001"
    users, accounts = users, accounts
    while True:
        action = input(""" What do you want to do?

        [1] Add new account
        [2] List accounts
        [3] Return to main menu
        [x] *Delete* is not yet a feature
                    
        """)
        if action == "3":
            print("returning to main menu...")
            return accounts
        elif action == "1":
            cpf = input("""\nPlease enter your CPF:
                            
                            Like the following format without dots and dash XXXXXXXXXXX

                            """)
            if len(cpf) == 11 and cpf.isdigit():
                found = False
                for user in users:
                    if user['cpf'] == cpf:
                        found = True
                        break
                if found:
                    account_number = len(accounts) + 1
                    user = cpf
                    accounts.append({"agency":agency, "account_number":account_number, "user":user})
                    print("\033[92m\nAccount created successfully\033[0m")
                else:
                    print("\033[91m\nThis user doesn't exists\033[0m")
            else:
                print("\033[91m\nInvalid CPF type\033[0m")
        elif action == "2":
            cpf = input("""\nPlease enter your CPF:
                            
                            Like the following format without dots and dash XXXXXXXXXXX

                            """)
            if len(cpf) == 11 and cpf.isdigit():
                found = False
                for account in accounts:
                    if account['user'] == cpf:
                        found = True
                        account_same = account
                        break
                if found:
                    accounts_len = len(accounts)
                    if accounts_len == 0:
                        print("\033[91m\nThere are no accounts yet for this user\033[0m")
                    else:
                        for account in accounts:
                            print(f"User: {account_same['user']}- Account number: {account_same['account_number']}- Agency: {account_same['agency']}\n")
                else:
                    print("\033[91m\nThis user doesn't exists\033[0m")
            else:
                print("\033[91m\nInvalid CPF type\033[0m")    

    return accounts
     
def main():
    limit = 500
    balance = 0
    transaction_history = ""
    number_of_transactions = 0
    MAX_TRANSACTIONS = 3
    users = []
    accounts = []

    while True:
        selection = menu()

        if selection == "6":
            print("exiting...")
            break

        elif selection == "1":
            value = float(input("\nPlease enter the amount you want to deposit: "))
            balance, transaction_history = deposit(value, balance, transaction_history)

        elif selection == "2":
            value = float(input("\nPlease enter the amount you want to withdraw: "))
            balance, transaction_history, number_of_transactions = withdraw(withdraw=value, balance=balance, transaction_history=transaction_history, limit=limit, number_of_transactions=number_of_transactions, MAX_TRANSACTIONS=MAX_TRANSACTIONS)

        elif selection == "3":
            transactions(balance, transaction_history=transaction_history)
        elif selection == "5":
            users = manage_user(users)
        elif selection == "4":
            accounts = manage_account (users, accounts)
        else :
            print(f"\033[91m\nInvalid input, your option must be between 1 and 4\033[0m")

main()