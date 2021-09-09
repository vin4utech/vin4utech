from import_methods import *

global conn, cursor
db = 'ATM_Database.db'
conn = sqlite3.connect('./ATM_Database.db')
cursor = conn.cursor()

def single_User_Ac():
    global user_ac, user_ac_details
    cursor.execute(f"SELECT MAX(Sr_No), AC_No FROM New_User_Details")
    user_ac_details = cursor.fetchall()
    for user_ac in user_ac_details:
        pass

def temp_Ac_No(acc_no):
    global user_acc_no
    user_acc_no = acc_no

def temp_transfer_ac_no(from_no):
    global from_ac_no
    from_ac_no = from_no
    
'''******************************************************************************'''
#This is for To Create Table for Admin Login Table....
def create_Tables():
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE Admin_Login_{user_ac[1]}(Sr_No int NOT NULL, 
            User_Name char(50) NOT NULL, 
            Password char(50) NOT NULL);''')
# create_Tables()

#This is for Insert Record in Admin Login 
def insert_Record():
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Admin_Login(Sr_No, User_Name, Password) VALUES (1, 'vin4u', 12345)''')
    cursor.execute('''INSERT INTO Admin_Login(Sr_No, User_Name, Password) VALUES (2, 'ankudi', 12345)''')
    cursor.execute('''INSERT INTO Admin_Login(Sr_No, User_Name, Password) VALUES (3, 'admin', 'admin')''')
    cursor.execute('''INSERT INTO Admin_Login(Sr_No, User_Name, Password) VALUES (4, 'administrator', 'administrator')''')
    cursor.execute('''INSERT INTO Admin_Login(Sr_No, User_Name, Password) VALUES (5, 'a', 'a')''')
    conn.commit()
# insert_Record()    

#This is for Delete Record from Admin Login 
def delete_Record():
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM Admin_Login WHERE Sr_No = 1''')  

    print('Record Deleted...!')
# delete_Record()

#THis is for To Update Record from Admin Login Table
def update_Record():
    cursor = conn.cursor()
    cursor.execute('''UPDATE New_User_Details SET Mob_No = 3322 WHERE Sr_No = 3''')
    conn.commit()
    print('Record Updated...!')
# update_Record()

#THis is for TO SHow All Admin Users in Tabular format....
def table_Format():
    cursor = conn.cursor()
    select = cursor.execute('''SELECT * FROM Admin_Login''')  
    table = prettytable.PrettyTable(['Sr.No', 'User Name', 'Password'])
    for record in select:
        table.add_row(record)
    print(table)
# table_Format()

'''******************************************************************************'''
#This is for To Create Depost Table.....
def create_Deposit_Table():
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE Deposit_Money_{user_ac[1]}(
                Sr_No INT, 
                Acc_Transaction_Dep CHAR(100) NOT NULL,
                Date DATETIME NOT NULL, 
                Debit FLOAT NOT NULL, 
                Credit FLOAT NOT NULL, 
                Balance FLOAT NOT NULL)''')
    cursor.execute(f'''INSERT INTO Deposit_Money_{user_ac[1]}(
            Sr_No, Acc_Transaction_Dep, Date, Debit, Credit, Balance) 
            VALUES (1, 'DEPAC000001', datetime('now', 'localtime'), '-', 0, 0)''')
    conn.commit()
# create_Deposit_Table()

