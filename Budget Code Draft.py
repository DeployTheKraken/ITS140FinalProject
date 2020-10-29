#!/usr/bin/env python
# coding: utf-8

# In[ ]:


############################################
#monthly subscriptions



############################################
#weekly subscription amounts



############################################
#weekly subscriptions
def get_week_sub():

    amnt_list=[]
    sub_names=[]

    print("Please enter number of weekly subscriptions")

    value=int(input())

##maybe a while not to make sure the person enters a number?

    for i in range(value):
        print("Enter subscription name")
        sub_name=str(input())
        sub_names.append(sub_name)

        print("Enter subscription amount")
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
    print("Your weekly total is:")
    print(total)

    return float(total)

############################################
#number of weeks
print("How many weeks are in the month?")
month_size=float(input())

week_array=get_week_sub()
show_weekly_sub_amnts(week_array)

total=show_weekly_sub_amnts(week_array)

print("Total cost of weekly subscriptions is: $",totalmonth_size)

############################################
#paycheck amounts
print("How many hours do you work on average per week?")
hours=float(input())

print("What is your hourly pay rate?")
payrate=float(input())

theft=hourspayrate0.800

print("Your estimated weekly paycheck is : $",theft)
print("Your estimated monthly paycheck amount is : $",theftmonth_size)

##This amount only assumes taxes, not 401k or split checks

############################################
#possible if, elif for amnt over or under budget

###########################################

