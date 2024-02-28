from datetime import datetime

def get_birthdays_this_week(colleagues):
    today = datetime.now()     # Отримання поточного тижня року
    current_week = today.isocalendar()[1]

    birthdays_this_week = [     # Фільтрація колег, дні народження яких випадають на поточний тиждень
        name for name, birthday_str in colleagues
        if datetime.strptime(birthday_str, "%Y-%m-%d").replace(year=today.year).isocalendar()[1] == current_week
    ]
    
    return birthdays_this_week

colleagues = [ # Приклад списку колег
    ("Василь Щур", "1995-03-03"),
    ("Антон Шпак", "1996-04-21"), 
    ("Тарас Шевченко", "1814-03-09"),
]

birthdays_this_week = get_birthdays_this_week(colleagues)
print(birthdays_this_week)