#This is for Deposit Record in Deposit Money Table 
def insert_Deposit_Record(deposit_amt, fixed_Amt):
    single_User_Ac()
    cursor = conn.cursor()
    start_Num = cursor.execute(f"SELECT MAX(Sr_No) FROM Deposit_Money_{user_acc_no}")
    leading_Zero = 6
    initial_Dep = 'DEPAC'
    Tran_Code = 'DEP'
    for i in start_Num:
        i = i[0] + 1
        auto = str(int(i)).zfill(leading_Zero)

    cursor.execute(f'''INSERT INTO Deposit_Money_{user_acc_no}(
        Sr_No, Acc_Transaction_Dep, Date, Debit, Credit, Balance) 
        VALUES (? , ? , datetime('now', 'localtime'), ? , ? , ? )''',(i , initial_Dep + auto, '-' , deposit_amt, fixed_Amt))
    cursor.execute(f'''INSERT INTO Mini_Statement_{user_acc_no}(
        Acc_Transaction, Tr_Code, Date, Debit, Credit, Balance) 
        VALUES (? , ? ,datetime('now', 'localtime'), ? , ? , ? )''',(initial_Dep + auto, Tran_Code,'-',deposit_amt, fixed_Amt))
    conn.commit()
    print('Successful Deposited...')
# insert_Deposit_Record(50,1000)

def table_Format_Deposit_Money():
    cursor = conn.cursor()
    select = cursor.execute(f"SELECT Sr_No, Acc_Transaction_Dep, Date, Debit, Credit, Balance FROM Deposit_Money_{user_acc_no}")
    table = prettytable.PrettyTable()
    table.field_names = ['Sr_No', 'Acc_Transaction_Dep', 'Date', 'Debit', 'Credit', 'Balance']
    table.title = ' DEPOSIT MONEY ' 
    table._max_width = {'Sr_No' : 3, 'Acc_Transaction_Dep' : 15, 'Date' : 11}
    table._align['Debit'] = 'r'
    table._align['Credit'] = 'r'
    table._align['Balance'] = 'r'
    for record in select:
        table.add_row(record)
    print(table)
# table_Format_Deposit_Money()

'''******************************************************************************'''
#This is for For To Create Withdraw Table...
def create_Withdraw_Table():
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE Withdraw_Money_{user_ac[1]}(
                Sr_No INT, 
                Acc_Transaction_With CHAR(100) NOT NULL,
                Date DATETIME NOT NULL, 
                Debit FLOAT NOT NULL, 
                Credit FLOAT NOT NULL, 
                Balance FLOAT NOT NULL)''')
    cursor.execute(f'''INSERT INTO Withdraw_Money_{user_ac[1]}(
            Sr_No, Acc_Transaction_With, Date, Debit, Credit, Balance) 
            VALUES (1, 'WTHAC000001', datetime('now', 'localtime'), 0, '-', 0)''')
    conn.commit()
# create_Withdraw_Table()

#This is for Insert Withdraw Record in Table...
def insert_Withdraw_Record(withdraw_amt, fixed_Amt):
    single_User_Ac()
    cursor = conn.cursor()
    start_Num = cursor.execute(f"SELECT MAX(Sr_No) FROM Withdraw_Money_{user_acc_no}")
    leading_Zero = 6
    initial_Wth = 'WTHAC'
    Tran_Code = 'WTH'
    for i in start_Num:
        i = i[0] + 1
        auto = str(int(i)).zfill(leading_Zero)

    cursor.execute(f'''INSERT INTO Withdraw_Money_{user_acc_no}(
            Sr_No, Acc_Transaction_With, Date, Debit, Credit, Balance)
            VALUES (? , ? , datetime('now', 'localtime'), ? , ? , ?)''',(i, initial_Wth + auto, withdraw_amt, '-' , fixed_Amt))
    cursor.execute(f'''INSERT INTO Mini_Statement_{user_acc_no}(
            Acc_Transaction, Tr_Code, Date, Debit, Credit, Balance)
            VALUES (? , ? , datetime('now', 'localtime'), ? , ? , ?)''',(initial_Wth + auto, Tran_Code, withdraw_amt, '-' , fixed_Amt))
    conn.commit()        
    print('Successful Withdraw...')
# insert_Withdraw_Record()

def table_Format_Withdraw_Money():
    cursor = conn.cursor()
    select = cursor.execute(f"SELECT Sr_No, Acc_Transaction_With, Date, Debit, Credit, Balance FROM Withdraw_Money_{user_acc_no}")
    table = prettytable.PrettyTable()
    table.field_names = ['Sr_No', 'Acc_Transaction_With', 'Date', 'Debit', 'Credit', 'Balance']
    table.title = ' WITHDRAW MONEY ' 
    table._max_width = {'Sr_No' : 3, 'Acc_Transaction_With' : 15, 'Date' : 11}
    table._align['Debit'] = 'r'
    table._align['Credit'] = 'r'
    table._align['Balance'] = 'r'
    for record in select:
        table.add_row(record)
    print(table)
# table_Format_Withdraw_Money()

'''******************************************************************************'''
#This is for To Create Fast cash Money Table....
def create_Table_Fast_Cash_Money():
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE Fast_Cash_Money_{user_ac[1]}(
                Sr_No INT, 
                Acc_Transaction_Fst CHAR(100) NOT NULL,
                Date DATETIME NOT NULL, 
                Debit FLOAT NOT NULL, 
                Credit FLOAT NOT NULL, 
                Balance FLOAT NOT NULL)''')
    cursor.execute(f'''INSERT INTO Fast_Cash_Money_{user_ac[1]}(
            Sr_No, Acc_Transaction_Fst, Date, Debit, Credit, Balance) 
            VALUES (1, 'FSTAC000001', datetime('now', 'localtime'), 0, '-', 0)''')
    conn.commit()
