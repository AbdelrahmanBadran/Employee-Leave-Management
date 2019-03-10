import sys
import os
import time
import datetime
today = datetime.datetime.today()
global data
data = []
global stat
stat = 0

def cls():
    
    print('\nLoading...')
    time.sleep(0.7)
    print('\n' *44)
    
def add_yrleave():

    cls()
    print(today)
    ch = input('''\n(1)Update Yearly Leave Limmit
(2)Go back to your Menu
(3)Logout/Exit ELMS\n
Kindly Enter Choice Number: ''')
    if ch == '1':
        cls()
        with open ('yrleave.txt', 'r') as update:
            limmit = update.read()    
        leave= print('\nCurrent Application Leave Limmit is  -', limmit , '-  days per year')

        limmit = input("\nUpdate Yearly Leave Allowed (days): ")
        
        time.sleep(0.5)
        with open ("yrleave.txt" , "w") as file:
            file.write(limmit)

        print("\n               *YEARLY LEAVE LIMMIT UPDATED SUCCESSFULLY*\n")
        time.sleep(0.25)

        bk = input('\nPress ENTER to Return To Your Main Menu\n')
        HR_UI()
        
    elif ch == '2':
        HR_UI()
        
    elif ch == '3':
        more_options()
        
    else:
        print('\n#Invalid Input#\n')
        time.sleep(0.5)
        add_yrleave()

def add_holiday():
    
    cls()
    print('\n',today)
    ch = input('''\n(1)Add Holiday
(2)Go back to your Menu
(3)Logout/Exit ELMS\n
Kindly Enter Choice Number: ''')
    
    if ch == '1':
        cls()
        print('\n                            ',today)
        print("\n---------------------UPDATE PUBLIC AND UNIVERSITY HOLIDAYS------------------\n")
        
        phd = input("Public Holiday (Day '08'): ")
        phm = input("Public Holiday (Month '07'): ")
        phy = input("Public Holiday (Year '2018'): ")
        uh = input("\nEnter Holiday Details (public/uni): ")
                
        with open("holiday.txt","a") as file:
                file.write("\n" + phd + "/" + phm + "/" + phy + " : " + uh)
        print("\n                     HOLIDAY UPDATED!\n")     
        time.sleep(0.25)
        bk = input('\nPress ENTER to go Back\n')
        add_holiday()
        
    elif ch == '2':
        HR_UI()
        
    elif ch == '3':
        more_options()
        
    else:
        print('\n#Invalid Input#\n')
        time.sleep(0.5)
        add_holiday()

def add_faqs():
    
    cls()
    print('\n',today)
    ch = input('''\n(1)Add FAQS and Leave Policies
(2)Go back to your Menu
(3)Logout/Exit ELMS\n
Kindly Enter Choice Number: ''')
    
    if ch == '1':
        cls()
        print('\n                        ',today)
        print("\n-----------------------UPDATE FAQS AND LEAVE POLICIES---------------------------\n")
        qs = input('Add Question/Policy: ')
        ans = input("Add Answer/Clarification: ")
        
        with open ("faqs.txt" , "a") as file:
            fq = ("Add FAQs : ")
            file.write("\n" + qs + "? " + " : " + ans)
            print("\n                       *UPDATED SUCCESSFULLY*")
        time.sleep(0.5)
        bk = input('\nPress ENTER to go Back\n')
        add_faqs() 

    elif ch == '2':
        HR_UI()
        
    elif ch == '3':
        more_options()
        
    else:
        print('\n#Invalid Input#\n')
        time.sleep(0.5)
        add_faqs()

def read_faqs():
    
        cls()
        with open ("faqs.txt" , "r") as faqs:
            faqs = faqs.read()
        print('\n                   ',today)    
        print('\n     DISPLAYING FREQUENTLY ASKED QUESTIONS AND LEAVE POLICIES')
        print('\n', faqs, '\n')
        back = input('\nPress ENTER To Return\n')


def read_holiday():
    
        cls()
        with open("holiday.txt","r") as holiday:
            holiday = holiday.read()
        print('\n',today)     
        print('\nPUBLIC AND UNIVERSITY HOLIDAYS')
        print('\n', holiday, '\n')
        back = input('\nPress ENTER To Return\n')
        
