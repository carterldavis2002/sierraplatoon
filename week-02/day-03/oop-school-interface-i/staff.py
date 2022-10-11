import csv
from person import Person

class Staff(Person):
    def __init__(self, employee_id=None, **kwargs):
        super().__init__(**kwargs)
        self.employee_id = employee_id

    @classmethod
    def all_staff(cls):
        staff = []
        
        with open("staff.csv", newline="") as csv_file:
            reader = csv.DictReader(csv_file, skipinitialspace=True)

            for row in reader:
                staff.append(cls(**row))
        
        return staff