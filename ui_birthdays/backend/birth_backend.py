from ui_birthdays.backend.birthdays import data_birthdays
from ui_birthdays.backend.holidays import data_holidays


def birth_info_output(birth_info):
    """Insert data to Birthday table when button was clicked"""

    birth_info.setText("")
    data = data_birthdays()
    if len(data[1]):
        birth_info.insertPlainText("These people are celebrating their birthday today:\n")
        for i in data[1]:
            birth_info.insertPlainText(f"{i} and turns {data[1][i]}\n")
        birth_info.insertPlainText("\n")
    if len(data[0]):
        birth_info.insertPlainText("These people are celebrating their birthday soon:\n")
        for name, day_years in data[0].items():
            if len(day_years) == 2:
                # output all people who has day and year of birth
                birth_info.insertPlainText(
                    f"{name} celebrates his birthday in {day_years[0]} days and turns {day_years[1]}.\n")
            else:
                # output all people who has only year of birth
                birth_info.insertPlainText(f"{name} celebrates his birthday in {day_years[0]} days.\n")
        birth_info.insertPlainText("\n")
    else:
        birth_info.insertPlainText("Unfortunately, nobody is celebrating their birthday anytime soon.")


def holidays_info_output(holidays_info):
    """Insert data to Holiday table when button was clicked"""

    holidays_info.setText("")
    data = data_holidays()
    if len(data[1]):
        holidays_info.insertPlainText(f"This holiday is celebrated today: {' '.join(i for i in data[1][0])}.")
        holidays_info.insertPlainText("\n")
    if len(data[0]):
        holidays_info.insertPlainText("These holidays are coming soon:\n")
        for birthday in data[0]:
            holidays_info.insertPlainText(f"{' '.join(i for i in birthday[0])} will come in {birthday[1]} days.")
        holidays_info.insertPlainText("\n")
    else:
        holidays_info.insertPlainText("No celebrations in the near future.")
