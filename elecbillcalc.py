  # Function to calculate electricity bill
def calculate_electricity_bill(units):
    if units <= 199:  
        rate = 1.20
    elif units < 400: 
        rate = 1.50
    elif units < 600:  
        rate = 1.80
    else:  
        rate = 2.00

# Calculate the total bill
    bill = units * rate  
    # Return the bill amount
    return bill  

# Get user input
units_consumed = int(input("Enter the number of units consumed: ")) 

# Calculate the bill
total_bill = calculate_electricity_bill(units_consumed)  

# Display the bill
print(f"Electricity bill: Ksh {total_bill:.2f}")  
