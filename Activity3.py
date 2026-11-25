

import keyword
#print(keyword.kwlist)

person_name = input("Enter your name: ")
goal_name = input("Enter one skill you want to get better at: ")
target_month  = input("Enter the month you want to reach it by: ")
daily_minutes = 30


#---------printing the personal goal plan-------

print("\n MY PERSONAL GOAL PLAN\n")
print ("Name: ",person_name)
print ("Daily practice: ",daily_minutes,"minutes")
print("Status: ",end=" ")
print("Not Started")
print ("Reminder:",end=" - ")
print("Practice Everyday!!")

print(person_name,"plans to work on",goal_name,"for",daily_minutes,"minutes everyday until",target_month)




