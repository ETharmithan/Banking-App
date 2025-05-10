#python Bank_App.py
def choice_number(para):
    while True:
        try:
            number = int(input(para))
            if number > 0:
                return number
            else:
                print("Enter a positive number.")
        except ValueError:
            print("Enter a number.")





#====================================Mini Bank App====================================
#Customer Create Accountant
#Get Customer Details=================================================================
def get_user_details():
    user_firstname=input("Enter the Firstname: ")
    user_lastname=input("Enter the Lastname: ")
    user_date_of_birth=input("Enter the Date of Birth(DD/MM/YYYY): ")
    user_nic=input("Enter the NIC: ")
    user_address=input("Enter the Address: ")
    user_gender=input("Enter the Gender: ")
    while True:
        try:
            user_phonenumber=int(input("Enter the Phone Number: "))
            break
        except ValueError:
            print("Invalid Phone Number. Please Enter Digits Only.")
    user_email=input("Enter the Email: ")
    user_job=input("Enter the Job: ")
    customer_details={
        "firstname": user_firstname,
        "lastname" : user_lastname,
        "nic" : user_nic,
        "dob" : user_date_of_birth,
        "address" : user_address,
        "gender" : user_gender,
        "phone" : user_phonenumber,
        "email" : user_email,
        "job" : user_job
    }
    return customer_details

# Save Custome Details==================================================================
def save_user_details():
    customer_details=get_user_details()
    try:
        with open("Customer_Personal_Details.txt",'r') as file:
            last_line=file.readlines()[-1]
            last_id=last_line.split(" | ")[0].strip()
            new_id=(f"C{str(int(last_id[1:])+1)}") #Auto Generate Customer ID
            with open("Customer_Personal_Details.txt","a") as file1:
                file1.write(f"{new_id} | {customer_details['firstname']} | {customer_details['lastname']} | {customer_details['nic']} | {customer_details['dob']} | {customer_details['address']} | {customer_details['email']} | {customer_details['phone']} | {customer_details['gender']} | {customer_details['job']}\n")
                print(f"{customer_details['lastname']} details saved successfully.")
    except FileNotFoundError:
        with open("Customer_Personal_Details.txt","w") as file1: #First Customer ID Create
            file1.write(f"C1001 | {customer_details['firstname']} | {customer_details['lastname']} | {customer_details['nic']} | {customer_details['dob']} | {customer_details['address']} | {customer_details['email']} | {customer_details['phone']} | {customer_details['gender']} | {customer_details['job']}\n")
            print(f"{customer_details['lastname']} details saved successfully.")

#Account Create===========================================================================
def create_account():
    user_name=input("Enter Your Username: ")
    user_password=input("Enter Your Password: ")
    try:
        user_initialbalnce=float(input("Enter the Balance: "))
    except ValueError:
        print("Enter Amount Digits Only!")

    with open("Customer_Personal_Details.txt","r") as file1:
        customer_id_01=file1.readlines()[-1]
        customer_id_02=customer_id_01.split(" | ")[0]
    try:
        with open("Accounts.txt","r") as file:
            Last_line=file.readlines()[-1]
            Last_ID=Last_line.split(" | ")[1]
            New_ID=(f"A{str(int(Last_ID[1:])+1)}") #Auto Generate Account ID
            with open("Accounts.txt","a") as file:
                file.write(f"{customer_id_02} | {New_ID} | {user_name} | {user_password} | {user_initialbalnce}\n")
                print(f"{user_name} Accountant Create Successfully.")
    except FileNotFoundError:
        with open("Accounts.txt","a") as file:
            file.write(f"{customer_id_02} | A1001 | {user_name} | {user_password} | {user_initialbalnce}\n") ##First Account ID Create
            print(f"{user_name} Accountant Create Successfully.") 
# create_account()

#==============================================================================================
#---------------------Money---------------------
#Amount========================================================================================
def Amount():
    
    while True:
        try:
            user_amount=float(input("Enter your amount: "))
            if user_amount>0:
                return user_amount
            else:
                print("Only Enter the Positive Amount")
                
        except ValueError:
            print("Enter  Only Numbers!")

#Balance=======================================================================================
def Balance():
    with open("Accounts.txt", "r") as file:
        customer_details=file.readlines()
        for gets in customer_details:
            customer_id=customer_details.split(" | ")[0]
            customer_balance=customer_details.split(" | ")[-1]
            if user_id == customer_id:
                return [customer_id,customer_balance]
#Withdraw======================================================================================
def Withdraw(user_ID):
    balance=Balance()
    while True:
        amount=Amount()
        if amount <= balance:
            new_balance=balance-amount
            print("Payment SuccessFully.")
            print(f"Your Current Balance is {new_balnce}.")
            break
        else:
            print("Not enough money in your account. Recheck your Amount!")

    # with open('')


# Withdraw()
#Deposite======================================================================================
def Deposite():
    balance_01=Balance()
    amount_01=Amount()
    new_balance_01=balance_01+amount_01
    print(new_balance_01)
# Deposite()
#Transaction History===========================================================================
# ?def Transaction():

#Check Balance=================================================================================
def check_balance():
    with open("Accounts.txt", "r") as file:
        get_Account=file.readlines()
        for account in get_Account:
            account_no=account.split(" | ")[1]
            while True:
                Account_No=input("Enter the Account Number: ")
                if account_no==Account_No:
                    print(f"Your Current Balance is {new_balance}")
                    break
                else:
                    print("Your Account Number is Insufficient. Please Check Your Account Number!")
# check_balance()
#Delete========================================================================================
#Delete Account
def Delete_Account():
    with open("Accounts.txt","r") as file:
        get_account=file.readlines()
        for account_01 in get_account:
            delete_account_id=account_01.split(" | ")[1]
            while True:
                Delete_account_id=input("Enter Delete Id: ")
                if delete_account_id==Delete_account_id:
                    print("Successfully Remove.")
                    break
                else:
                    print("Your Account Number is Insufficient. Please Check Your Account Number!")
# Delete_Account()













#Customer Menu=================================================================================
def customer_menu(get_customer_id,get_account_id,get_user,get_password):
    print("Welcome To Mini Bank")
    pass


## 
def check_user():
    with open("Accounts.txt", "r") as username_password:
        get_username_password = username_password.readlines()
    while True:
        user_name = input("Enter your user name: ")
        password = input("Enter your password: ")
        for i in get_username_password:
            get_user = i.split("|")[2].strip()
            get_password = i.split("|")[3].strip()
            get_customer_id = i.split("|")[0].strip()
            get_account_id = i.split("|")[1].strip()
            if user_name == get_user and password == get_password:
                customer_menu(get_customer_id,get_account_id,get_user,get_password)
    

                



def Menu():
    while True:
        print("Welcome to Mini Bank!")
        print("1.Admin login.")
        print("2.Customer login.")
        print("3.Exit.")
        choice = choice_number("Enter your choice: ")
        if choice < 3 :
            if choice == 1:
                pass
            elif choice == 2:
                customer_menu()
        elif choice == 3:
            break
        else:
            print("Enter the correct number.")

