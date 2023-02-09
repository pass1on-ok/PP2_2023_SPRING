
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
            print("Остаток: ")
            return self.balance
        else:
            print("Insufficient funds")
            return self.balance

name = input('Имя ' )
balance = int(input('Баланс '))
acct1 = BankAccount(name, balance)
acct1.deposit(int(input('Депозит: ')))
acct1.withdraw(int(input('Сколько хотите снять: '))) 
acct1.withdraw(int(input('Сколько хотите снять: '))) 
    
    
print(acct1.balance) 
