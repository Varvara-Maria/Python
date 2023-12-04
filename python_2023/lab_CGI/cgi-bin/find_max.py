#!/usr/bin/env python
import cgi

# Встановлення заголовків для коректної роботи CGI
print("Content-type: text/html\n")

# Отримання даних з форми
form = cgi.FieldStorage()
num1 = float(form.getvalue("num1"))
num2 = float(form.getvalue("num2"))
num3 = float(form.getvalue("num3"))

# Знайти найбільше число
max_num = max(num1, num2, num3)

# Вивести результат
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Результат</title>
</head>
<body>
    <h1>Найбільше число:</h1>
    <p>{max_num}</p>
</body>
</html>
""")
