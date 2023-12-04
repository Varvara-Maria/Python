from database import add_club, calculate_budget_by_country, find_most_successful_club
import transaction

# Відкриття транзакції перед додаванням клубів
transaction.begin()

# Додавання клубів до бази даних
add_club("Real Madrid", "Spain", 1902, "Florentino Perez", 800000000, 34)
add_club("FC Barcelona", "Spain", 1899, "Joan Laporta", 850000000, 26)
add_club("Manchester United", "England", 1878, "Joel Glazer", 750000000, 42)

# Завершення та закриття транзакції
transaction.commit()

# Обчислення загального бюджету клубів для заданої країни (наприклад, Іспанія)
total_budget_spain = calculate_budget_by_country("Spain")
print("Total budget for clubs in Spain:", total_budget_spain)

# Знаходження клубу, який виграв найбільше трофеїв
most_successful = find_most_successful_club()
print("Most successful club:", most_successful.name)
