from sys import float_repr_style
from import_methods import *
from Main_Menu import main_Menu, text_Delay, main_Menu_selection, temp_cur_Bal
from ATM_Database import *
from Password_Check import *
from Loading_System import *

time_sec = 0.02
counter_for_first_run = True

# This part is for User Main Menu using Function
def user_Main_menu():
    global counter_for_first_run 
    if counter_for_first_run == True:
        text_Delay("_"*16, time_sec)
        text_Delay("    ANKUDI's BANK OF INDIA     ", time_sec)
        text_Delay("_"*16, time_sec)
        print("\n")
        print("-"*16,"WELCOME TO VIN4U_ANKUDI's ATM","-"*16,"\n")
    else:
        print("_"*16, end="")
        print("    ANKUDI's BANK OF INDIA     ", end="")
        print("_"*16, end="")
        print("\n")
        print("-"*16,"WELCOME TO VIN4U_ANKUDI's ATM","-"*16,"\n")
    
# This part is for User Main Menu using Function
def user_Option():
    print("Menu's to Access Banks Services : \n")
    text_Delay("\t1. Login \t\t2. Create Account \n\t3. Forgot Passowrd \t4. Cancel", time_sec)
    print("\n")
    while True:
        try:
            user_Menu_opt = int(input("Select Above Option : "))
            break
        except ValueError:
            print("\n\tYou are Entered Wrong Characters...!\n\tPlese Enter Right Given Number...\n")
            continue
    if user_Menu_opt == 1:
        login_Existing_user()
    elif user_Menu_opt == 2:
        create_New_account()
    elif user_Menu_opt == 3:
        forgot_Password()
    elif user_Menu_opt == 4:
        user_Exit_menu()
    else:
        print("\n\tYour are Entered Wrong Choice...\n\tPlease Select Correct Option....!\n")
        user_Exit_menu()
        
# This part is for Create New User using Function
# cursor = conn.cursor()
# select_acc_no = cursor.execute('SELECT MAX(Sr_No), AC_No FROM New_User_Details')
# for row in select_acc_no:
#     pass
# acc_No = row[1]
# print(acc_No)

def create_New_account():
    global counter_for_first_run
    os.system("cls")
    text_Delay("\t\t---> CREATE NEW BANK ACCOUNT <---",time_sec)
    print('\n')
    text_Delay("First Name \t\t: \t", time_sec)
    first_Name = input()
    text_Delay("Middle Name \t\t: \t", time_sec)
    middle_name = input()
    text_Delay("Last Name \t\t: \t", time_sec)
    last_name = input()
    text_Delay("Gender (Enter Option)\t:--\t", time_sec)
    print()
    while True:
        try:
            text_Delay("1) Male \t2) Female \t3) Other : ", time_sec)
            gender_Opt = int(input())
            break
        except ValueError:
            print("\n\tYou are Entered Wrong Characters...!\n\tPlese Enter Right Given Number...\n")
            continue
    if gender_Opt == 1:
        gender = 'Male'
    elif gender_Opt == 2:
        gender = 'Female'
    elif gender_Opt == 3:
        gender = 'Other'
    else:
        print('Wrong Choice....!')
    text_Delay("Marital Status \t: \t", time_sec)
    print()
    while True:
        try:
            text_Delay("1) Married \t2) Unmarried : ", time_sec)
            marital_Opt = int(input())
            break
        except ValueError:
            print("\n\tYou are Entered Wrong Characters...!\n\tPlese Enter Right Given Number...\n")
            continue
    if marital_Opt == 1:
        status = 'Married'
    elif marital_Opt == 2:
        status = 'Unmarried'
    else:
        print('Wrong Choice....!')
    text_Delay("Permanent Address \t: \t", time_sec)
    user_Address = input()
    text_Delay("City/ Villege \t\t: \t", time_sec)
    user_City = input()
    text_Delay("Taluka \t\t\t: \t", time_sec)
    user_Tal = input()
    text_Delay("District \t\t: \t", time_sec)
    user_Dist = input()
    text_Delay("State \t\t\t: \t", time_sec)
    user_State = input()
    while True:
        try:
            text_Delay("Your Mobile No. \t: \t", time_sec)
            mob_No = int(input())
            break
        except ValueError:
            print("\n\tPlease Enter Correct Mobile Number...!\n")
            continue
    while True:
        try:
            text_Delay("Adhar Card No. \t\t: \t", time_sec)
            adhar_No = int(input())
            break
        except ValueError:
            print("\n\tPlease Enter Correct Adhar Number...!\n")
            continue
    text_Delay("PAN Card No. \t\t: \t", time_sec)
    pan_No = input()
    text_Delay("\nDo You Want To Create Account ? Y/N : ", time_sec)
    confirm_Create_ac = input()
    if confirm_Create_ac in ('y', 'Y', 'yes', 'YES'):
        confirmation = 'Yes'
    else:
        confirmation = 'No'
    if confirm_Create_ac in ('y', 'Y', 'yes', 'YES'):
        insert_Record_New_AC(first_Name, middle_name, last_name, gender, status, user_Address, user_City, user_Tal, user_Dist, user_State, mob_No, adhar_No, pan_No, confirmation)
        print()
        text_Delay('Welcome to Ankudi_Vinudi Bank Service....', 0.02)
        print()
        text_Delay(f'Hello Mr/Mrs. {first_Name} {last_name}', 0.02)
        print()
        print('Your Account has been Created...!')
        print()
        text_Delay('Your New System Generated Account No. is ', 0.02)
        print()
        cursor = conn.cursor()
        select_acc_no = cursor.execute('SELECT MAX(Sr_No), AC_No FROM New_User_Details')
        for row in select_acc_no:
            pass
        acc_No = row[1]
        print('\t---> ', acc_No, ' <---')
        print()
        text_Delay('To Access Your Banking Option Please Set User Name and Password...', 0.02)
        print('\n')
        first_Run_Table()
        password_check()
    else:
        os.system("cls")
        counter_for_first_run = False
        user_Main_menu()
        user_Option()

