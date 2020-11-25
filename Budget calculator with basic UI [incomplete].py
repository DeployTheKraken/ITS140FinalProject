#!/usr/bin/env python
# coding: utf-8

# In[51]:


from tkinter import *

root = Tk()
root.geometry("350x250")
frame = Frame(root)
frame.pack()

leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)

label = Label (frame, text = "Welcome to the budget calculator!")
label.pack()

button1 = Button (leftframe, text = "Add weekly payments")
button1.pack(padx = 10, pady = 1)
button2 = Button (leftframe, text = "Add monthly payments")
button2.pack(padx = 10, pady = 10)
button3 = Button (frame, text = "Add a paycheck")
button3.pack(padx = 0, pady = 10)
button4 = Button(rightframe, text= "Calculate")
button4.pack(padx = 40, pady = 0)

root.title("Budget Calculator")


############################################
#monthly subscriptions
def get_monthly_amnts():

    amnt_list=[]
    sub_names=[]
    date_list=[]

    print("Please enter number of monthly subscriptions")

    value=int(input())

##maybe a while not to make sure the person enters a number?

    for i in range(value):
        print("Enter subscription/company name")
        sub_name=str(input())
        sub_names.append(sub_name)

        print("Enter amount")
        amnt=float(input())
        amnt_list.append(amnt)

        print("Enter date")
        date=str(input())
        date_list.append(date)
        
        while not(str() in date):
            print("enter date")
            date=input()
        
    return amnt_list

############################################
#weekly subscription amounts

def show_monthly_amnts(monthly_array):
    mon_total=0.0
    size=len(monthly_array)
    for i in range(size):
        mon_total=mon_total+monthly_array[i]
    
    return float(mon_total)

############################################
#weekly subscriptions
def get_week_sub():
    
    #number of weeks here?
    print("How many weeks are in the month?")
    month_size=float(input())
    
    amnt_list=[]
    sub_names=[]

    print("Please enter number of weekly payments")

    value=int(input())

##maybe a while not to make sure the person enters a number?

    for i in range(value):
        print("Enter subscription/company name")
        sub_name=str(input())
        sub_names.append(sub_name)

        print("Enter amount")
        amnt=float(input())
        amnt_list.append(amnt)

    return amnt_list

############################################
#weekly subscription amounts

def show_weekly_sub_amnts(week_array):
    total=0.0
    size=len(week_array)
    for i in range(size):
        total=total+week_array[i]
    
    return float(total)

############################################
#number of weeks

week_array=get_week_sub()
show_weekly_sub_amnts(week_array)

total = show_weekly_sub_amnts(week_array)


############################################

monthly_array = get_monthly_amnts()
show_monthly_amnts(monthly_array)

mon_total =show_monthly_amnts(monthly_array)

############################################

#paycheck amounts
def get_paycheck(theft, mon_total, week_total, mon_paycheck, expense_total, final_amt):
    print("How many hours do you work on average per week?")
    hours=float(input())

    print("What is your hourly pay rate?")
    payrate=float(input())

    theft=hours*payrate*0.800

    mon_paycheck=theft*month_size

    week_total=total*month_size

    expense_total=week_total+mon_total

    final_amnt=mon_paycheck-expense_total
    
    return theft, mon_total, week_total, mon_paycheck, expense_total, final_amt

###################################################################

def calc_total_and_over_under_budget(week_total, mon_total, theft, mon_paycheck, expense_total):

    print("Monthly cost of weekly payments is: $",week_total)
    print("Monthly cost of monthly payments is: $",mon_total)
    print("Your estimated weekly paycheck is : $",theft)
    print("Your estimated monthly paycheck amount is : $",mon_paycheck)
    print("Your estimated monthly expenses are: $",expense_total)

####################################################################

###### THIS IS THE MOST WIP PART OF ALL THE CODE! COMMENTED THESE LINES OUT B/C I'M NOT SURE HOW THEY WORK YET ######
### To see the UI immediately, remove all functions.
'''
button1.bind('<button-1>', get_week_sub())
button2.bind('<button-1>', get_monthly_amnts())
button3.bind('<button-1>', get_paycheck(theft, mon_total, week_total, mon_paycheck, expense_total, final_amt, month_size))
button4.bind('<button-1>', calc_total_and_over_under_budget())
'''

if (mon_paycheck>expense_total):
    print("The amount left for the month is $",final_amnt)
elif (expense_total>mon_paycheck):
    print("You are $", final_amnt,"over budget")
else:
    print("You are $0 over budget")

    
root.mainloop()


# In[ ]:




