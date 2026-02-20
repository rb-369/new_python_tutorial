# Moderate Problem: Bank Account Management System
# Problem Statement:
# Design a class BankAccount with:
# Class Attributes:
# • bank_name = "National Bank"
# • total_accounts = 0
# • total_bank_balance = 0
# Instance Attributes:
# • account_holder
# • balance
# Requirements:
# • Increment total_accounts when a new account is created.
# • Add the initial deposit to total_bank_balance.
# • Create methods:
# • deposit(amount) → increase balance and update total_bank_balance
# • withdraw(amount) → decrease balance and update total_bank_balance
# • display_account_info()
# • Ensure withdrawal cannot exceed balance.
# • Add a class method display_bank_summary() that prints:
# • Bank name
# • Total accounts
# • Total bank balance

class BankAccount:
    bank_name="National Bank"
    total_accounts = 0
    total_bank_balance = 0

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder,
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        BankAccount.total_bank_balance+=amount
        print(f"Your Bank Banlance After Depositing Rs{amount}: Rs{self.balance}")

    def withdraw(self, amount):
        if(amount>self.balance):
            print("Not enough balance in the account")
            return
        self.balance -= amount
        BankAccount.total_bank_balance -= amount    
        print(f"Your Bank Banlance After Withdrawing Rs{amount}: Rs{self.balance}")

    def acc_info(self):
        print(f"Acoount Holder: Rs{self.account_holder}")
        print(f"Bank: Rs{self.bank_name}")
        print(f"Balance: Rs{self.balance}")    

b1 = BankAccount("Rb", 0)
b1.deposit(50)
b1.withdraw(31)
b1.acc_info()