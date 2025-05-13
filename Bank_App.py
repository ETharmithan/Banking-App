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
            new_id=(f"C{str(int(last_id[1:])+1)}") 
            with open("Customer_Personal_Details.txt","a") as file1:
                file1.write(f"{new_id} | {customer_details['firstname']} | {customer_details['lastname']} | {customer_details['nic']} | {customer_details['dob']} | {customer_details['address']} | {customer_details['email']} | {customer_details['phone']} | {customer_details['gender']} | {customer_details['job']}\n")
                print(f"{customer_details['lastname']} details saved successfully.")
    except FileNotFoundError:
        with open("Customer_Personal_Details.txt","w") as file1: 
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
            New_ID=(f"A{str(int(Last_ID[1:])+1)}") 
            with open("Accounts.txt","a") as file:
                file.write(f"{customer_id_02} | {New_ID} | {user_name} | {user_password} | {user_initialbalnce}\n")
                print(f"{user_name} Accountant Create Successfully.")
    except FileNotFoundError:
        New_ID="A1001"
        with open("Accounts.txt","w") as file:
            file.write(f"{customer_id_02} | {New_ID} | {user_name} | {user_password} | {user_initialbalnce}\n") 
            print(f"{user_name} Accountant Create Successfully.")
    with open("Transaction_History.txt","a") as file2:
        file2.write(f"{customer_id_02} | {New_ID} | {user_initialbalnce} | Deposit | {user_initialbalnce}\n")

#==============================================================================================
#---------------------Money---------------------
#Withdraw======================================================================================
def Withdraw(customer_id_03):
    with open("Accounts.txt","r") as file:
        lines=file.readlines()
    # input_account_no=input("Enter your account number: ") 
    change_data=[]
    for line in lines:
        if customer_id_03 in line.strip().split(" | "):
            datas=line.strip().split(" | ")
            print(f"Hi, {datas[2]}")
            print(f"Your current balance is {datas[4]}")
            while True:
                Confirmation_password=input("Enter the user password: ")
                if datas[3]==Confirmation_password:
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
                                    break
                            else:
                                print(f"Reminder: Your current balance is {datas[-1]}")
                        else:
                            print("Please enter positive numbers only: ")
                    except ValueError:
                        print("Please make sure to enter the amount using numbers only!")
                else:
                    print("Recheck your password")
        else:
            change_data.append(line)
        with open("Accounts.txt", "w") as file2:
            file2.writelines(change_data)

#Deposit======================================================================================
def Deposit(customer_id_03,):
    with open("Accounts.txt", "r") as file:
        lines=file.readlines()
    # account_number_input=input("Enter your account number: ") 
    Change_data=[]
    for line in lines:
        if customer_id_03 in line.strip().split(" | "):
            Datas=line.strip().split(" | ")
            print(f"Hi, {Datas[2]}")
            print(f"Your current balance is {Datas[4]}")
            while True:
                confirmation_password=input("Enter the user password: ")
                if Datas[3]==confirmation_password:
                    try:
                        Amount=float(input("Please enter the amount: "))
                        if Amount>0:
                            new_balance=float(Datas[-1])+Amount
                            print(f"{Datas[2]}, you have successfully deposited {Amount}.")
                            print(f"Your new balance is {new_balance}.")
                            Change_data.append(f"{Datas[0]} | {Datas[1]} | {Datas[2]} | {Datas[3]} | {new_balance}\n")
                            with open("Transaction_History.txt","a") as file1:
                                file1.write(f"{Datas[0]} | {Datas[1]} | {Amount} | Deposit | {new_balance}\n")
                                break
                        else:
                            print("Please enter positive amount only: ")
                    except ValueError:
                        print("Please make sure to enter the amount using numbers only!")
                else:
                    print("Recheck your password")
        else:
            Change_data.append(line)
        with open("Accounts.txt", "w") as file2:
            file2.writelines(Change_data)

#Transaction History===========================================================================
#Customer Transaction History==================================================================
def Customer_Transaction_History(customer_id_03):
    with open("Transaction_History.txt","r") as file:
        lines=file.readlines()
    # enter_account_id=input("Enter your account ID: ")
    customer_history=[]
    for line in lines:
        if customer_id_03 in line.strip().split(" | "):
            records=line.strip().split(" | ")
            print(f"{records[1]} | {records[2]} | {records[3]} | {records[4]}")

