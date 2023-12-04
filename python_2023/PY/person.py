import datetime

class Person:
    def __init__(self, last_name, first_name, middle_name, birthdate):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.birthdate = birthdate

    def calculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age