# create_Table_Fast_Cash_Money()

#This is for Insert Withdraw Record in Table...
def insert_Fast_Cash_Record(withdraw_amt, fixed_Amt):
    single_User_Ac()
    cursor = conn.cursor()
    start_Num = cursor.execute(f"SELECT MAX(Sr_No) FROM Fast_Cash_Money_{user_acc_no}")
    leading_Zero = 6
    initial_Wth = 'FSTAC'
    Tran_Code = 'FST'
    for i in start_Num:
        i = i[0] + 1
        auto = str(int(i)).zfill(leading_Zero)

    cursor.execute(f'''INSERT INTO Fast_Cash_Money_{user_acc_no}(
            Sr_No, Acc_Transaction_Fst, Date, Debit, Credit, Balance)
            VALUES (? , ? , datetime('now', 'localtime'), ? , ? , ?)''',(i, initial_Wth + auto, withdraw_amt, '-' , fixed_Amt))
    cursor.execute(f'''INSERT INTO Mini_Statement_{user_acc_no}(
            Acc_Transaction, Tr_Code, Date, Debit, Credit, Balance)
            VALUES (? , ? , datetime('now', 'localtime'), ? , ? , ?)''',(initial_Wth + auto, Tran_Code, withdraw_amt, '-' , fixed_Amt))
    conn.commit()        
    print('Successful Withdraw...')
# insert_Fast_Cash_Record()

def table_Format_Fast_Cash_Money():
    cursor = conn.cursor()
    select = cursor.execute(f"SELECT Sr_No, Acc_Transaction_Fst, Date, Debit, Credit, Balance FROM Fast_Cash_Money_{user_acc_no}")
    table = prettytable.PrettyTable()
    table.field_names = ['Sr_No', 'Acc_Transaction_With', 'Date', 'Debit', 'Credit', 'Balance']
    # table.title = '  ' 
    table._max_width = {'Sr_No' : 3, 'Acc_Transaction_With' : 15, 'Date' : 11}
    table._align['Debit'] = 'r'
    table._align['Credit'] = 'r'
    table._align['Balance'] = 'r'
    for record in select:
        table.add_row(record)
    print(table)
# table_Format_Fast_Cash_Money()

'''******************************************************************************'''

