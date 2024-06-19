menu_options = """

        [1] deposit
        [2] withdraw
        [3] balance
        [4] exit

"""
saldo = 0
limit = 500
balance = 0
number_of_transactions = 0
MAX_TRANSACTIONS = 3

while True:
    option = input(menu_options)

    if option == "4":
        print("exiting...")
        break
    elif option == "1":
        #print("depositing...")
        deposit = float(input("\nPlease enter the amount you want to deposit: "))
        if deposit >= 0:
            balance += deposit
            print(f"\033[92m\nDeposit complete\033[0m")
        else:
            print(f"\033[91m\nYou can't deposit a negative amount\033[0m")
           

        pass
    elif option == "2":
        #print("withdrawing...")
        if number_of_transactions < MAX_TRANSACTIONS:
            if balance <= 0:
                print(f"\033[91m\nYou don't have enough money\033[0m")
            else:
                withdraw = float(input("\nPlease enter the amount you want to withdraw: "))
                if withdraw > limit:
                    print(f"\033[91m\nYou can't withdraw more than R$500,00\033[0m")
                elif withdraw > balance:
                    print(f"\033[91m\nYou are trying to withdraw more than your balance\033[0m")
                else:
                    balance -= withdraw
                    number_of_transactions += 1
                    print(f"\033[92m\nWithdrawal transaction complete\033[0m")
        else:
            print(f"\033[91m\nYou have reached the maximum number of transactions\033[0m")
            
    elif option == "3":
        #print("checking balance...")
        print(f"\nYour balance is R${balance:.2f}")
    else :
        print(f"\033[91m\nInvalid input, your option must be between 1 and 4\033[0m")