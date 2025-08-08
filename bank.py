def view_accounts(banksys):
    if not banksys:
        print("No accounts are added")
    else:
        print(banksys)

def add_account(banksys,detail):
    account = input("Enter the Account Number: ")
    name = input('Enter the name of Account Holder: ')
    balance = float(input('Enter the Balance: '))
    detail['Name'] = name
    detail['Balance'] = balance
    banksys[account] = detail


def deposit_money(banksys):
    daccount = input("Enter the Account Number: ")
    dmoney = float(input("Enter the amount to deposit: "))
    banksys[daccount]['Balance'] += dmoney
    print("Rs.",dmoney," has been deposited")

def withdraw_money(banksys):
    waccount = input("Enter the Account Number: ")
    wmoney = float(input("Enter the amount to withdraw: "))
    banksys[waccount]['Balance'] += wmoney
    print("Rs.",wmoney, " has been withdrawn")

def check_balance(banksys):
    baccount = input("Enter the Account Number: ")
    print("The current Balance is: ","Rs.",banksys[baccount]['Balance'])



def bankman():
    banksys = {}
    detail = {'Name':'','Balance':''}

    print('''** Options **
    1: View All Accounts
    2: Create New Account
    3: Deposit Money
    4: Withdraw Money
    5: Check Balance
    6: Exit''')

    while True:
        option = int(input("Enter the option: "))
        if option == 1:
            view_accounts(banksys)

        elif option == 2:
            add_account(banksys,detail)

        elif option == 3:
            deposit_money(banksys)

        elif option == 4:
            withdraw_money(banksys)

        elif option == 5:
            check_balance(banksys)

        elif option == 6:
            print("Exiting the Banking Management System...")
            break

        else:
            print("Invalid Choice")
            continue
bankman()

