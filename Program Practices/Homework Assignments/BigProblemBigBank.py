'''
Problem 1:

You have been hired by 🅱️ig city 🅱️ank to develop their virtual 🅱️anking platform. 🅱️ig city 🅱️ank offers three kinds of bank accounts: 🅱️asic, Premium, and ULTRA_ELITE 
(the underscore amplifies the sense of significance one feels in the presence of an ULTRA_ELITE account holder). 
Each bank account has a balance, and interest rate; the balance is set to an initial deposit passed through the constructor, and the annual interest rates vary by the types of account.

You will implement the actions deposit (to increase balance), take_out (to decrease balance), and simple interest (argument years, return simple interest as float).
 Premium and ULTRA_ELITE account holders also have an annual fee; create a function to subtract that amount from their balance if they have the funds.

Here is a table listing the difference between account types:

Basic: 10% Intrest Rate     No annual fee
Premium: 13% Intrest Rate   Annual fee $1000
ULTRA_ELITE: 17% Intrest rate   Annual fee $10,000

'''

class Basic():
    def __init__(self):
        self.balance = 100 # Initial Deposit
        self.interest_rate = 0.1 # 10%
        self.annual_fee = 0
    
    def deposit(self, money):
        self.balance += money
    
    def take_out(self, money):
        if self.balance >= money:
            self.balance -= money

    def simple_interest(self, years):
        fee = years*self.annual_fee
        interest = self.balance*(1 + self.interest_rate * years) - fee
        return interest

class Premium():
    def __init__(self):
        self.balance = 200 # Initial Deposit
        self.interest_rate = 0.13 # 13%
        self.annual_fee = 1000
    
    def deposit(self, money):
        self.balance += money
    
    def take_out(self, money):
        if self.balance >= money:
            self.balance -= money

    def simple_interest(self, years):
        fee = years*self.annual_fee
        interest = self.balance*(1 + self.interest_rate * years) - fee
        return interest

class ULTRA_ELITE():
    def __init__(self):
        self.balance = 300 # Initial Deposit
        self.interest_rate = 0.17 # 17%
        self.annual_fee = 10000
    
    def deposit(self, money):
        self.balance += money
    
    def take_out(self, money):
        if self.balance >= money:
            self.balance -= money

    def simple_interest(self, years):
        fee = years*self.annual_fee
        interest = self.balance*(1 + self.interest_rate * years) - fee
        return interest


