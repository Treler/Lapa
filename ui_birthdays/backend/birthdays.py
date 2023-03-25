from datetime import datetime, date


_ = datetime.today()
system_time = date(_.year, _.month, _.day)  # the current time in user's computer

names = {}
names_today = {}
days = 15  # number of days after which the notification must be send

main_path = "D:\\Projects\\Python\\MultyProgram"


# function for sort names in database by first letter of the name
def sort_names():

    with open(f"{main_path}\\ui_birthdays\\data\\names.txt", "r", encoding="utf-8") as before:
        not_sorted = before.readlines()
        new = sorted(not_sorted, key=lambda x: x[0])

    with open(f"{main_path}\\ui_birthdays\\data\\names.txt", "w", encoding="utf-8") as after:
        for line in new:
            after.write(line)


# function of form data about all people in database
def data_birthdays():
    sort_names()

    with open(f"{main_path}\\ui_birthdays\\data\\names.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            line = line.split()

            try:
                # there are days left until the birthday
                days_left = (date(system_time.year, int(line[2][3:5]), int(line[2][0:2])) - system_time).days
                if 0 < days_left <= days:
                    names[f"{line[0]} {line[1]}"] = (days_left, system_time.year - int(line[2][6:10]))

            except ValueError:
                if 0 < days_left <= days:
                    names[f"{line[0]} {line[1]}"] = [days_left]

            if days_left == 0:
                names_today[f"{line[0]} {line[1]}"] = system_time.year - int(line[2][6:10])

    # names - tuple of names, day and how years old is
    # names_today - tuple of names and how years old is
    return names, names_today


# function for check the results, not using in main script
def output():
    all_data = data_birthdays()

    if len(all_data[1]) > 0:
        # output all people who celebrate their birthday today
        print("\nThese people are celebrating their birthday today:", *all_data[1])

    if len(all_data[0]):
        print("\nThese people are celebrating their birthday soon:")
        for name, day_years in all_data[0].items():

            if len(day_years) == 2:
                # output all people who have day and year of birth
                print(f"{name} celebrates his birthday in {day_years[0]} days and he turns {day_years[1]}")

            else:
                # output all people who have only year of birth
                print(f"{name} celebrates his birthday in {day_years[0]} days")
    else:
        print("\nUnfortunately, nobody is celebrating their birthday anytime soon.")


# output()