def create_Table_Transfer_Money():
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE Transfer_Money_{user_ac[1]}(
                Sr_No INT, 
                Acc_Transaction_Trf CHAR(100) NOT NULL,
                Date DATETIME NOT NULL, 
                Debit FLOAT NOT NULL, 
                Credit FLOAT NOT NULL, 
                Balance FLOAT NOT NULL)''')
    cursor.execute(f'''INSERT INTO Transfer_Money_{user_ac[1]}(
            Sr_No, Acc_Transaction_Trf, Date, Debit, Credit, Balance) 
            VALUES (1, 'TRFTO000001', datetime('now', 'localtime'), 0, 0, 0)''')
    conn.commit()

def insert_Transfer_To_Record(transfer_Amt, fixed_Amt):
    single_User_Ac()
    cursor = conn.cursor()
    start_Num = cursor.execute(f"SELECT MAX(Sr_No) FROM Transfer_Money_{user_acc_no}")
    leading_Zero = 6
    initial_Wth = 'TRFTO'
    Tran_Code = 'TRTO'
    for i in start_Num:
        i = i[0] + 1
        auto = str(int(i)).zfill(leading_Zero)
    cursor.execute(f'''INSERT INTO Transfer_Money_{user_acc_no}(
            Sr_No, Acc_Transaction_Trf, Date, Debit, Credit, Balance)
            VALUES (? , ? , datetime('now', 'localtime'), ? , ? , ?)''',(i, initial_Wth + auto, transfer_Amt, '-' , fixed_Amt))
    cursor.execute(f'''INSERT INTO Mini_Statement_{user_acc_no}(
            Acc_Transaction, Tr_Code, Date, Debit, Credit, Balance)
            VALUES (? , ? , datetime('now', 'localtime'), ? , ? , ?)''',(initial_Wth + auto, Tran_Code, transfer_Amt, '-' , fixed_Amt))
    conn.commit()      
    
    
def insert_Transfer_From_Record(transfer_Amt):
    single_User_Ac()
    cursor = conn.cursor()
    start_Num = cursor.execute(f"SELECT MAX(Sr_No) FROM Transfer_Money_{from_ac_no}")
    leading_Zero = 6
    initial_Wth = 'TRFROM'
    Tran_Code = 'TRFR'
    for i in start_Num:
        i = i[0] + 1
        auto = str(int(i)).zfill(leading_Zero)
    user_Bal = cursor.execute(f"SELECT MAX(Sr_No), Balance FROM Mini_Statement_{from_ac_no}")
    for bal in user_Bal:
        pass
    cur_Trf_bal = bal[1]
    cur_Trf_bal = cur_Trf_bal + transfer_Amt
    cursor.execute(f'''INSERT INTO Transfer_Money_{from_ac_no}(Sr_No, Acc_Transaction_Trf, Date, Debit, Credit, Balance)
            VALUES (? , ? , datetime('now', 'localtime'), ? , ? , ?)''',(i, initial_Wth + auto, '-' ,transfer_Amt, cur_Trf_bal))
    cursor.execute(f'''INSERT INTO Mini_Statement_{from_ac_no}(
            Acc_Transaction, Tr_Code, Date, Debit, Credit, Balance)
            VALUES (? , ? , datetime('now', 'localtime'), ? , ? , ?)''',(initial_Wth + auto, Tran_Code, '-' , transfer_Amt, cur_Trf_bal))
    conn.commit()
    print('Successful Transfer Money...')

'''******************************************************************************'''
#This is for To Create Mini Statement Table....
def create_Table_Mini_Statement():
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE Mini_Statement_{user_ac[1]}(
                Sr_No INTEGER PRIMARY KEY AUTOINCREMENT, 
                Acc_Transaction CHAR(100) NOT NULL,
                Tr_Code CHAR(20) NOT NULL,
                Date DATETIME NOT NULL, 
                Debit FLOAT NOT NULL, 
                Credit FLOAT NOT NULL, 
                Balance FLOAT NOT NULL)''')
    cursor.execute(f'''INSERT INTO Mini_Statement_{user_ac[1]}(
            Acc_Transaction, Tr_Code, Date, Debit, Credit, Balance) 
            VALUES ('MINI-STATE','MINI',datetime('now', 'localtime'),'0','0','0')''')
    conn.commit()
# create_Table_Mini_Statement()

