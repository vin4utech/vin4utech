from import_methods import *
from ATM_Database import *
from Export_Report import *

global time_sec
counter_for_first_run = True
time_sec = 0.02
def temp_cur_Bal(curr_bal):
    global balance
    balance = curr_bal

def current_Balance():
    global cur, fixed_Amt
    # cursor.execute(f"SELECT MAX(Sr_No), AC_No FROM New_User_Details")
    # user_ac_details = cursor.fetchall()
    # for user_ac in user_ac_details:
    #     pass
    curr_Bal = cursor.execute(f"SELECT MAX(Sr_No), Balance FROM Mini_Statement_{balance}")
    for cur in curr_Bal:
        pass
    fixed_Amt = cur[1]

# This part is for Text Delay in all functions and menus using Function
def text_Delay(main_Menu_Text, time):
    for characters in main_Menu_Text:
        print(characters, end='')        
        sys.stdout.flush()
        sleep(time)
    main_Menu_items = ("\t1. Deopsit", "\t2. Cash Withdraw", "\t3. Fast Cash", "\t4. Balance Enquiry", "\t5. Transfer", "\t6. Mini Statement", "\t7. Profile", "\t8. Exit")
    if main_Menu_Text == '\r':
        for char in main_Menu_items:
            print(char, "")
            sleep(time)

# This part is for Main Menu using Function
def main_Menu():    
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

# This part is for Main Menu Options Selection using Function
def main_Menu_selection():
    text_Delay('\r', 0.05)
    while True:
        try:
            opt = int(input("Select Above Option : "))
            if opt == 1:
                print()
                deposit_money()
            elif opt == 2:
                print()
                cash_Withdraw_money()
            elif opt == 3:
                print()
                fast_Cash_money()
            elif opt == 4:
                print()
                balance_Enquiry_money()
            elif opt == 5:
                print()
                transfer_Money()
            elif opt == 6:
                print()
                mini_Statement_Balance()
            elif opt == 7:
                print(".......Under Development.......")
                pass
            elif opt == 8:
                print()
                exit_Menu()
            else:
                text_Delay("\nThe Option You are Entered is Not Available in Our ATM SERVICE...!\n", 0.01)
                print()
                text_Delay("Sorry, Your are entered Wrong Choice, Please Try Again...",0.01)
                print("\n")
                continue
            break
        except ValueError:
            print("\n\tYou are Entered Wrong Characters...!\n\tPlese Enter Right Given Number...\n")
            continue

# This part is for Deposite Money using function
def deposit_money():
    current_Balance()
    global fixed_Amt
    while True:
        while True:
            try:
                deposit_amt = int(input("Enter Amount to Deposit in Your Account : "))
                break
            except ValueError:
                print("\n\tYou are Entered Wrong Characters...!\n\tPlese Enter Right Given Number...\n")
                continue
        print("Your are entered ", deposit_amt, "\n\nIs this correct amount...? Y/N : ", end="")
        correct_amt = input()
        if correct_amt in ('y', 'Y', 'yes', 'YES'):
            fixed_Amt = fixed_Amt + deposit_amt
            text_Delay("\n\tYour Total Deposited Amount is ", time_sec)
            text_Delay(str(int(fixed_Amt)), time_sec)
            print('\n')
            insert_Deposit_Record(deposit_amt, fixed_Amt)
            continue_Transaction()        

# This part is for Withdraw Cash using function
def cash_Withdraw_money():
    current_Balance()
    global fixed_Amt
    while True:
        while True:
            try:
                withdraw_amt = int(input("Enter Withdraw Amount : "))
                break
            except ValueError:
                print("\n\tYou are Entered Wrong Characters...!\n\tPlese Enter Right Given Number...\n")
                continue
        print("Your are entered", withdraw_amt, "withdraw amount..\n\nIs this correct amount...? Y/N : ", end="")
        correct_amt = input()
        if withdraw_amt > fixed_Amt:
            print("Insufficient Balance...:( In your account..!")
        elif correct_amt in ('y', 'Y', 'yes', 'YES'):
            fixed_Amt = fixed_Amt - withdraw_amt
            insert_Withdraw_Record(withdraw_amt, fixed_Amt)
            Successful_withdraw()
            continue_Transaction()

