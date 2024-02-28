from datetime import datetime
from birthdays import get_birthdays_this_week

def is_leap_year(year):
    """Перевіряє, чи є рік високосним."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def bot_response(command):
    if command == "1": # генерація відповіді по команді
        today = datetime.now()
        return f"Сьогодні {today.strftime('%A, %d %B %Y')}."
    elif command == "2":
        if is_leap_year(datetime.now().year):
            return "Цей рік високосний."
        else:
            return "Цей рік не високосний."
    elif command == "3":
        colleagues = [ # дні народження колег
            ("Василь Щур", "1995-03-03"),
            ("Антон Шпак", "1996-04-21"), 
            ("Тарас Шевченко", "1814-03-09"),
        ]
        birthdays = get_birthdays_this_week(colleagues)
        if birthdays:
            return "Цього тижня день народження святкує: " + ", ".join(birthdays)
        else:
            return "На цьому тижні днів народження немає."
    else:
        return "Вибачте, я не розумію команду."

def greet_user():
    """Виводить привітання користувачу."""
    print("Привіт! Я бот-асистент. Чим можу допомогти?")


greet_user()
while True: # Основний цикл асистента
    print("\nЯ можу виконати наступні команди:")
    print("1) Який сьогодні день та дата?")
    print("2) Рік високосний чи ні?")
    print("3) Чи святкують мої колеги день народження цього тижня?")
    print("q) Вийти")
    
    command = input("Введіть команду: ")
    if command == "q":
        break
    response = bot_response(command)
    print(response)
