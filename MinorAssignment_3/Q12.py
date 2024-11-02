from datetime import datetime, timedelta

def get_day_of_week(date):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[date.weekday()]

def calculate_new_date_and_day(today_date, today_day, days_to_add):
    today_date = datetime.strptime(today_date, "%Y-%m-%d")
    new_date = today_date + timedelta(days=days_to_add)
    new_day = get_day_of_week(new_date)
    return new_date.strftime("%Y-%m-%d"), new_day
today_date = input("Today's date (YYYY-MM-DD): ")
today_day = input("Today's day: ")
days_to_add = int(input("Number of days: "))
new_date, new_day = calculate_new_date_and_day(today_date, today_day, days_to_add)
print("New date:", new_date)
print("New day:", new_day)