#This is for Insert Record in MINI STATEMENT TABLE.....
def insert_Record_Mini_Statement():
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO Mini_Statement_{user_ac[1]}(Acc_Transaction, Tr_Code, Date, Debit, Credit, Balance) VALUES('MINI-STAT', 'MINI', datetime('now'), 0, 0, 0);")
    conn.commit()
    print('Record Inserted into MINI STATEMENT...!')
# insert_Record_Mini_Statement()

def delete_Record_Mini_Statement():
    cursor = conn.cursor()
    cursor.execute(f'''DELETE FROM Mini_Statement_{user_ac[1]} WHERE Sr_No = 3''')  
    conn.commit()
    print('Record Deleted...!')
# delete_Record_Mini_Statement()


#This is for MINI STATEMENT Tabular format.....
def table_Format_Mini_Statement():
    single_User_Ac()
    cursor = conn.cursor()
    select = cursor.execute(f"SELECT * FROM Mini_Statement_{user_acc_no}")
    table = prettytable.PrettyTable()
    print('+','-'*74,'+','\n|',' '*28,' MINI-STATEMENT ',' '*28,'|')
    print('|',' '*74,'|','\n|',' '*18,' From Date 01-01-2021 To 31-01-2021 ',' '*18,'|')
    table.field_names = ['Sr_No', 'Acc_Transaction', 'TR-CODE', 'Date', 'Debit', 'Credit', 'Balance']
    # table.title = '  ' 
    table._max_width = {'Sr_No' : 4, 'Acc_Transaction' : 15, 'Date' : 11}
    table._align['Debit'] = 'r'
    table._align['Credit'] = 'r'
    table._align['Balance'] = 'r'
    for record in select:
        table.add_row(record)
    print(table)
# table_Format_Mini_Statement()

'''******************************************************************************'''

def create_Table_New_AC():
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE New_User_Details(
                Sr_No INT, 
                AC_No CHAR(100) NOT NULL,
                Date DATETIME NOT NULL, 
                First_Name CHAR(20) NOT NULL,
                Middle_Name CHAR(20) NOT NULL,
                Last_Name CHAR(20) NOT NULL,
                Gender CHAR(10) NOT NULL,
                Marital_Status CHAR(15) NOT NULL,
                Address CHAR(150) NOT NULL,
                City_Villege CHAR(50) NOT NULL,
                Taluka CHAR(50) NOT NULL,
                District CHAR(50) NOT NULL,
                State CHAR(50) NOT NULL,
                Mob_No INT,
                Adhar_Card INT,
                PAN_Card CHAR(15) NOT NULL,
                Confirmation CHAR(20) NOT NULL)''')
    cursor.execute('''INSERT INTO New_User_Details(
            Sr_No, AC_No, Date, First_Name, Middle_Name, Last_Name, Gender, Marital_Status,
            Address, City_Villege, Taluka, District, State, Mob_No, 
            Adhar_Card, PAN_Card, Confirmation) 
                VALUES (1, 'AVNI00000001', datetime('now', 'localtime'), 'Vinayak', 'Kishor', 'Kumbhar', 
                'Male', 'Maried', 'Rui Phata', 'Ichalkaranji', 'Hatkanangale', 'Kolhapur', 'Maha', 
                7972690248, 735317754486, 'FIAPK4416F', 'Yes')''')
    conn.commit()
# create_Table_New_AC()

def insert_Record_New_AC(first_Name, middle_name, last_name, gender, status, user_Address, user_City, user_Tal, user_Dist, user_State, mob_No, adhar_No, pan_No, confirmation):
    cursor = conn.cursor()
    start_Num = cursor.execute('SELECT MAX(Sr_No) FROM New_User_Details')
    leading_Zero = 8
    initial_AC = 'AVNI'
    Tran_Code = 'AVB'
    for i in start_Num:
        i = i[0] + 1
        auto = str(int(i)).zfill(leading_Zero)

    cursor.execute('''INSERT INTO New_User_Details(
            Sr_No, AC_No, Date, First_Name, Middle_Name, Last_Name, Gender, 
            Marital_Status, Address, City_Villege, Taluka, District, State, 
            Mob_No, Adhar_Card, PAN_Card, Confirmation) 
                VALUES (?, ?, datetime('now', 'localtime'), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                (i, initial_AC + auto, first_Name, middle_name, last_name, 
                gender, status, user_Address, user_City, user_Tal, user_Dist, 
                user_State, mob_No, adhar_No, pan_No, confirmation))
    conn.commit()