#Show Balance==================================================================================
def Show_Balance(customer_id_03):
    with open("Accounts.txt", "r") as file:
        lines=file.readlines()
    # Enter_account_id=input("Enter your account ID: ")
    for line in lines:
        if customer_id_03 in line.strip().split(" | "):
            print(f"Hi, {line.strip().split(" | ")[2]}")
            print(f"Your balance is {line.strip().split(" | ")[-1]}.")

#Customer Menu=================================================================================
def Customer_Menu(customer_id_03):
    with open("Accounts.txt", "r") as file:
        lines=file.readlines()

    for line in lines:
        if customer_id_03 in line.strip().split(" | "):
            while True:
                print(f"---------Welcome To Mini Bank---------\n-----------Have a Great Day-----------\nHi,{line.strip().split(" | ")[2]}\n")
                print(f"Customer ID: {line.strip().split(" | ")[0]}\nAccount ID: {line.strip().split(" | ")[1]}\nHow can I help you?\n")
                print("1.Deposit Money")
                print("2.Withdraw Money")
                print("3.Show Balance")
                print("4.Transaction History")
                print("5.Exit")    
                try:
                    choose=int(input("Enter the number only (1 to 5): "))
                    if choose>0:
                        if choose==1:
                            Deposit(customer_id_03)
                        elif choose==2:
                            Withdraw(customer_id_03)
                        elif choose==3:
                            Show_Balance(customer_id_03)
                        elif choose==4:
                            Customer_Transaction_History(customer_id_03)
                        elif choose==5:
                            print("Thank you for choosing us!")
                            break
                        else:
                            print("Please select only between 1 and 5.")
                    else:
                        print("Please enter positive numbers only")
                except ValueError:
                    print("Please enter numbers only!")

#Admin Menu====================================================================================
def Admin_Menu():
    while True:
        print(f"---------Welcome To Mini Bank---------\n-----------Have a Great Day-----------\nHi, Admin\nHow can I help you?\n")
        print("1.Customer Register")
        print("2.Create Account")
        print("3.Deposit")
        print("4.Withdraw")
        print("5.Transaction History")
        print("6.Check Balance")
        # print("7.Back to MainMenu")
        print("7.Exit")
        try:
            choose=int(input("Enter the number only (1 to 7): "))
            if choose>0:
                if choose==1:
                    save_user_details()
                elif choose==2:
                    create_account()
                elif choose==3:
                    customer_id_03=input("Enter the Customer ID: ")
                    Deposit(customer_id_03)
                elif choose==4:
                    customer_id_03=input("Enter the Customer ID: ")
                    Withdraw(customer_id_03)
                elif choose==5:
                    customer_id_03=input("Enter the Customer ID: ")
                    Customer_Transaction_History(customer_id_03)
                elif choose==6:
                    customer_id_03=input("Enter the Customer ID: ")
                    Show_Balance(customer_id_03)
                # elif choose==7:
                #     print("Going to Mainmenu👈")
                #     break  
                elif choose==7:
                    print("Thank you for choosing us!")
                    break
                else:
                    print("Please select only between 1 and 7!")
            else:
                print("Please enter positive numbers only")
        except ValueError:
            print("Please enter numbers only!")
        
#Choose User===================================================================================
def users():
    while True:
        print("========================💱Welcome-To-Mini-Banking-System💱=========================")
        print("1.Admin Login")
        print("2.Customer Login")
        print("3.Exit")
        try:
            select=int(input("Choose the number (1 to 3): "))
            if select>0 and select<4:
                if select==1:
                    print("Opening Admin Menu👉...")
                    admin_username="Admin"
                    admin_password="Admin143"
                    input_admin_name=input("Enter the Admin name(Admin): ")
                    input_admin_password=input("Enter the Admin Password(Admin143): ")
                    if admin_username==input_admin_name and admin_password==input_admin_password:
                        Admin_Menu()
                        break
                    else:
                        print("Please Check your Username or Userpassword!")
                elif select==2:
                    print("Opening Customer Menu👉...")
                    try:
                        with open("Accounts.txt", "r") as file:
                            lines=file.readlines()
                    except FileNotFoundError:
                        print("Invalid account")
                    customer_username=input("Enter the User name: ")
                    customer_password=input("Enter the Password: ")
                    for line in lines:
                        datas=line.strip().split(" | ")
                        if datas[2]==customer_username and datas[3]==customer_password:
                            customer_id_03=datas[0]
                            print(f"{datas[2]} Login successfully.")
                            Customer_Menu(customer_id_03)
                    else:
                        print("Invalid Username or Password!")
                else:
                    print("Thank you for choosing us!")
                    break
            else:
                print("Please enter only the positive number 1 to 3!")
        except ValueError:
            print("Please enter numbers only!")
users()
