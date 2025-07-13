import datetime

def birthday_countdown():
    print("\n" + "Birthday Countdown 🎂".center(50, "*"))
    birthday = input("Enter birthday (YYYY-MM-DD): ")
    today = datetime.date.today()
    bday = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
    days_left = (bday - today).days
    if days_left > 0:
        print(f"{days_left} days left until your birthday!")
    elif days_left == 0:
        print("🎉 Happy Birthday!")
    else:
        print("This birthday has already passed this year.")
