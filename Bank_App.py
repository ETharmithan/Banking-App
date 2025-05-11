#python Bank_App.py
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
        print("Enter Amount Numbers Only!")

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
        New_ID="A1001"
        with open("Accounts.txt","w") as file:
            file.write(f"{customer_id_02} | {New_ID} | {user_name} | {user_password} | {user_initialbalnce}\n") ##First Account ID Create
            print(f"{user_name} Accountant Create Successfully.")
    with open("Transaction_History.txt","a") as file2:
        file2.write(f"{customer_id_02} | {New_ID} | +{user_initialbalnce} | {user_initialbalnce}\n")
#==============================================================================================
#---------------------Money---------------------
#Amount========================================================================================
# def Amount():    
#     while True:
#         try:
#             user_amount=float(input("Enter your amount: "))
#             if user_amount>0:
#                 return user_amount
#             else:
#                 print("Only Enter the Positive Amount")                
#         except ValueError:
#             print("Enter  Only Numbers!")

# # Balance=======================================================================================
# def Balance():
#     with open("Accounts.txt", "r") as file:
#         customer_details=file.readlines()
#         for gets in customer_details:
#             customer_id=customer_details.split(" | ")[0]
#             customer_balance=customer_details.split(" | ")[4]
#             if user_id == customer_id:
#                 return [customer_id,customer_balance]
#Withdraw======================================================================================
def Withdraw():
    with open("Accounts.txt","r") as file:
        lines=file.readlines()
    for line in lines:
            customer_id_04=line.split(" | ")[0]
            customer_account_id_02=line.split(" | ")[1]
            customer_user_name_01=line.split(" | ")[2]
            customer_user_password_01=line.split(" | ")[3]
            # check_user_name=input("Enter the User Name: ")
            check_user_password_01=input("Enter the User Password: ")
            if customer_user_password_01==check_user_password_01:
                customer_old_balance_01=line.split(" | ")[4]
                try:
                    Amount_01=float(input("Enter the Amount: "))
                    if Amount_01>=0:
                        if Amount_01<=float(customer_old_balance_01):
                            New_balance_01=float(customer_old_balance_01)-Amount_01
                            print(f"{customer_user_name_01} has Successfully Withdrwed {Amount_01}.")
                            print(f"Your New Balance is {New_balance_01}.")
                            with open("Transaction_History.txt", "a") as file: #Add a Transaction History
                                file.write(f"{customer_id_04} | {customer_account_id_02} | -{Amount_01} | {New_balance_01}\n")
                                break
                        else:
                            print(f"Reminder Your Current Balance is {customer_old_balance_01}")
                    else:
                        print("Enter Only Positive Numbers.")
                except ValueError:
                    print("Amount is Enter Numbers only!")
            else:
                print("Check Your Username or Userpassword!")    
#Deposite======================================================================================
def Deposite():
    with open("Accounts.txt","r") as file:
        lines=file.readlines()
    for line in lines:
            customer_id_03=line.split(" | ")[0]
            customer_account_id_01=line.split(" | ")[1]
            customer_user_name=line.split(" | ")[2]
            customer_user_password=line.split(" | ")[3]
            # check_user_name=input("Enter the User Name: ")
            check_user_password=input("Enter the User Password: ")
            if customer_user_password==check_user_password:
                try:
                    Amount=float(input("Enter the Amount: "))
                    if Amount>=0:
                        customer_old_balance=line.split(" | ")[4]
                        New_balance=float(customer_old_balance)+Amount
                        print(f"{customer_user_name} has Successfully Deposited {Amount}.")
                        print(f"Your New Balance is {New_balance}.")
                        with open("Transaction_History.txt", "a") as file: #Add a Transaction History
                            file.write(f"{customer_id_03} | {customer_account_id_01} | +{Amount} | {New_balance}\n")
                        break
                    else:
                        print("Enter Only Positive Numbers.")
                except ValueError:
                    print("Amount is Enter Numbers only!")
            else:
                print("Check Your Username or Userpassword!")    
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
                    print(f"Your Current Balance is ")
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
def customer_menu():
    print("---------Welcome To Mini Bank---------")
    print("1.Deposite Money")
    print("2.Withdraw Money")
    print("3.Check Balance")
    print("4.Transaction History")
    print("5.Exit")
    while True:    
        try:
            choose=int(input("Enter The Number Only(1 to 5): "))
            if choose==1:
                Deposite()
            elif choose==2:
                Withdraw()
            elif choose==3:
                check_balance()
            elif choose==4:
                Transaction_History()
            elif choose==5:
                print("Thanks for coming!")
                exit()
            else:
                print("You can Choice only (1 to 5): ")
        except ValueError:
            print("Enter  Only Numbers!")
# customer_menu()

#Check User====================================================================================
def Check_User():
    # with open("Accounts.txt", "r") as username_password:
    #     get_username_password = username_password.readlines()
    # while True:
    #     user_name = input("Enter your user name: ")
    #     password = input("Enter your password: ")
    #     for i in get_username_password:
    #         get_user = i.split("|")[2].strip()
    #         get_password = i.split("|")[3].strip()
    #         get_customer_id = i.split("|")[0].strip()
    #         get_account_id = i.split("|")[1].strip()
    #         if user_name == get_user and password == get_password:
    #             customer_menu(get_customer_id,get_account_id,get_user,get_password)
    

                


#Admin Menu====================================================================================
def Admin_Menu():
    while True:
        print("Hi, Admin")
        print("1.Save User Details")
        print("2.Account Create")
        print("")
        print("")
        print("")
        print("")
        print("")



#Menu==========================================================================================
def Menu():
    while True:
        print("---------Welcome to Mini Bank!---------")
        print("1.Admin login.")
        print("2.Customer login.")
        print("3.Exit.")
        try:
            Choose=int(input("Choose the Numbers(1 to 3): "))
            if Choose>0 and Choose<4:   
                if Choose==1:
                    Check_User()
                    Admin_Menu()
                    pass
                elif Choose==2:
                    Check_User()
                    customer_menu()
                elif Choose==3:
                    print("Thanks For UsingSystem!")
                    exit()
            else:
                print("Only Type Positive Numbers! and  Choose 1 to 3")
        except ValueError:
            print("Only choose Numbers!")
Menu()