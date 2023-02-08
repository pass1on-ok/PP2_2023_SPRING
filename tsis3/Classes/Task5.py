
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            print("Insufficient funds")
            return self.balance

name = input()
balance = int(input())
acct1 = BankAccount(name, balance)
acct1.deposit(int(input()))
acct1.withdraw(int(input())) 
acct1.withdraw(int(input())) 
    
    
print(acct1.balance) 