'''******************************************************************************'''
def create_Table_User_Login():
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE New_User_Login(Sr_No INT, 
                AC_No CHAR(100) NOT NULL,
                Date DATETIME NOT NULL, 
                User_Name CHAR(50) NOT NULL,
                Password CHAR(50) NOT NULL)''')
    cursor.execute('''INSERT INTO New_User_Login(Sr_No, AC_No, Date, User_Name, Password)
        VALUES (1, 'AVNI00000001', datetime('now', 'localtime'), 'vin4u', 12345)''')
    conn.commit()

def insert_Record_User_Login(new_User_name, Confirm_pass):
    cursor = conn.cursor()
    Ac_No_User_Login = cursor.execute('SELECT MAX(Sr_No) FROM New_User_Login')
    leading_Zero = 8
    initial_AC = 'AVNI'
    Tran_Code = 'AVB'
    for i in Ac_No_User_Login:
        i = i[0] + 1
        auto = str(int(i)).zfill(leading_Zero)

    cursor.execute('''INSERT INTO New_User_Login(Sr_No, AC_No, Date, User_Name, Password) 
                VALUES (?, ?, datetime('now', 'localtime'), ?, ?)''', 
                (i, initial_AC + auto, new_User_name, Confirm_pass))
    conn.commit()


#First time Create Database Tables for all Options......
def first_Run_Table():
    single_User_Ac()
    cursor = conn.cursor()
    # Admn_Tbl = cursor.execute("SELECT NAME FROM sqlite_master WHERE type = 'table' AND NAME = 'Admin_Login'").fetchall()
    Deps_Tbl = cursor.execute(f"SELECT NAME FROM sqlite_master WHERE type = 'table' AND NAME = 'Deposit_Money_{user_ac[1]}'").fetchall()
    With_Tbl = cursor.execute(f"SELECT NAME FROM sqlite_master WHERE type = 'table' AND NAME = 'Withdraw_Money_{user_ac[1]}'").fetchall()
    Fast_Tbl = cursor.execute(f"SELECT NAME FROM sqlite_master WHERE type = 'table' AND NAME = 'Fast_Cash_Money_{user_ac[1]}'").fetchall()
    Mini_Tbl = cursor.execute(f"SELECT NAME FROM sqlite_master WHERE type = 'table' AND NAME = 'Mini_Statement_{user_ac[1]}'").fetchall()
    trnf_Tbl = cursor.execute(f"SELECT NAME FROM sqlite_master WHERE type = 'table' AND NAME = 'Transfer_Money_{user_ac[1]}'").fetchall()
    # if Admn_Tbl == []:
    #     create_Tables()
    #     insert_Record()
    if Deps_Tbl == []:
        create_Deposit_Table()
    if With_Tbl == []:
        create_Withdraw_Table()
    if Fast_Tbl == []:
        create_Table_Fast_Cash_Money()
    if Mini_Tbl == []:
        create_Table_Mini_Statement()
    if trnf_Tbl == []:
        create_Table_Transfer_Money()
    else:
        pass

def first_Run_New_User_Table():
    New_Usr_Tbl = cursor.execute("SELECT NAME FROM sqlite_master WHERE type = 'table' AND NAME = 'New_User_Details'").fetchall()
    Login_Tbl = cursor.execute("SELECT NAME FROM sqlite_master WHERE type = 'table' AND NAME = 'New_User_Login'").fetchall()
    if New_Usr_Tbl ==[]:
        create_Table_New_AC()
    if Login_Tbl == []:
        create_Table_User_Login()
    else:
        pass
    first_Run_Table()

# single_User_Ac()