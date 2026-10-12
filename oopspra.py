# class customer_details:
#     def __init__(self, customer_name, customer_phno, customer_country):
#         self.a = customer_name
#         self.b = customer_phno
#         self.c = customer_country
#     def cust_data(self):
#         print("customer_name =", self.a)
#         print("customer phone.no =", self.b)
#         print("customer country =", self.c)
# def log_output(log_message):
#     with open(r"C:\Users\anuma\Desktop\desktop info\log2.txt", "a") as log_file:
#         log_file.write(log_message + "\n")
# name = input("Enter your name: ").strip()
# phno = int(input("Enter your mobile number: "))
# country = input("Enter your country: ").strip()
# customer1 = [name, phno, country]
# customer = customer_details(*customer1)
# customer.cust_data()
# log_message = f"Customer name: {name} | Phone: {phno} | Country: {country}"
# log_output(log_message)


# class BankAccount:
#     def __init__(self, customer_name, account_number, balance, monthly_interest_rate):
#         self.customer_name = customer_name
#         self.account_number = account_number
#         self.balance = balance
#         self.monthly_interest_rate = monthly_interest_rate
#     def calculate_interest(self):
#         interest = self.balance * self.monthly_interest_rate / 100
#         return interest
#     def add_monthly_interest(self):
#         interest = self.calculate_interest()
#         self.balance = self.balance + interest
#         return interest
#     def display_details(self):
#         print("Customer Name:", self.customer_name)
#         print("Account Number:", self.account_number)
#         print("Balance:", self.balance)
#         print("Monthly Interest Rate:", self.monthly_interest_rate)
#         print()
# # Creating customers/accounts
# customer1 = BankAccount("Ravi", 101, 50000, 1)
# customer2 = BankAccount("Anu", 102, 75000, 1.5)
# customer3 = BankAccount("Rahul", 103, 100000, 2)
# # Display original details
# print("Before Monthly Interest:")
# customer1.display_details()
# customer2.display_details()
# customer3.display_details()
# # Adding monthly interest
# interest1 = customer1.add_monthly_interest()
# interest2 = customer2.add_monthly_interest()
# interest3 = customer3.add_monthly_interest()
# # Display updated details
# print("After Monthly Interest:")
# customer1.display_details()
# customer2.display_details()
# customer3.display_details()