class FootballClub:
    def __init__(self, name, country, year_founded, president, budget, trophies_won):
        self.name = name
        self.country = country
        self.year_founded = year_founded
        self.president = president
        self.budget = budget
        self.trophies_won = trophies_won

    def __str__(self):
        return f"Club: {self.name}, Country: {self.country}, Founded: {self.year_founded}, President: {self.president}, Budget: {self.budget}, Trophies: {self.trophies_won}"

    def __repr__(self):
        return self.__str__
