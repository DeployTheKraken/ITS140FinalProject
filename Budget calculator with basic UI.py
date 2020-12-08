#!/usr/bin/env python
# coding: utf-8

# In[4]:


#MUST BE FIRST LINE OF CODE
from tkinter import *

# create a new tk object named "root"
root = Tk()

# set up the window
## geometry is width x height in pixels of the total amount of space the total amount of created tk vars can take up
root.geometry("350x250")

## create a new frame object named "frame". think of it as a program window. all our interface display will be inside this frame
### NOTE:  frame auto-fills the entire above-mentioned geometry (350 x 250 here).
frame = Frame(root)

## .pack() takes whatever object is calling that function and puts it inside a tk object (instance named "root" here)
frame.pack()

## the code below creates a "left side" and "right side" of the frame and orients them to the left and right of the display
''' NOTE: 
creating 2 additional frames splits the window into 3 for positioning: 
            a left side("leftframe"), a middle ("frame"), and a right side ("rightside")
Since both leftframe and rightframe are also created with Frame(root), 
"frame", "leftside", and "rightside" are all identical Frame objects that are "aware" of one another existing inside main;"root"
'''
leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)


label = Label (frame, text = "Welcome to the budget calculator!")
label.pack()


###################### weekly ######################

weekly_amnt_list=[]
weekly_sub_names=[]
m_weeks = 0

label1 = Label(frame, text = "How many weeks are in the month?")
weeks_in_month = Entry (frame)
m_weeks = int(weeks_in_month)

label2 = Label (leftframe, text = "Enter subscription/company name")
weekly_name = Entry (leftframe)
#add subscription names to file
weekly_sub_names.append(weekly_name)

label3 = Label (leftframe, text = "Enter amount")
weekly_take_amt = Entry (leftframe)
#add subscription cost to file
weekly_amnt_list.append (weekly_take_amnt)

#############################################################################

''' Getting around global vars with writing to files! '''

def write_to_weekly_file(date, names, fees, weeks):
    # open file as read-only
    file_reader = open("weekly.txt", "r")
    
    #validate appended entries. validatating just the new appends still ensures that all previous entries are valid.
    
    # 1. Validate weeks in month
    if weeks < 0 or weeks > 5 or weeks == 1 or weeks == 2:
        failed0 = Label (frame, text = "The submitted weeks for month is invalid.  Please enter a valid number of weeks for a month and try again.")
        file_reader.close()
        
    # 2. Validate most recent date append
    while True:
        # @catch & @display
        try:
            catcher = str(date(date.len()))
        except ValueError:
            failed1 = Label (frame, text = "The submitted date is invalid.  Please enter a valid date and try again.")
            break
        else:
            break
    # 3. Validate most recent name append
    while True:
        # @catch & @display
        try:
            catcher = str(names(names.len()))
        except ValueError:
            failed2 = Label (frame, text = "The submitted subscription name is invalid.  Please enter a valid title and try again.")
            break
        else:
            break
    # 4. validate most recent cost append
    while True:
        # @catch & @display
        try:
            catcher = float(fees(fees.len()))
        except ValueError:
            failed3 = Label (frame, text = "The submitted cost is invalid.  Please enter a valid number and try again.")
        else:
            break
            
    # determine if file has been previously been written to:
    if str(file_reader.readline()).startswith("\n"):
        # if @this, file has data in it. close file & @append data to it
        file_reader.close()
    else:
        # file has not been previously written to. designate new:
        file_reader.close()
        f_designate = open("weekly.txt", "w")
        f_designate.write("\n")
        f_designate.close()
    
    # append the valid data to the end of the file
    f_apply = open("weekly.txt", "a")
    
    #1. find number of entries
    entry_count = data_dump.count("\n")
    # ... subtract 1 from it becuase we do the designation with a \n
    entry_count -= 1
    
    f_apply.append("Week expense #", entry_count, "is name:", names[names.len()], "fees:", fees[fees.len()])
    
    #2. write to @master file. @master is for debugging purposes!
    f_apply.close()
    
    f_master = open("internal_data.txt", "w")
    
    #locate start of line
    find_string = ""
    find_string = "number of entries in weekly.txt = "
    find_string.strip()
    find_length = 28
        
    # locate counter lines
    master_dump = str(f_master.read())
    dump_array = master_dump.splitlines()
        
    for y in dump_array:
        # if the line starts with the string we want to find,
        if dump_aray(y).startswith(find_str) == True:
                
            # separate it out! (casting as a precaution)
            grab_str = str(dump_aray(y))
            # We start at the end of the identifier (=),
            val = grab_str.find("=") + 1
            # and our number/s should begin right after that
            if val == find_length + 1:
                
                #so we "snip" that value out of the file's string!
                #leave end of range for file to automatically go to end
                snip = str(grab_str[val:])
                
                # replace the outdated information with updated information
                grab_str.replace(snip, entry_count,"\n")
                # and then replace the entire string
                master_dump(y).replace(grab_str,"\n")
                    
                # ... and then replace the whole file.
                '''I wasted 3 weeks struggling to understand what I was reading about os library... 
                and then I realized that I no longer had time to try to understand it'''
                f_master.write("\n")
                for z in f_master:
                    f_master.append(master_dump(z))
