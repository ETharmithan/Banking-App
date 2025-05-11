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
        file2.write(f"{customer_id_02} | {New_ID} | {user_initialbalnce} | Deposit | {user_initialbalnce}\n")

#==============================================================================================
#---------------------Money---------------------
#Withdraw======================================================================================
def Withdraw():
    with open("Accounts.txt","r") as file:
        lines=file.readlines()
    input_account_no=input("Enter your account number: ") #Identify User.
    change_data=[]
    for line in lines:
        if input_account_no in line.strip().split(" | "):
            datas=line.strip().split(" | ")
            print(f"Hi, {datas[2]}")
            print(f"Your current balance is {datas[4]}")
            try:
                Amount=float(input("Please enter the amount: "))
                if Amount>0:
                    if Amount<float(datas[-1]):
                        New_balance=float(datas[-1])-Amount
                        print(f"{datas[2]}, you have successfully withdrawn {Amount}.")
                        print(f"Your new balance is {New_balance}.") 
                        change_data.append(f"{datas[0]} | {datas[1]} | {datas[2]} | {datas[3]} | {New_balance}\n")
                        with open("Transaction_History.txt", "a") as file1:
                            file1.write(f"{datas[0]} | {datas[1]} | {Amount} | Withdraw | {New_balance}\n")
                    else:
                        print(f"Reminder: Your current balance is {datas[-1]}")
                else:
                    print("Please enter positive numbers only: ")
            except ValueError:
                print("Please make sure to enter the amount using numbers only!")
        else:
            change_data.append(line)
        with open("Accounts.txt", "w") as file2:
            file2.writelines(change_data)

#Deposit======================================================================================
def Deposit():
    with open("Accounts.txt", "r") as file:
        lines=file.readlines()
    account_number_input=input("Enter your account number: ") #Identify User
    Change_data=[]
    for line in lines:
        if account_number_input in line.strip().split(" | "):
            Datas=line.strip().split(" | ")
            print(f"Hi, {Datas[2]}")
            print(f"Your current balance is {Datas[4]}")
            try:
                Amount=float(input("Please enter the amount: "))
                if Amount>0:
                    new_balance=float(Datas[-1])+Amount
                    print(f"{Datas[2]}, you have successfully deposited {Amount}.")
                    print(f"Your new balance is {new_balance}.")
                    Change_data.append(f"{Datas[0]} | {Datas[1]} | {Datas[2]} | {Datas[3]} | {new_balance}\n")
                    with open("Transaction_History.txt","a") as file1:
                        file1.write(f"{Datas[0]} | {Datas[1]} | {Amount} | Deposit | {new_balance}\n")
                else:
                    print("Please enter positive numbers only: ")
            except ValueError:
                print("Please make sure to enter the amount using numbers only!")
        else:
            Change_data.append(line)
        with open("Accounts.txt", "w") as file2:
            file2.writelines(Change_data)

#Transaction History===========================================================================
#Customer Transaction History==================================================================
def Customer_Transaction_History():
    with open("Transaction_History.txt","r") as file:
        lines=file.readlines()
    enter_account_id=input("Enter your account ID: ")
    customer_history=[]
    for line in lines:
        if enter_account_id in line.strip().split(" | "):
            records=line.strip().split(" | ")
            print(records)
            # customer_history.append(f"{records[0]} | {records[1]} | {records[2]} | {records[3]} | {records[4]}")
            # print(customer_history)
Customer_Transaction_History()





'''
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
    print("1.Deposit Money")
    print("2.Withdraw Money")
    print("3.Check Balance")
    print("4.Transaction History")
    print("5.Exit")
    while True:    
        try:
            choose=int(input("Enter The Number Only(1 to 5): "))
            if choose==1:
                Deposit()
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
Menu()'''