# This part is for Existing Use Login using Function
def login_Existing_user():
    count = 0
    num = 3
    # user_Main_menu()
    print()
    while count < num:
        U_Name = input("Enter User Name \t:\t ")
        U_Password = input("Enter Password \t\t:\t ")
        cursor = conn.cursor()
        cursor.execute(f"SELECT User_Name, Password FROM New_User_Login WHERE User_Name = '{U_Name}' AND Password = '{U_Password}'")
        if cursor.fetchone():
            cursor.execute(f"SELECT AC_No FROM New_User_Login WHERE User_Name = '{U_Name}' AND Password = '{U_Password}'")
            login = cursor.fetchone()
            for login_row in login:
                pass
            cursor.execute(f"SELECT AC_No, first_name, Middle_Name, Last_Name FROM New_User_Details WHERE AC_No = '{login_row}'")
            user_all_details = cursor.fetchall()
            for user_name in user_all_details:
                pass
            text_Delay("\n\tSuccessfully Login.....", 0.02)
            temp_Ac_No(user_name[0])
            temp_cur_Bal(user_name[0])
            time.sleep(0.8)
            os.system('cls')
            main_Menu()
            print(f' ------ > WELCOME MR/MRS. {user_name[1]} {user_name[2]} {user_name[3]} < ------\n')
            main_Menu_selection()
            break
        else:
            count +=1
            if count != 3:
                text_Delay("\n\tWrong User Name or Password...!\n\tPlease Try Again..!", 0.01) 
                print()
                text_Delay(f"\tYou have only {num - count} attempt left\n", 0.01)
                print()
            else:
                text_Delay("\nSorry... You have Excessed Password Attempts..!", 0.01)
                print()
                text_Delay("Your account has been Blocked for 24 hours...!\n", 0.01)
                time.sleep(1.8)
                os.system('cls')
                user_Main_menu()
                user_Option()

# This part is for Guest Use Login using Function
def forgot_Password():
    while True:
        forgot_mob_no = int(input("Enter Mobile Number \t:\t"))
        cursor.execute(f"SELECT Mob_No, AC_No FROM New_User_Details WHERE Mob_No = {forgot_mob_no}")
        select_row = cursor.fetchall()
        for mob_row in select_row:
            pass
        if select_row:
            get_user_name = input("Enter User Name / AC No :\t")
            cursor.execute(f"SELECT AC_No, User_Name, Password FROM New_User_Login WHERE AC_No = '{mob_row[1]}' AND User_Name = '{get_user_name}' OR AC_No = '{get_user_name}'")
            select_User_row = cursor.fetchall()
            for user_row in select_User_row:
                pass
            if select_User_row:
                print("\nPASSWORD for Account No. ", user_row[0], " is \n\t------->  ", user_row[2], "  <-------\n")
                user_Exit_menu()
                break
            else:
                print("\nUser Name or Account Number Does not match with given Mobile Number.")
                print("Please Check and Enter Correct User Name or Account Number.\n")
        else:
            print("\nBank Account is Not Found with Given Mobile Number OR\nGiven Mobile Number is Not Linked with Bank Account.\n")

# This part is for Close Menu Options using Function
def user_Exit_menu():
    global counter_for_first_run
    exit_val = input("Do you want to Close Transaction..? Y/N : ")
    if exit_val in ('y', 'Y', 'yes', 'YES'):
        os.system("cls")
        print('\n')
        text_Delay("* "*33,0.01)
        text_Delay("\n\t(:...THANK YOU FOR CHOOSING OUR SERVICE...:)\n\n", 0.02)
        text_Delay("* "*33, 0.01)
        print()
        exit()
    else:
        os.system("cls")
        counter_for_first_run = False
        user_Main_menu()
        user_Option()

# loading_System()
first_Run_New_User_Table()
user_Main_menu()
user_Option()
# conn.commit()
# conn.close()
# create_New_account()