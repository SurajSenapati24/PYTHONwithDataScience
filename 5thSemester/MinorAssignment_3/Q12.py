from datetime import datetime, timedelta

def get_day_of_week(date):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[date.weekday()]

def cal_n_date_and_day(t_date, t_day, days_to_add):
    t_date = datetime.strptime(t_date, "%Y-%m-%d")
    n_date = t_date + timedelta(days=days_to_add)
    n_day = get_day_of_week(n_date)
    return n_date.strftime("%Y-%m-%d"), n_day
t_date = input("Today's date (YYYY-MM-DD): ")
t_day = input("Today's day: ")
days_to_add = int(input("Number of days: "))
n_date, n_day = cal_n_date_and_day(t_date, t_day, days_to_add)
print("New date:", n_date)
print("New day:", n_day)