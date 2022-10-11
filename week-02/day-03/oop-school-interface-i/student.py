import csv
from person import Person

class Student(Person):
    def __init__(self, school_id=None, **kwargs):
        super().__init__(**kwargs)
        self.school_id = school_id

    @classmethod
    def all_students(cls):
        students = []

        with open("students.csv", newline="") as csv_file:
            reader = csv.DictReader(csv_file, skipinitialspace=True)

            for row in reader:
                students.append(cls(**row))
        
        return students