def search_leave():
        
        cls()
        print('\n                                   ',today) 
        print('\n                                   PENDING LEAVE APPLICATIONS')
        print('\n----------------------------------------------------------------------------------------------------------')
        with open ("leave.txt", "r") as leave:
            leave = leave.readlines()
            for line in leave:
                print(line)       
        print('--------------------------------------------------------------------------------------------------------------')

        app = 0
        nm = input("\nPress Enter To Go Back OR\nSearch Applications by User ID: ")
        
        if nm == '':
            leader_UI()
            
        else:
            lv = open('leave.txt')
        
            for line in lv:
                    if line.startswith(nm):
                        line = line.strip()
                        app = 1

                        if 'pending...' in line:
                            print('\nFound pending Application For  -', nm, '-  Here\n')
                            print(line)
                            app == 1
                            arl(nm)
      
                        else:
                            print('\n No pending Applications for  -', nm,'-')
                            app = 1
                            time.sleep(0.5)
                            arl_options()
                    
            if app == 0 :
                    print('\n            -',nm ,'-  did not apply for leave')
                    time.sleep(0.5)
                    arl_options()
        
def arl(nm):
    
    lv = input('''\n(1)APPROVE LEAVE\n(2)REJECT LEAVE
(3)More Options/Exit ELMS\n
Enter Choice Number: ''')
         
    if(lv == '1'):
        days = input('\nAmount of days Approving: ')
        app_rej(nm, days, "Approved")
        time.sleep(0.30)
        print("\n                      *Leave Approved*")
        time.sleep(0.5)
        cls()
        arl_options()
        
    elif(lv == '2'):
        days = input('\nAmount of days Rejecting: ')
        app_rej(nm, days, "Rejected")
        time.sleep(0.30)
        print ("\n                     *Leave Rejected*")
        time.sleep(0.5)
        cls()
        arl_options()
        
    elif(lv == '3'):
        arl_options()
        
    else:
        print("\n#Invalid Input#\n")
        arl(nm)
        
def app_rej(nm, days, status):
    
    with open('status.txt', 'a') as nw:
        nw.write('\n' + nm + ' : ' +  days + ' : ' + 'days'+ ' : ' + status)

    del_app('leave.txt', nm)   
        
def del_app(file, nm):
    
    file = open(file, 'r+')
    erase = file.readlines()
    file.seek(0)
    
    for line in erase:
        if nm not in line:
            file.write(line)          
    file.truncate()
    file.close()
    
def arl_options():
    
        choice = input('''\n\n(1)Back To Pending Applications
(2)Back To Your Menu\n(3)Logout/Exit ELMS\n
Enter Choice Number: ''')
        if(choice == '1'):
                search_leave()
                
        elif(choice == '2'):
                leader_UI()
                
        elif(choice == '3'):
                more_options()

        else:
                print("#Invalid Input#\n")
                time.sleep(0.5)
                cls()
                arl_options()
    
def vew_status():
    
        cls()
        print('\n',today)
        choice = input('''\n(1)View Your Leave Application status
(2)Apply for Leave\n(3)Back to Your Main Menu\n(4)Logout/Exit ELMS
\nPlease Provide choice number: ''')
        
        if choice == '1':
                vew = 0
                
                ID = input('\nUser ID: ')
                with open('status.txt', 'r') as sts:
                        for line in sts:
                                if ID in line:
                                        if 'Approved' in line:
                                                time.sleep(0.25)
                                                print('\nFound "Approved" Application For  -', ID, '-  Here:\n',line)
                                                vew = 1
                                                pol = input('\n            Press ENTER To Continue\n')

                                        else:
                                                time.sleep(0.25)
                                                print('\nFound "Rejected" Application For  -', ID, '-  Here:\n',line)
                                                vew = 1
                                                ice = input('\n            Press ENTER To Continue\n')

                lv = open('leave.txt')
                for line in lv:
                        if line.startswith(ID):
                                vew = 1
                                time.sleep(0.25)
                                print('\nFound "Pending" Application For  -', ID, '-  Here:\n', line)
                                time.sleep(0.5)
                                back = input('\n            Press ENTER To Go Back\n')
                                vew_status()
                                
                
                if vew == 0:
                        print('\nNo Applications found for -', ID, '-')
                        time.sleep(0.5)
                        back = input('\n            Press ENTER To Go Back\n')
                        vew_status()
                          
        if choice == '2':
                leave_app()
                
        if choice == '3':
                lect_UI()
                
        if choice == '4':
                more_options()

        else:
                print('\nPlease Enter Choice Number')
                time.sleep(0.5)
                vew_status()

