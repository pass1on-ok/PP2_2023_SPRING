class Account(object):
    def _init_(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print( "Deposit of" ,amount,"accepted")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Funds Unavailable!")
        else:
            self.balance -= amount
            print("Withdrawal of", amount, "accepted.")

    def _str_(self):
        return "Account owner:", self.owner,"\nAccount balance:", self.balance


account = Account('Kumar')


account.deposit(100)
account.deposit(50)


account.withdraw(25)
account.withdraw(125)


print(account)