###########################################################################################

# call write on button click
b_add_weekly_payment = Button (leftframe, text = "Add weekly payment", command = write_to_weekly_file(weekly_date_list, weekly_amnt_list, weekly_sub_names, m_weeks))

#################### monthly #########################

payment_due_date = []
monthly_sub_names=[]
monthly_amnt_list=[]

label4 = Label(leftframe, text = "Enter subscription/company name")
month_sub_name = Entry (leftframe)
monthly_sub_names.append(monthly_sub_names)

label5 = Label(leftframe, text = "Enter amount")
month_sub_amt = Entry (leftframe)
monthly_amnt_list.append(monthly_amnt_list)

label6 = Label(leftframe, text = "Enter date")
sub_payment_date = Entry (leftframe)
payment_due_date.append(sub_payment_date)

##############################################################

''' Getting around global vars with writing to files! '''

def write_to_weekly_file(date, names, fees):
    # open file as read-only
    file_reader = open("monthly.txt", "r")
    
    #validate appended entries. validatating just the new appends still ensures that all previous entries are valid.
    
    # 1. Validate most recent date append
    while True:
        # @catch & @display
        try:
            catcher = str(date(date.len()))
        except ValueError:
            failed0 = Label (frame, text = "The submitted due date is invalid.  Please enter a valid date and try again.")
        else:
            break
    # 2. Validate most recent name append
    while True:
        # @catch & @display
        try:
            catcher = str(names(names.len()))
        except ValueError:
            failed1 = Label (frame, text = "The submitted subscription name is invalid.  Please enter a valid title and try again.")
        else:
            break
    # 3. validate most recent string append
    while True:
        # @catch & @display
        try:
            catcher = float(fees(fees.len()))
        except ValueError:
            failed2 = Label (frame, text = "The submitted cost is invalid.  Please enter a valid number and try again.")
        else:
            break
            
    # determine if file has been previously been written to:
    if str(file_reader.readline()).startswith("\n"):
        # if @this, file has data in it. close file & @append data to it
        file_reader.close()
    else:
        # file has not been previously written to. designate new:
        file_reader.close()
        f_designate = open("monthly.txt", "w")
        f_designate.write("\n")
        f_designate.close()
    
    # append the valid data to the end of the file
    f_apply = open("monthly.txt", "a")
    
    #1. find number of entries
    entry_count = data_dump.count("\n")
    # ... subtract 1 from it becuase we do the designation with a \n
    entry_count -= 1
    
    if entry_count <= 0:
        entry_count = 1
    
    f_apply.append("Monthly expense #", entry_count, "is date:", date[date.len()], "name:", [names.len()], "fees:", [fees.len()])
    
    #2. write to @master file. @master is for debugging purposes!
    f_apply.close()
    
    f_master = open("internal_data.txt", "w")
    
    #locate start of line
    find_str = "number of entries in monthly.txt = "
    find_str.strip()
    find_length = 29
        
    # locate counter lines
    master_dump = str(f_master.read())
    master_dump_array = master_dump.splitlines()
        
    for y in master_dump:
        # if the line starts with the string we want to find,
        if master_dump(y).startswith(find_str) == True:
                
            # separate it out! (casting as a precaution)
            grab_str = str(master_dump(y))
            # We start at the end of the identifier (=),
            val = grab_str.find("=") + 1
            # and our number/s should begin right after that
            if val == find_length + 1:
                
                #so we "snip" that value out of the file's string!
                #leave end of range for file to automatically go to end
                snip = str(grab_str[val:])
            
                # replace the outdated information with updated information
                grab_str.replace(snip, entry_count,"\n")
                # and then replace the entire string
                master_dump(y).replace(grab_str,"\n")
                
                # ... and then replace the whole file.
                '''I wasted 3 weeks struggling to understand what I was reading about os library... 
                and then I realized that I no longer had time to try to understand it'''
                f_master.write("\n")
                for z in f_master:
                    f_master.append(master_dump(z))
###########################################################################################
payment_due_date = []
monthly_sub_names=[]
monthly_amnt_list=[]

