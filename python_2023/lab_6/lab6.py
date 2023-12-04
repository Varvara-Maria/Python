import sqlite3

# Підключення до бази даних або створення її, якщо не існує
conn = sqlite3.connect("football_clubs.db")
cursor = conn.cursor()

# Створення таблиці для футбольних клубів
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clubs (
        id INTEGER PRIMARY KEY,
        name TEXT,
        country TEXT,
        foundation_year INTEGER,
        president_name TEXT,
        annual_budget REAL,
        trophies_won INTEGER
    )
''')

# Збереження змін до бази даних
conn.commit()

# Додавання даних про клуби
clubs_data = [
    ("Real Madrid", "Spain", 1902, "Florentino Perez", 750000000, 97),
    ("FC Barcelona", "Spain", 1899, "Joan Laporta", 800000000, 91),
    ("Manchester United", "England", 1878, "Richard Arnold", 650000000, 66),
]

for club in clubs_data:
    cursor.execute('''
        INSERT INTO clubs (name, country, foundation_year, president_name, annual_budget, trophies_won)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', club)

conn.commit()

# Задача 1: Обчислення загального бюджету клубів для заданої країни (наприклад, "Spain")
country = "Spain"
cursor.execute('''
    SELECT SUM(annual_budget) 
    FROM clubs
    WHERE country = ?
''', (country,))
total_budget = cursor.fetchone()[0]
print(f"Загальний бюджет клубів у {country}: {total_budget} грн")

# Задача 2: Знайдення клубу, що виграв найбільше трофеїв
cursor.execute('''
    SELECT name
    FROM clubs
    ORDER BY trophies_won DESC
    LIMIT 1
''')
most_successful_club = cursor.fetchone()[0]
print(f"Клуб, що виграв найбільше трофеїв: {most_successful_club}")

# Закриття підключення до бази даних
conn.close()


#include <iostream>
#include <fstream>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

using namespace std;

void createFileAndRename() {
    // Відкриваємо файл для запису
    int fd = open("data.txt", O_CREAT | O_WRONLY, S_IRUSR | S_IWUSR);

    if (fd == -1) {
        cerr << "Error creating file." << endl;
        return;
    }

    // Закриваємо файл
    close(fd);

    // Затримка перед перейменуванням
    sleep(2);

    // Перейменовуємо файл
    if (rename("data.txt", "mydata.txt") != 0) {
        cerr << "Error renaming file." << endl;
        return;
    }

    // Задаємо права доступу тільки для власника
    if (chmod("mydata.txt", S_IRUSR | S_IWUSR) != 0) {
        cerr << "Error changing file permissions." << endl;
        return;
    }

    cout << "File created, renamed, and permissions set." << endl;
}

int main() {
    cout << "Process ID: " << getpid() << endl;
    cout << "Parent Process ID: " << getppid() << endl;
    cout << "Start of the program." << endl;

    createFileAndRename();

    cout << "End of the program." << endl;

    return 0;
}

