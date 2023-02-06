from datetime import datetime, date


_ = datetime.today()
system_time = date(_.year, _.month, _.day)

days = 15
holidays = []
today_holiday = []


def sort_holidays():

    with open("Scripts\\Birthdays\\holidays.txt", "r", encoding="utf-8") as before:
        not_sorted = before.readlines()
        new = sorted(not_sorted, key=lambda x: x[0])

    with open("Scripts\\Birthdays\\holidays.txt", "w", encoding="utf-8") as after:
        for line in new:
            after.write(line)


def data_holidays():
    sort_holidays()

    with open("Scripts\\Birthdays\\holidays.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            days_left = (date(system_time.year, int(line[-3:-1]), int(line[-6:-4])) - system_time).days

            if 0 < days_left <= days:
                holidays.append((line.split()[0:-2], days_left))

            elif days_left == 0:
                today_holiday.append(line.split()[0:-2])

    return holidays, today_holiday


# function for check the results, not using in main script
def output():
    all_holidays = data_holidays()

    if len(all_holidays[1]):
        print(f"This holiday is celebrated today:", *all_holidays[1][0])

    if len(all_holidays[0]):
        print("\nThese holidays are coming soon:")

        for holiday in all_holidays[0]:
            print(f"{' '.join(i for i in holiday[0])} will come in {holiday[1]} days")
    else:
        print("No celebrations in the near future")


# output()
