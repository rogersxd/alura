class Account:
    def __init__(self, number, holder, balance, limit):
        print("Building object...{}".format(self))
        self.number = number
        self.holder = holder
        self.balance = balance
        self.limit = limit

    def statement(self):
        print("Saldo `{} do titular {}".format(self.balance, self.holder))