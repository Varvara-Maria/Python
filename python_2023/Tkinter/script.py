import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Калькулятор")

        # Створення інтерфейсних елементів
        self.label1 = tk.Label(master, text="Введіть перше число:")
        self.label2 = tk.Label(master, text="Введіть друге число:")
        self.label3 = tk.Label(master, text="Введіть третє число:")

        self.entry1 = tk.Entry(master)
        self.entry2 = tk.Entry(master)
        self.entry3 = tk.Entry(master)

        self.label1.grid(row=0, column=0)
        self.label2.grid(row=1, column=0)
        self.label3.grid(row=2, column=0)

        self.entry1.grid(row=0, column=1)
        self.entry2.grid(row=1, column=1)
        self.entry3.grid(row=2, column=1)

        self.max_button = tk.Button(master, text="Знайти найбільше", command=self.find_max)
        self.min_button = tk.Button(master, text="Знайти найменше", command=self.find_min)

        self.max_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.min_button.grid(row=4, column=0, columnspan=2, pady=10)

    def find_max(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            num3 = float(self.entry3.get())
            result = max(num1, num2, num3)
            messagebox.showinfo("Результат", f"Найбільше число: {result}")
        except ValueError:
            messagebox.showerror("Помилка", "Будь ласка, введіть коректні числа.")

    def find_min(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            num3 = float(self.entry3.get())
            result = min(num1, num2, num3)
            messagebox.showinfo("Результат", f"Найменше число: {result}")
        except ValueError:
            messagebox.showerror("Помилка", "Будь ласка, введіть коректні числа.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