def hr_status():
    
        cls()
        print('\n',today)
        choice = input('''\n(1)View Leave Applications\n(2)Back to Your Menu
(3)Logout/Exit ELMS\n
Kindly Enter Choice Number: ''')
        if choice == '1':
                cls()
                print('\n',today)
                print('\n--------------------------------')
                with open('status.txt', 'r') as sts:
                        for line in sts:
                                line = line.strip()
                                print('\n',line)
                print('\n--------------------------------')
                input('\n\nPress ENTER To Return To Your Main Menu\n')
                HR_UI()
                
        elif choice == '2':
                HR_UI()
                
        elif choice == '3':
                more_options()
                
        else:
                print('\n#Input Invalid Please Enter Number#\n')
                time.sleep(0.5)
                hr_status()
                
def leave_app():
    
    cls()
    print(today)
    
    ch = input ('''\n(1)Apply For Leave
(2)Go back to Lecturer Menu
(3)Check FAQs and Leave Policies
(4)Check Public and University Holidays
(5)Logout/Exit ELMS\n
Kindly Enter Choice Number: ''')
    
    if ch == '1':

        cls()
        print('\n                      ',today)
        print('\n---------------------------Leave Application--------------------')

        data [:] = []
        nm = str(input('\nUser ID: '))
        

        file = open('lect.txt')
        for line in file:
            
            if not line.startswith(nm):
                continue
            profs = line.split()
            data.append(profs)
                
            if nm == data[0][0] and len(nm) == len(data[0][0]):

                days = str(input("Leave NUMBER of days: "))
                
                global limmit
                
                with open ('yrleave.txt', 'r') as update:
                    limmit = update.read()
                    
                if int(days) > int(limmit):
                    
                    print('\nLeave ammount of days "', days,'" is greater than limmit: ', limmit,'''
Returing to Leave Application...''')
                    time.sleep(1)
                    leave_app()
                   
                else:
                    count_check(nm, days)           

                levd= str(input("\n#LEAVE DATE DETAILS#\nLeave day(31): "))
                levm= str(input("Leave month(12): "))
                levy= str(input("Leave year(18): "))

                retd = str(input("\n#RETURN DATE DETAILS#\nReturn day(31): "))
                retm= str(input("Return month (12): "))
                rety= str(input("Return year(18): "))

                reas = str(input("\nReason: "))
                info = str(input("Additional Info: "))

                print('\nSending Application...')
            
                with open('leave.txt', 'a') as lv:
                    lv.write('\n' + nm + " : " + days +
                         " : " + levd + "/" + levm + "/"
                         + levy + " : " + retd + "/"
                         + retm + "/" + rety + " : " + reas
                         + " : " + info + " : " + "pending..."
                         + " : " + "can apply")
                
                time.sleep(0.5)
                print('                         Application Sent Successfully!')
                time.sleep(1)
                leave_app()

        else:
            print('\n#Sorry ID not registered in system, cannot apply for leave#')
            time.sleep(2)
            leave_app()
            
    elif ch == '2':
        lect_UI()

    elif ch == '3':
        read_faqs()
        leave_app()

    elif ch == '4':
        read_holiday()
        leave_app()
    
    elif ch == '5':
        more_options()
        
    else:
        print('\n                           #Invalid Input#')
        leave_app()

def count_check(nm, days):
    
    global limmit
    data [:] = []
    number = []
    sum = 0

    stat = open('status.txt')
    for line in stat:
        if line.startswith(nm):

            if not 'Approved' in line:
                continue
            line = line.strip()
            amount = line.split()    
            data.append(amount)
            txt = int(data[0][2])
            number.append(txt)
            data [:] = []

    for i in range(len(number)):
        sum = sum + number[i]
        total = sum + int(days)                    
                    
    if total > int(limmit):

        print('\n#Sorry',nm,', leave limmit:',limmit,'exceeded, you already left for:', sum , 'days#')
        time.sleep(0.5)
        gf = input('\nPress ENTER to go Back\n')
        time.sleep(0.5)
        leave_app()              

