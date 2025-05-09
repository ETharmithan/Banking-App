# #python Bank_App.py
# #====================================Mini Bank App====================================
# #Customer Create Accountant
# #Get Customer Details=================================================================
# def get_user_details():
#     user_firstname=input("Entert the Firstname: ")
#     user_lastname=input("Entert the Lastname: ")
#     user_date_of_birth=input("Entert the Date of Birth(DD/MM/YYYY): ")
#     user_nic=input("Entert the NIC: ")
#     user_address=input("Entert the Address: ")
#     user_gender=input("Entert the Gender: ")
#     while True:
#         try:
#             user_phonenumber=int(input("Entert the Phone Number: "))
#             break
#         except ValueError:
#             print("Invalid Phone Number. Please Enter Digits Only.")
#     user_email=input("Entert the Email: ")
#     user_job=input("Entert the Job: ")
#     customer_details={
#         "firstname": user_firstname,
#         "lastname" : user_lastname,
#         "nic" : user_nic,
#         "dob" : user_date_of_birth,
#         "address" : user_address,
#         "gender" : user_gender,
#         "phone" : user_phonenumber,
#         "email" : user_email,
#         "job" : user_job
#     }
#     return customer_details

# # Save Custome Details==================================================================
# def save_user_details():
#     customer_details=get_user_details()
#     try:
#         with open("Customer_Personal_Details.txt",'r') as file:
#             last_line=file.readlines()[-1]
#             last_id=last_line.split(" | ")[0] 
#             new_id=(f"C{str(int(last_id[1:])+1)}")
#             with open("Customer_Personal_Details.txt","a") as file1:
#                 file1.write(f"{new_id} | {customer_details['firstname']} | {customer_details['lastname']} | {customer_details['nic']} | {customer_details['dob']} | {customer_details['address']} | {customer_details['email']} | {customer_details['phone']} | {customer_details['gender']} | {customer_details['job']}\n")
#                 print(f"{customer_details['lastname']} details saved successfully.")
#     except FileNotFoundError:
#         with open("Customer_Personal_Details.txt","w") as file1: #First Customer ID Create
#             file1.write(f"C1001 | {customer_details['firstname']} | {customer_details['lastname']} | {customer_details['nic']} | {customer_details['dob']} | {customer_details['address']} | {customer_details['email']} | {customer_details['phone']} | {customer_details['gender']} | {customer_details['job']}\n")
#             print(f"{customer_details['lastname']} details saved successfully.")
#     return last_id
# #Account Create===========================================================================
# def create_accotant():
#     last_id=save_user_details()
#     user_name=input("Enter Your Username: ")
#     user_password=input("Enter Your Password: ")
#     user_initialbalnce=float(input("Enter the Balance: "))
#     try:
#         with open("Account.txt","r") as file:
#             Last_line=file.readlines()[-1]
#             Last_ID=Last_line.split(" | ")[1]
#             New_ID=(f"A{str(int(Last_ID[1:])+1)}")
#             with open("Account.txt","a") as file:
#                 file.write(f"{last_id} | {New_ID} | {user_name} | {user_password} | {user_initialbalnce}\n")
#                 print(f"{user_name} Accountant Create Successfully.")
#     except FileNotFoundError:
#         with open("Account.txt","w") as file:
#             file.write(f"{last_id} | A1001 | {user_name} | {user_password} | {user_initialbalnce}\n")
#             print(f"{user_name} Accountant Create Successfully.")
# create_accotant()

#---------------------Money---------------------
#Amount
def Amount():
    while True:
        try:
            user_amount=float(input("Enter your amount: "))
            if user_amount>0:
                print("payment successfully")
                break
            else:
                print("Only Enter the Positive Amount")
                continue
        except ValueError:
            print("Enter the Only Numbers!")
Amount()
#