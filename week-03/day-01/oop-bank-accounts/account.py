import csv
from owner import Owner
from datetime import datetime

class Account:
    def __init__(self, id, balance, open_date):
        if int(balance) < 0:
            raise Exception("Cannot create account with negative balance.")
    
        self.id = int(id)
        self.balance = int(balance)
        self.open_date = datetime.strptime(open_date, "%Y-%m-%d %H:%M:%S %z")
        self.owner = None

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("WARNING: Withdraw makes account balance negative, balance not modified.")
        
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def set_owner(self, owner):
        self.owner = owner

    @classmethod
    def all_accounts(cls):
        accounts = []

        with open("data/accounts.csv", newline="") as csv_file:
            reader = csv.DictReader(csv_file, fieldnames=["id", "balance", "open_date"])

            for row in reader:
                accounts.append(cls(**row))
        
        return accounts

    @classmethod
    def find(cls, id):
        for account in cls.all_accounts():
            if account.id == id:
                return account