class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Account is inactive.")

    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Account is inactive.") 

    def deactivate(self):
        self.is_active = False
        print("Account has been deactivated.")

    def activate(self):
        self.is_active = True
        print("Account has been activated.")

account1 = BankAccount("Mario Ramos", 1000)
account1.deposit(500)
account1.withdraw(200)
account1.deactivate()
account1.deposit(100)
account1.activate()
account1.withdraw(300)  