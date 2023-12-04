from person import Person

class Driver(Person):
    def __init__(self, last_name, first_name, middle_name, birthdate, distance, cost_per_km, car_brand):
        super().__init__(last_name, first_name, middle_name, birthdate)
        self.distance = distance
        self.cost_per_km = cost_per_km
        self.car_brand = car_brand

    def calculate_earnings(self):
        earnings = self.distance * self.cost_per_km
        return earnings