# This part is for fast cash Withdraw Cash using function
def fast_Cash_money():
    current_Balance()
    global fixed_Amt
    # os.system('setterm -cursor off')
    fixed_cash = [100, 500, 1000, 2000, 5000, 'Cancel']
    while True:
        # print("Select Fast Cash Withdraw Amount : \n\t1. {}\t\t4. {}\n\t2. {}\t\t5. {}\n\t3. {}\t\t6. {} \nSelect Option :".format(fixed_cash[0], fixed_cash[3], fixed_cash[1],fixed_cash[4], fixed_cash[2], fixed_cash[5]), end="")
        print("Select Fast Cash Withdraw Amount : ")
        text_Delay("\n\t1. 100\t\t4. 2000\n\t2. 500\t\t5. 5000\n\t3. 1000\t\t6. Cancel",time_sec)
        print("\nSelect Option :", end="")
        while True:
            try:
                withdraw_amt = int(input())
                break
            except ValueError:
                print("\n\tYou are Entered Wrong Characters...!\n\tPlese Enter Right Given Number...\n")
                continue
        print("Your are Selected", fixed_cash[withdraw_amt-1], "for withdraw amount..\n")
        if fixed_cash[withdraw_amt-1] == 100 < fixed_Amt:
            fixed_Amt = fixed_Amt - 100
            insert_Fast_Cash_Record(100, fixed_Amt)
            Successful_withdraw()
            continue_Transaction()
        elif fixed_cash[withdraw_amt-1] == 500 < fixed_Amt:
            fixed_Amt = fixed_Amt - 500
            insert_Fast_Cash_Record(500, fixed_Amt)
            Successful_withdraw()
            continue_Transaction()
        elif fixed_cash[withdraw_amt-1] == 1000 < fixed_Amt:
            fixed_Amt = fixed_Amt - 1000
            insert_Fast_Cash_Record(1000, fixed_Amt)
            Successful_withdraw()           
            continue_Transaction()
        elif fixed_cash[withdraw_amt-1] == 2000 < fixed_Amt:
            fixed_Amt = fixed_Amt - 2000
            insert_Fast_Cash_Record(2000, fixed_Amt)
            Successful_withdraw()
            continue_Transaction()
        elif fixed_cash[withdraw_amt-1] == 5000 < fixed_Amt:
            fixed_Amt = fixed_Amt - 5000
            insert_Fast_Cash_Record(5000, fixed_Amt)
            Successful_withdraw()
            continue_Transaction()
        elif fixed_cash[withdraw_amt-1] == 'Cancel':
            text_Delay("\tYou are Canceled this Process....!", time_sec)
            print("\n")
            continue_Transaction()
        else:
            text_Delay("\tYour Total Balance is ", time_sec)
            print(end="")
            text_Delay(str(int(fixed_Amt)), 0.03)
            print("\n\nInsufficient Balance...:( In your account..!")
            continue_Transaction()

# This part is for Balance Enquiry money using function
def balance_Enquiry_money():
    current_Balance()
    global fixed_Amt
    text_Delay("\n\tYour Current Balance is ", time_sec)
    text_Delay(str(int(fixed_Amt)), time_sec)
    print("\n")
    continue_Transaction()

