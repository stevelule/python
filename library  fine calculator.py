#Library fine Calculator

#importing datetime module
from datetime import datetime

#User input
BookId = input("Enter the Book  ID: ")
Due_date = input("Enter the Duedate (MM-DD-YYY): ")
Return_Date = input("Enter the Returning date (MM-DD-YYY): ")

#converting user input to actual date format
Due_date = datetime.strptime(Due_date,"%m-%d-%Y")
Return_Date =datetime.strptime(Return_Date,"%m-%d-%Y")

#Calculating number of overdue days
Days_overdue = (Return_Date - Due_date).days

#Conditions to determine charges

if Days_overdue <=0 :
    fine_Rate = 0

elif Days_overdue <=7 :
    fine_Rate = 20

elif Days_overdue <=14 :
    fine_Rate = 50

else:
      fine_Rate = 100

#calculation to get the total fine
Total_Fine = Days_overdue * fine_Rate if Days_overdue >0 else 0


#output
print("\n--- Library Fine Details ---")
print(f"Book ID: {BookId}")
print(f"Due Date: {Due_date.strftime('%m-%d-%Y')}")
print(f"Return Date: {Return_Date.strftime('%m-%d-%Y')}")
print(f"Days Overdue: {Days_overdue}")
print(f"Fine Rate: Ksh {fine_Rate} per day")
print(f"Total Fine Amount: Ksh {Total_Fine}")