b_add_monthly_payments = Button (leftframe, text = "Add monthly payment", command = write_to_monthly_file(payment_due_date, monthly_sub_names, monthly_amnt_list))

#################### paycheck ###################
paycheck_hours = []
paycheck_pay_rate = []

label7 = Label(leftframe, text = "Enter hours worked for one week")
paycheck_add_hours = Entry (leftframe)
paycheck_hours.append(paycheck_add_hours)

label8 = Label(leftframe, text = "Enter hourly pay rate")
paycheck_hourly_pay = Entry (leftframe)
paycheck_pay_rate.append(paycheck_hourly_pay)

###########################################################################################
def get_paycheck(hours, payrate):
    # open file as read-only
    file_reader = open("paycheck.txt", "r")
    
    while True:
        try:
            hours=float(hours(hours.len())
        except ValueError:
            print("The submitted work hours is invalid.  Please enter a valid number of hours and try again.")
        else:
            break

    while True:
        try:
            payrate=float(payrate(payrate.len())
        except ValueError:
            print("The submitted pay rate is invalid.  Please enter a valid rate and try again.")
        else:
            break
    # determine if file has been previously been written to:
    if str(file_reader.readline()).startswith("\n"):
        # if @this, file has data in it. close file & @append data to it
        file_reader.close()
    else:
        # file has not been previously written to. designate new:
        file_reader.close()
        f_designate = open("paycheck.txt", "w")
        f_designate.write("\n")
        f_designate.close()
    
    # append the valid data to the end of the file
    f_apply = open("paycheck.txt", "a")
    
    #1. find number of entries
    data_dump = str(f_apply.read())
    entry_count = data_dump.count("\n")
    # ... subtract 1 from it becuase we do the designation with a \n
    entry_count -= 1
                          
    # *** and divide by 2 because every paycheck has two appends! ***
    entry_count = entry_count / 2
    
    if entry_count <= 0:
        entry_count = 1
    
    f_apply.append("Paycheck #", entry_count, "is hours:", hours[hours.len()], "and payrate:", payrate[payrate.len()])
    
    ####################### calculate paycheck #############################
    
    #1. net pay
    net_pay = hours * payrate
    
    # 2. taxes
    tax = 0
    tax = net_pay * 0.800
    
    # 3. check
    total = net_pay - tax
                          
    # 4. append               
    f_apply.append("Net pay for check #", entry_count, "is $",net_pay, "and remaining check is: $",total)   
                          
    #########################################################################
                          
    # 4. write to @master file. @master is for debugging purposes!
    f_master = open("internal_data.txt", "w")
    
    #locate start of line
        find_str = "number of entries in paycheck.txt = "
        find_str.strip()
        find_length = 30
        
    # locate counter lines
        master_dump = str(f_master.read())
        read_array = master_dump.splitlines()
                          
        for y in read_array:
            # if the line starts with the string we want to find,
            if read_array(y).startswith(find_str) == True:
                
                # separate it out! (casting as a precaution)
                grab_str = str(master_dump(y))
                # We start at the end of the identifier (=),
                val = grab_str.find("=") + 1
                # and our number/s should begin right after that
                if val == find_length + 1:
                
                    #so we "snip" that value out of the file's string!
                    #leave end of range for file to automatically go to end
                    snip = grab_str[val:]
                
                    # replace the outdated information with updated information
                    grab_str.replace(snip, entry_count"\n")
                    # and then replace the entire string
                    master_dump(y).replace(grab_str"\n")
                    
                    # ... and then replace the whole file.
                    '''I wasted 3 weeks struggling to understand what I was reading about os library... 
                    and then I realized that I no longer had time to try to understand it'''
                    f_master.write("\n")
                    for z in f_master:
                        f_master.append(master_dump(z))
###########################################################################################

b_add_new_paycheck = Button (rightframe, text = "Add paycheck", command = get_paycheck(paycheck_hours, paycheck_pay_rate))

########################## calculate budget ########################
def calc_total(weeks):
    expenses = 0
                          
    # 1. read paychecks
    r_checks = open("paycheck.txt", "r")
    check_identifier_key = "Net pay for check #"
    
    # count number of paychecks
    check_dump = str(r_checks.read())
                          
    num_checks = check_dump.count(check_identifier_key)
    start_pos = "and remaining check is: $"
    
    check_dump_array = check_dump.splitlines()
                          
    # catch if no paychecks entered
    if num_checks <= 0:
        check_error = Label(leftframe, text = "The program cannot find any paychecks.  Please create one and try again.")
        break
    
    money_to_spend = 0.0
    running_total = 0.0
    
    # total money
    for x in check_dump_array:
        if check_dump_array(x).startswith(check_identifier_key) == True:
            snip = str(check_dump_array(x))
            pos = snip.index(start_pos) + 1
            
            val = float(snip[pos:].strip())
            money_to_spend += val
    
    r_checks.close()
                          
    # open monthly
    monthly_dates = []
    monthly_names = []
    monthly_fees = []
                          
    entry_id_key = "Monthly expense #"
    start_pos1 = "date:"
    start_pos2 = "name:"
    start_pos3 = "fees:"
                          
    r_month = open("monthly.txt", "r")
                          
    m_dump = str(r_month.read())
    num_entries = m_dump.count(entry_id_key)                  
    
    # catch if no monthly expenses entered
    if num_entries <= 0:
        check_error = Label(leftframe, text = "The program cannot find any monthly expenses.  Please create one and try again.")
        break
                          
    m_entry_array = m_dump.splitlines()
    
    for y in m_entry_array:
        if m_entry_array(y).startswith(entry_id_key) == True:
            snip1 = str(entry_array(y))
            pos = snip1.index(start_pos1) + 1
            entry = str(snip1[pos:])
            
            monthly_dates.append[entry]
                          
            # clear
            entry = ""
            pos = 0
            
            snip2 = str(entry_array(y))
            pos = snip2.index(start_pos2) + 1
            entry = str(snip2[pos:])
            
            monthly_names.append[entry]
                          
            # clear
            val = 0.0
            pos = 0
                          
            snip3 = str(entry_array(y))
            pos = snip3.index(start_pos3) + 1
            val = float(snip3[pos:].strip())
                          
            monthly_fees.append(val)
            expenses += val
                          
    r_month.close()
    num_entries = 0
    
    # open weekly                     
    weekly_names = []
    weekly_fees = []
                          
    entry_id_key = "Weekly expense #"
    start_pos1 = "name:"
    start_pos2 = "fees:"
                          
    r_weekly = open("weekly.txt", "r")
                          
    w_dump = str(r_weekly.read())
    num_entries = w_dump.count(entry_id_key)                  
    
    # catch if no monthly expenses entered
    if num_entries <= 0:
        check_error = Label(leftframe, text = "The program cannot find any weekly expenses.  Please create one and try again.")
        break
                          
    w_entry_array = w_dump.splitlines()
    
    for y in entry_array:
        if w_entry_array(y).startswith(entry_id_key) == True:
            w_snip1 = str(entry_array(y))
            pos = w_snip1.index(start_pos1) + 1
            entry = str(w_snip1[pos:])
            
            weekly_names.append(entry)
                          
            # clear
            val = 0
            pos = 0
            
            w_snip2 = str(entry_array(y))
            pos = w_snip2.index(start_pos2) + 1
            val = float(snip2[pos:].strip())
                          
            weekly_fees.append[val]
            
            expenses += val * weekly_date_list
                              
    r_week.close()
   
    #calculate over/under budget
    running_total = money_to_spend - expenses
    
    if running_total >= 0:
        remaining_money = Label (frame, "You have $", running_total, "left over.")
    else:
        remaining_money = Label (frame, "You are $", running_total * -1, "over your budget.")
     
    # display due date/s for monthly payments
    due_dates = ""
                          
    for z in monthly_dates:
        due_dates += str(monthly_dates(z)), ","
        
    m_date_label = Label (rightframe, "Your monthly payments are due on: ", due_dates)
                          
    for a in weekly_names:
        w_date += str(weekly_names(a)), ","
                          
    w_date_label = Label (rightframe, "Your weekly payments are for:  ", w_date)
###############################################################################################
                          
b_calc_budget = Button(frame, text = "Calculate Budget", command = calc_total())

############################ new budget; clear all files #######################

#####################################################################################
def new_budget():
    w_paycheck = open ("paycheck.txt", "w")
    w_paycheck.write()
    w_paycheck.close()
    
    w_monthly = open ("monthly.txt", "w")
    w_monthly.write()
    w_paycheck.close()
                          
    w_weekly = open ("weekly.txt", "w")
    w_weekly.write()
    w_paycheck.close()
                          
    w_internal_data = open ("internal_data.txt", "w")
    w_internal_data.write("numberofentriesinmonthly.txt=0 \n numberofentriesinweekly.txt=0 \n numberofentriesinpaycheck.txt=0")
##############################################################################                          
                          
b_start_over = Button(rightframe, text = "Create a new Budget", command = new_budget())    
#####################################################################################
                          
# MUST BE LAST LINE OF CODE; tells the program to create a window and keep it open until the program is (manually) terminated    
root.mainloop()


# In[ ]:




