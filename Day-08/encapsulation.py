class BankAccount:
  def __init__(self,account_no,blance):
    self.account_no=account_no
    self._balance=balance
  def deposit(self,amount):
    self._balance+=amount
  def get_balance(self):
    return self._balance
acc=BankAccount(123,500)
acc.deposit(400)
print(acc.get_balance())