def edit_menu():
    
    cls()
    print('\n                   ',today)
    print("\n\n-----------------View, Search and Modify profiles---------------\n")
    ch = input('''(1)Edit Lecturer Accounts\n(2)Edit Academic Leader Accounts
(3)Back to your main Menu\n(4)Logout/Exit ELMS\n\nPlease Enter Choice Number: ''')
    print('\n')
 
    if (ch == '1'):
        edit_acc('lect.txt', 'LECTURER') 

    elif (ch =='2'):
        edit_acc('leader.txt', 'ACADEMIC LEADER') 

    elif (ch =='3'):
        HR_UI()
        
    elif (ch =='4'):
        more_options()

    else:
        print('                *Please Choose by Entering Corresponding Number*\n')
        edit_menu()
            
def edit_acc(file, name):

    cls()
    time.sleep(0.1)
    print('\n                    ',today)
    print('\n------------------Displaying #', name, '# Accounts---------------------------\n')

    accs = open(file, 'r')   
    for line in accs:
        print(line)

    print('-------------------------------------------------------------------------------')
    
    global word
    word = input('\nPress Enter To Return OR\nSearch accounts by ID or word: ')

    if word == '':
        edit_menu()
    fnd = 0
    
    check = open(file)
    for line in check:
        if not word in line:
            continue
        print('---------------------------------------------------------------------')
        fnd = 1
        print('\nFound "',word,'" In: \n')
        print(line)
        print('----------------------------------------------------------------------')

    if (fnd == 0): 
            print('\n           #"',word,'" Does Not Exist in ', name, ' Accounts#\n')
            time.sleep(0.5)
            xas = input('Press ENTER To Go Back\n')
            edit_acc(file,name)

    ch = input('''\n
(5)HR Main Menu
(4)Go Back to Editing Menu
(3)Go Back To Searching
(2)Delete Account(Line)
(1)Delete/Replace(Word)
\nPlease Enter Operation Number: ''')

    if ch == '1':
        rep_info(file)
        edit_options(file, name)
        
    elif ch == '2':
        del_acc(file)
        edit_options(file, name)

    elif ch == '3':
        edit_acc(file, name)

    elif ch == '4':
        edit_menu()        

    elif ch == '5':
        HR_UI()
        
    else:
        print("                             *Input Not Supported*\n")
        edit_acc(file, name)

def rep_info(file):
    
    global word
    print('\nPress Enter To Delete OR')
    
    with open(file)as nw:
        rep = nw.read()

    with open(file, 'w') as nw:
        nword = input('Change Info to: ')
        rep = rep.replace(word, nword)
        nw.write(rep)
        print("\nChange Saved!")
        hw = input('\nPress ENTER To Coninue\n')

        if nword == ' ':
            print('                       "', word,'" Erased From Account \n')
            hi = input('\nPress ENTER To Continue\n')
        else:
            print('                       "', word,'"',"Changed to",'"', nword,'"\n')
            oi = input('\nPress ENTER To Continue\n')
            
def del_acc(file):
    
    global word
    file = open(file, 'r+')
    erase = file.readlines()
    file.seek(0)

    for line in erase:
        if word not in line:
            file.write(line)
            
    file.truncate()
    file.close()
    
    print("\nErasing Account Data...")
    li = input('\nPress ENTER To Continue\n')
    
    print('\n          ***Account(s) associated with  "', word, '" Deleted***\n') 
    ar = input('\nPress ENTER To Continue\n')
    
def edit_options(file, name):
    
    cls()
    ch = input('''(1)Search/Modify Account
(2)Back to Editing Menu
(3)Back to HR Main Menu
(4)Logout/Exit ELMS\n
Please Enter Choice Number: ''')
    
    if ch == '1':
        edit_acc(file, name)
        
    if ch == '2':
        edit_menu()
        
    elif ch == '3':
        HR_UI()

    elif ch == '4':
        more_options()
        
    else:
        print("                             *Input Not Supported*\n")
        edit_options(file, name)
        

