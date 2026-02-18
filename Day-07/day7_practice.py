class BankAccount:
    def __init__(self, account_no, balance=0):
        self.account_no = account_no
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited into account {self.account_no}")
        else:
            print("Deposit amount must be positive")
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn from account {self.account_no}")

    def check_balance(self):
        print(f"Account {self.account_no} Balance: ₹{self.balance}")
  # Create accounts
acc1 = BankAccount(101, 5000)
acc2 = BankAccount(102, 3000)
# Perform transactions
acc1.deposit(2000)
acc1.withdraw(1500)
acc1.check_balance()
print("-----------")
acc2.deposit(1000)
acc2.withdraw(5000)   # insufficient balance
acc2.check_balance()

