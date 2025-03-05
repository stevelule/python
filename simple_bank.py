# Defining the BankAccount class
class BankAccount:
    # Constructor to initialize account details
    def __init__(self, account_number, customer_name, balance, date_of_opening):
        self.account_number = account_number  # Stores account number
        self.customer_name = customer_name  # Stores customer name
        self.balance = balance  # Stores current balance
        self.date_of_opening = date_of_opening  # Stores account opening date

    # Method to deposit money into the account
    def deposit(self, amount):
        self.balance += amount  # Increase balance by deposited amount
        return f"Deposited: {amount}"  # Return confirmation message

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount > self.balance:  # Check if balance is insufficient
            return "Insufficient balance"
        else:
            self.balance -= amount  # Deduct amount from balance
            return f"Withdrawn: {amount}"  # Return confirmation message

    # Method to check account balance
    def check_balance(self):
        print(f"Current Balance: {self.balance}")  # Display balance

    # Method to display customer details
    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")  
        print(f"Account Number: {self.account_number}") 
        print(f"Date of Opening: {self.date_of_opening}") 
        print(f"Balance: {self.balance}")  

#  usage
account = BankAccount("123456789", "John Doe", 5000, "01-01-2023")

# Depositing money
print(account.deposit(2000))

# Withdrawing money
print(account.withdraw(3000))

# Checking balance
account.check_balance()

# Displaying customer details
account.customer_details()
