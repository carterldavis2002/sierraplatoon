import csv

class Owner:
    def __init__(self, id, last, first, addr, city, state):
        self.id = int(id)
        self.last = last
        self.first = first
        self.addr = addr
        self.city = city
        self.state = state
    
    @classmethod
    def all_owners(cls):
        owners = []

        with open("data/owners.csv", newline="") as csv_file:
            reader = csv.DictReader(csv_file, fieldnames=["id", "last", "first", "addr", "city", "state"])

            for row in reader:
                owners.append(cls(**row))
        
        return owners

    @classmethod
    def find(cls, id):
        for owner in cls.all_owners():
            if owner.id == id:
                return owner