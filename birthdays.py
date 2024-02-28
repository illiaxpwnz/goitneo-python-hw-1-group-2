from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    today = datetime.today().date()
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    birthdays = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = datetime.strptime(user["birthday"], "%Y-%m-%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:   # якщо дн пройшов, розглядаємо наступний рік
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days <= 7:
            day_of_week = week_days[birthday_this_year.weekday()]
            if day_of_week in ["Saturday", "Sunday"]:           # якщо сб-нд, привітання на понеділок
                day_of_week = "Monday"
            birthdays[day_of_week].append(name)
    
    result = ""     # форматування результату для виводу
    for day in week_days:
        if day in birthdays:
            names = ", ".join(birthdays[day])
            result += f"{day}: {names}\n"

    return result.strip()

users = [
    {"name": "Bill Gates", "birthday": "1955-10-28"},
    {"name": "Anton Shpak", "birthday": "1996-03-03"},
    {"name": "Taras Shevchenko", "birthday": "1814-03-09"},
    {"name": "Jan Koum", "birthday": "1976-02-24"}
]

print(get_birthdays_per_week(users))
