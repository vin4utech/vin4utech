from Main_Menu import text_Delay, main_Menu, main_Menu_selection, temp_cur_Bal
from ATM_Database import *
from import_methods import *
from Loading_System import *
special_Symbols = ["!", "@", "#", "$", "%", "&"]
time_sec = 0.03

def user_Validation():
    global new_User_name
    while True:
        text_Delay("New User Name \t\t: \t", time_sec)
        new_User_name = input()
        cursor = conn.cursor()
        cursor.execute(f"SELECT User_Name FROM New_User_Login WHERE User_Name = '{new_User_name}'")
        if not cursor.fetchone():
            print(f'\t--> {new_User_name} User Name is Available..\n\t--> Now You can Set New Password....!\n')
            break
        else:
            print(f'\t--> {new_User_name} User Name is Not Available..\n\t--> Please Enter Other User Name....!\n')
            continue

def password_Validation():
    global condition, special_Symbols, Enter_pass
    condition = True
    text_Delay("Set New Password \t: \t", time_sec)
    Enter_pass = input()
    if len(Enter_pass) < 4:
        print("Password Should be Greater than 4 digits.")
        condition = False
    
    if len(Enter_pass) > 10:
        print("Password Should be Less than 10 digits.")
        condition = False
    
    if not any(char.isdigit() for char in Enter_pass):
        print("Password Should have at Least One Digit.")
        condition = False
    
    if not any(char.isupper() for char in Enter_pass):
        print("Password Should have at Least One Uppercase.")
        condition = False
    
    if not any(char.islower() for char in Enter_pass):
        print("Password Should have at Least One Lowercase.")
        condition = False
    
    if not any(char in special_Symbols for char in Enter_pass):
        print("Password Should have at Least One Special Symbols.")
        print("! @ # $ % &")
        condition = False

def password_check():
    global condition, Confirm_pass
    count = 0
    num = 3
    while count < num:
        if count == 0:
            user_Validation()
        password_Validation()
        cursor.execute(f"SELECT MAX(Sr_No), AC_No, first_name, Middle_Name, Last_Name FROM New_User_Details")
        user_all_details = cursor.fetchall()
        for user_name in user_all_details:
            pass
        if condition == True:
            text_Delay("Confirm Password \t: \t", time_sec)
            Confirm_pass = input()
            if Enter_pass == Confirm_pass:
                insert_Record_User_Login(new_User_name, Confirm_pass)
                text_Delay("\n\tPassword Set Successfully.....", 0.02)
                print("\n\tNow You Can Login by Using User Name And Password...")
                time.sleep(2.1)
                os.system('cls')
                loading_System()
                temp_Ac_No(user_name[1])
                temp_cur_Bal(user_name[1])
                main_Menu()
                print(f' ------ > WELCOME MR/MRS. {user_name[2]} {user_name[3]} {user_name[4]} < ------\n')
                main_Menu_selection()                
                break
            else:
                count +=1
                if count != 3:
                    print("\n\tYou are Entered Wrong Confirm Password...!\n\tPlease Try Again...")
                    print(f"\tYou have only {num - count} attempt left\n")
                else:
                    print("\nSorry... You have Excessed Confirm Password Attempts..!")
                    print("Your account has been Blocked for 24 hours...!\n")
        else:
            count +=1
            if count != 3:
                print("\n\tWrong Password...!\n\tPlease Try Again..!") 
                print(f"\tYou have only {num - count} attempt left\n")
            else:
                print("\nSorry... You have Excessed Password Attempts..!")
                print("Your account has been Blocked for 24 hours...!\n")

# password_check()