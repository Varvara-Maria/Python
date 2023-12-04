import ZODB
import ZODB.FileStorage
import transaction
from persistent import Persistent
from football_club import FootballClub

# Відкриття бази даних ZODB
storage = ZODB.FileStorage.FileStorage("football_club.fs")
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()

def add_club(name, country, year_founded, president, budget, trophies_won):
    club = FootballClub(name, country, year_founded, president, budget, trophies_won)
    root[name] = club
    transaction.commit()

def calculate_budget_by_country(country):
    total_budget = sum([club.budget for club in root.values() if club.country == country])
    return total_budget

def find_most_successful_club():
    most_successful = max(root.values(), key=lambda club: club.trophies_won)
    return most_successful
