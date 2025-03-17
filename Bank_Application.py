from getpass import getpass
import string

def password_validation(password):
    i = 0
    lower = False
    upper = False
    digit = False
    special = False
    if len(password) >= 6:
        while i < len(password):
            if password[i].islower():
                lower = True
            elif password[i].isupper():
                upper = True
            elif password[i].isdigit():
                digit = True
            elif password[i] in string.punctuation:
                special = True
            i += 1
        if all([lower, upper, digit, special]):
            return True
        else:
            return False
    else:
            return False
        
users_data = {}
def signup():
    user_name = input("Enter your name : ")
    password = getpass("Enter your password with length 6 and includes [A-Z,a-z,0-9,!@#$%] : ")
    if password_validation(password):
        print("Note :- Initial amount of 2000 or more is required to open an account in the bank...")
        balance = int(input("How much initial amount you want to add : "))
        if balance >= 2000:
            acc_no = 1000 + (len(users_data)) + 1
            print(f"Account created successfully\nYour Account Number : {acc_no}")
            print(f"Note down your account number and save it for future use")
            users_data[acc_no]={"name" : user_name,"balance" : balance,"password" : password}
            login()
        else:
            print("Initial amount is low please try again\n")
            bank_application_menu()
    else:
        print("Password is not valid please try again\n")
        bank_application_menu()

def login():
    acc_no = int(input("Enter your Account Number : "))
    if acc_no in users_data.keys():
        password = getpass("Enter your Password : ")
        if password == users_data[acc_no]["password"]:
            print("Login successfully...")
            bank_dashboard(acc_no)
        else:
            print("User password is incorrect please try again\n")
            bank_application_menu()
    else:
        print("User account not found\n")
        bank_application_menu()

def bank_dashboard(acc_no):
    print("\nWelcome to dashboard of Python Bank")
    print("1. Credit\n2. Debit\n3. Change Password\n4. Check Balance\n5. Logout")
    query = int(input("Enter your query : "))
    if query == 1:
        amount = int(input("Enter credit amount : "))
        users_data[acc_no]["balance"] += amount
        print("Amount credited successfully...")
        bank_dashboard(acc_no)
    elif query == 2:
        amount = int(input("Enter debit amount : "))
        if users_data[acc_no]["balance"] - amount < 2000:
            print("\nNot enough balance...")
            bank_dashboard(acc_no)
        else:
            users_data[acc_no]["balance"] -= amount
            print("Amount debited successfully...")
            bank_dashboard(acc_no)
    elif query == 3:
        new_password = getpass("Enter your new password : ")
        if password_validation(new_password):
            users_data[acc_no]["password"] = new_password
            print("Password changed successfully...")
            bank_dashboard(acc_no)
        else:
            print("Please enter strong password with length 6 and includes [A-Z,a-z,0-9,!@#$%]")
            bank_dashboard(acc_no)
    elif query == 4:
        print("Your total balance is :",users_data[acc_no]["balance"])
        bank_dashboard(acc_no)
    elif query == 5:
        print("Thank you for using our services")
        print("Logout successfully...\n")
        bank_application_menu()
    else:
        print("Invalid query input..?")
        bank_dashboard(acc_no)

def bank_application_menu():
    print("______WELCOME TO PYTHON BANK______\nPlease choose option from below\n1.Login\n2.Signup\n3.Exit\n___________________________________")
    userip=(int(input(" Please type the number\n")))
    if userip==1:
        login()
    elif userip==2:
        signup()
    elif userip==3:
        print("Thanks for using bank application\n\tBYE")
        exit
    else:
        print("Try again\n")
        bank_application_menu()

bank_application_menu()