# This part is for Balance Enquiry money using function
def transfer_Money():
    current_Balance()
    global fixed_Amt
    while True:
        try:
            text_Delay("1) Mobile Transfer \t2) Account Transfer : ", time_sec)
            get_Acc_Opt = int(input())
            break
        except ValueError:
            print("\n\tYou are Entered Wrong Characters...!\n\tPlese Enter Right Given Number...\n")
            continue
    if get_Acc_Opt == 1:
        while True:
            get_acc_mob_no = input("Enter Mobile No. : ")
            print()
            cursor.execute(f"SELECT AC_No, Mob_No, First_Name, Middle_Name, Last_Name FROM New_User_Details WHERE Mob_No = {get_acc_mob_no}")
            select_user_mob_no = cursor.fetchall()
            for row in select_user_mob_no:
                pass
            if select_user_mob_no:
                print(f"Account Available to given Mob No. {get_acc_mob_no} \n")
                while True:
                    try:
                        transfer_amt = int(input("Enter Amount to Transfer : "))
                        break
                    except ValueError:
                        print("\n\tYou are Entered Wrong Characters...!\n\tPlese Enter Right Given Number...\n")
                        continue
                print("Your are entered", transfer_amt, "Transfer amount..\n\nIs this correct amount...? Y/N : ", end="")
                correct_amt = input()
                if transfer_amt > fixed_Amt:
                    print("Insufficient Balance...:( In your account..!")
                elif correct_amt in ('y', 'Y', 'yes', 'YES'):
                    temp_transfer_ac_no(row[0])
                    fixed_Amt = fixed_Amt - transfer_amt
                    insert_Transfer_To_Record(transfer_amt, fixed_Amt)
                    insert_Transfer_From_Record(transfer_amt)
                    print('\n\t')
                    text_Delay("Money Has Been Transfered to ", 0.02)
                    text_Delay(f"Mr/Mrs. {row[2]} {row[3]} {row[4]}", 0.02)
                    print()
                    continue_Transaction()
                break
            else:
                print('Please Check Entered Mobile No. is linked to Bank Account or Not.')
                continue


    elif get_Acc_Opt == 2:
        while True:
            get_acc_mob_no = input("Enter Account No. : ")
            print()
            cursor.execute(f"SELECT AC_No, Mob_No, First_Name, Middle_Name, Last_Name FROM New_User_Details WHERE AC_No = '{get_acc_mob_no}'")
            select_user_ac_no = cursor.fetchall()
            for row in select_user_ac_no:
                pass
            if select_user_ac_no:
                print(f"Account Available to given Account No. {get_acc_mob_no} \n")
                while True:
                    try:
                        transfer_amt = int(input("Enter Amount to Transfer : "))
                        break
                    except ValueError:
                        print("\n\tYou are Entered Wrong Characters...!\n\tPlese Enter Right Given Number...\n")
                        continue
                print("Your are entered", transfer_amt, "Transfer amount..\n\nIs this correct amount...? Y/N : ", end="")
                correct_amt = input()
                if transfer_amt > fixed_Amt:
                    print("Insufficient Balance...:( In your account..!")
                elif correct_amt in ('y', 'Y', 'yes', 'YES'):
                    temp_transfer_ac_no(row[0])
                    fixed_Amt = fixed_Amt - transfer_amt
                    insert_Transfer_To_Record(transfer_amt, fixed_Amt)
                    insert_Transfer_From_Record(transfer_amt)
                    print('\n\t')
                    text_Delay("Money Has Been Transfered to ", 0.02)
                    text_Delay(f"Mr/Mrs. {row[2]} {row[3]} {row[4]}", 0.02)
                    print()
                    continue_Transaction()
                break
            else:
                print('Please Check Entered Account No. is Correct or Not.')
                continue
# transfer_Money()
# This part is for Successful Withdraw Cash using function
def Successful_withdraw():
    current_Balance()
    global fixed_Amt
    text_Delay("\n\tWithdraw Successfully..:)\n",0.01)
    text_Delay("\tYour Total Deposited Balance is ", time_sec)
    text_Delay(str(int(fixed_Amt)), time_sec)
    print("\n")

# This part is for Mini Statement Balance Menu using function
def mini_Statement_Balance():
    os.system("cls")
    # main_Menu()
    table_Format_Mini_Statement()
    print()
    continue_Transaction()

# This part is for Continue Transaction Menu using function
def continue_Transaction():
    global counter_for_first_run
    continue_Menu = input("Do you want to Continue Transaction..? Y/N : ")
    while True:
        if continue_Menu in ('y', 'Y', 'yes', 'YES'):
            counter_for_first_run = True
            os.system("cls")
            main_Menu()
            main_Menu_selection()
        else:
            exit_Menu()

# This part is for Exit or Close Menu using function
def exit_Menu():
    global counter_for_first_run
    exit_val = input("Do you want to Close Transaction..? Y/N : ")
    if exit_val in ('y', 'Y', 'yes', 'YES'):
        os.system("cls")
        print('\n')
        text_Delay("* "*33,0.01)
        text_Delay("\n\n\t(:...THANK YOU FOR CHOOSING OUR SERVICE...:)\n\n", 0.02)
        text_Delay("* "*33, 0.01)
        print('\n')
        time.sleep(0.5)
        exit()
    else:
        os.system("cls")
        counter_for_first_run = False
        main_Menu()
        main_Menu_selection()

# main_Menu()
# main_Menu_selection()