def add_prof():
    
    cls()
    print('\n                            ',today)
    print('\n                                  REGISTER NEW USER                     '
          '\n(1)Lecturer \n(2)Academic Leader \n(3)Back To Main Menu\n(4)Logout\Exit ELMS') 
    nuser = input("\nKindly Enter number: ")
    
    if nuser == '1':
        add_user('lect.txt', 'LECTURER')

    elif nuser == '2':
        add_user('leader.txt', 'ACADEMIC LEADER')
        
    elif nuser == '3':
        HR_UI()
    elif nuser == '4':
        more_options()
    else:
        print(" \n                              SORRY, INVALID RESPONSE.                          \n")
        add_prof()
    
def add_user(file, new_user):
    
    cls()
    print(today)
    print("                              NEW", new_user, "ID & Password                       ")

    nus = input('\nUsername: ')
    
    data[:] = []
    profs = open(file)

    for line in profs:
        if not line.startswith(nus):
            continue
        profs = line.split()
        data.append(profs)
        print('\n')
        print(line)

        if nus == data[0][0] and len(nus) == len(data[0][0]):
            er = input('''\n#Username ID already exists#\n
(1) Retry Registration
(2) Register another type of user
(3) Logout/Exit ELMS\n
\nChoice Number: ''')    
        if(er == '1'):
            add_user(file, new_user)
            
        elif(er == '2'):
            add_prof()
            
        elif(er == '3'):
            more_options()
            
        else:
            print('#Invalid Input#')
            add_user(file, new_user)

    npas = input('Password: ')
    fn = input('Firstname: ')
    ls = input('Lastname: ')
    gd = input('Gender: ')
    mbn = input('Mobile no.: ')
    eml = input('Email: ')
    pp = input('Passport: ')


    with open(file) as adus:
        check = adus.read()
    
    with open(file, 'a') as adus:
        adus.write('\n' + nus + ' : ' + npas  + ' : ' + fn + ' : ' + ls + ' : ' + gd +  ' : ' + mbn  + ' : ' + eml + ' : ' + pp)
        print("\nSaving...\n")
        time.sleep(1)

    print('Username:', nus , '   ' , ' Password:' ,npas)
    print('\n          *Saved Successfully*\n')
    time.sleep(1)
    add_options()
            
def add_options(): 
    
    ch = input('\nWould you like to Register another user?\nEnter n or y: ')

    if(ch == 'n'):
        wd = input('\n(1)Exit to your menu\n(2)Logout/Exit ELMS\n\nPlease Enter Choice Number: ')

        if(wd == '1'):
            HR_UI()

        elif(wd == '2'):
            more_options()

        else:
            print("\nUnsupported Response.\n")
            time.sleep(0.5)
            cls()
            add_options()

    elif(ch == 'y'):
        add_prof()

    else:
        print("\nPlease Enter only 'y' or 'n' or\n")
        time.sleep(0.5)
        cls()
        add_options()
        
def more_options():
    
    pick = input('''\nWould you like to:\n\n(1)Logout to ELM Login Page
(2)Exit ELMS\n
Choice Number: ''')

    if (pick == '1'):
        login()

    elif(pick == '2'):
        print("                                  closing...                                  ")
        time.sleep(1)
        print("                                 ELMS EXITED                               \n")
        exit()

    else:
        login()

def HR_UI():
    
    cls()
    print('\n                            ',today)
    op = input('''\n                              HUMAN RESOURCE MAIN MENU                    \n
(1)Register New User
(2)View and Modify Profiles
(3)View Lecturers Leave Status
(4)Upload Yearly Leave
(5)Upload Public & University Holidays
(6)Upload FAQs and Leave Policies
(7)Logout/Exit
\nKindly Enter Number of Choice: ''')   

    if(op == '1'):
        add_prof()
        
    elif(op == '2'):
        edit_menu()
        
    elif(op == '3'):
       hr_status()
       
    elif(op == '4'):
        add_yrleave()
        HR_UI()
        
    elif(op == '5'):
        add_holiday()
        
    elif(op == '6'):
          add_faqs()
          
    elif(op == '7'):
        more_options()
        
    else:    
        print('\n                                *Input Not Supported*\n')
        time.sleep(0.5)
        HR_UI()
            
