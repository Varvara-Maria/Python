from driver import Driver
import datetime

# Створюємо об'єкти водіїв
driver1 = Driver("Petrov", "Ivan", "Oleksandrovich", datetime.date(1985, 5, 10), 200, 5, "Toyota")
driver2 = Driver("Sidorov", "Oleg", "Petrovich", datetime.date(1990, 8, 15), 150, 6, "Honda")
driver3 = Driver("Kovalenko", "Maria", "Ivanivna", datetime.date(1988, 3, 20), 180, 4.5, "Ford")

# Обчислюємо заробіток кожного водія і знаходимо наймолодшого водія
drivers = [driver1, driver2, driver3]
youngest_driver = None
min_age = float('inf')

for driver in drivers:
    earnings = driver.calculate_earnings()
    age = driver.calculate_age()
    print(f"{driver.first_name} {driver.last_name}:")
    print(f"Вік: {age} років")
    print(f"Заробіток: {earnings} грн\n")
    
    if age < min_age:
        min_age = age
        youngest_driver = driver

print(f"Наймолодший водій: {youngest_driver.first_name} {youngest_driver.last_name} ({min_age} років)")