class BankAccount:
    def __init__(self,ac_holder,balance=0.0):
        self.ac_holder=ac_holder
        self.balance=balance
    def withdraw(self,amount):
        if amount<=0.0:
            raise ValueError("Invalid Amount!!")
        if self.balance<amount:
            raise ValueError("Insufficient Balance.")
        self.balance-=amount
        print(f"{amount} withdrawn successfully.")
    def deposit(self, amount):
        if amount<=0.0:
            raise ValueError("Invalid Amount!!")
        self.balance+=amount
        print(f'{amount} deposited successfully.')
    def __repr__(self):
        return f'Account Holder: {self.ac_holder}  Balance: {self.balance}'
ac1=BankAccount("Suraj Senapati",4500.0)
ac1.deposit(6000)
ac1.withdraw(2000)
print(ac1)
        