def leader_UI():
    
    cls()
    print('\n                      ',today)
    option = input('''\n                        ACADEMIC LEADER MAIN MENU\n
(1)View Pending Leave Applications
(2)Approve/Reject Applications
(3)View Public and University Holidays
(4)View FAQs and Leave Policies
(5)Logout/Exit ELMS\n
Enter Number of Choice: ''')
        
    if(option == '1'):
        search_leave()
        
    elif (option == '2'):
        search_leave()
            
    elif (option == '3'):
        read_holiday()
        leader_UI()
        
    elif (option =='4'):
        read_faqs()
        leader_UI()
        
    elif (option =='5'):
        more_options()

    else:
        print('\n                             *Input Not Supported*\n')
        time.sleep(0.5)
        leader_UI()
            
def lect_UI():
    
    cls()
    print('\n                       ',today)
    option = input('''\n                           LECTURER MAIN MENU\n
(1)Apply for Leave
(2)Check Status of Application(s)
(3)View Public and University Holidays
(4)View FAQs and Leave Policies
(5)Logout/Exit ELMS\n
Enter Number of Choice: ''')

    if(option == '1'):
        leave_app()
                
    elif (option == '2'):
        vew_status()
        
    elif (option == '3'):
        read_holiday()
        lect_UI()
        
    elif (option =='4'):
        read_faqs()
        lect_UI()
            
    elif (option =='5'):
        more_options()
    else:
        print('\n                             *Input Not Supported*\n')
        time.sleep(0.25)
        lect_UI()
        
def login():
    
    print('\n' *50)
    cls()
    print('\n                               ',today)
    print('''
                     -----------------------------------------------
                     WELCOME TO THE EMPLOYEE LEAVE MANAGEMENT SYSTEM
                     -----------------------------------------------
          ''')
    log = input('''         (1)Human Resource  (2)ACADEMIC LEADER (3)LECTURER (4)Holidays (5)FAQs        
\nKindly Enter Number: ''')  

    if(log == '1'):
         prof_login("hr.txt", 'HUMAN RESOURCE')
         HR_UI()
         
    elif(log == '2'):
        prof_login("leader.txt", 'ACADEMIC LEADER')
        leader_UI()
        
    elif(log == '3'):
        prof_login("lect.txt", 'LECTURER')
        lect_UI()

    elif(log == '4'):
        read_holiday()
        login()

    elif(log == '5'):
        read_faqs()
        login()
        
    else:
        print('\n#Invalid Choice Please Input Number#\n')
        time.sleep(1)
        login()
                   
def prof_login(filename, name):
    
    cls()
    print('\n                                  ',today)
    print('''\n                      ---------------------------------------------
                          WELCOME TO''', name ,'''LOGIN PAGE
                      ---------------------------------------------''') 
    print('\nPress ENTER For ELMS Main Login Page')

    user = input('Username: ')
    if user == '':
        time.sleep(0.25)
        login()
    pas = input('Password: ')

        
    data[:]= []
    stat = 0
    file = open(filename)

    for line in file:
        if not line.startswith(user): 
            continue
        profs = line.split()
        data.append(profs)
        
        if user != data[0][0] and len(data[0][0]) != len(user):
            continue
            stat = 0
        elif user == data[0][0] and len(data[0][0]) == len(user):
            stat = 1
               
            if pas == data[0][2] and len(data [0][2]) == len(pas):
                print("                                     Welcome,", data[0][0], "\n")
                stat = 1
                time.sleep(0.5)
            else:
                stat = 1
                print("\n#Incorrect Password#")
                prof_login(filename, name)
                
    if stat != 1:    
        rm = input('''\n#User ID not found#\n
Press (1) Retry Login
Press (2) ELMS Login Page
Press (3) Logout/Exit ELMS
\nChoice Number: ''')    
        if(rm == '1'):
            prof_login(filename, name)
            
        elif(rm == '2'):
            login()
            
        elif(rm == '3'):
            more_options()
            
        else:
            print('                                              #INVALID INPUT#')
            time.sleep(0.75)
            prof_login(filename, name)
            
login()
