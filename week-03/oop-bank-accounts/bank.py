from account import Account
from owner import Owner
import csv

class Bank:
    def __init__(self):
        self.accounts = Account.all_accounts()
        self.owners = Owner.all_owners()

        self.link_owners()

    def link_owners(self):
        with open("data/account_owners.csv", newline="") as csv_file:
            reader = csv.DictReader(csv_file, fieldnames=["account_id", "owner_id"])

            for row in reader:
                account = Account.find(int(row["account_id"]))
                owner = Owner.find(int(row["owner_id"]))

                for a in self.accounts:
                    for o in self.owners:
                        if a.id == account.id and o.id == owner.id:
                            a.set_owner(o)