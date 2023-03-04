import os
from MySQLdb import connect
from array import array
from json import dumps
from requests import get
from bs4 import BeautifulSoup


with open("ui_investments\\database.txt", "r", encoding="utf-8") as data:
    lines = data.readlines()


host = lines[0].strip()
user = lines[1].strip()
password = lines[2].strip()


def update_db():
    """should be some interesting"""

    databases = ("binance", )
    all_data = {}
    path_to_photo = "D:\\Scripts (main)\\Pictures\\Investments\\"

    for database in databases:
        try:
            with connect(
                    host=host,
                    user=user,
                    password=password,
                    database=f"{database}"
            ) as connection:
                with connection.cursor() as cursor:

                    use_database = f"USE {database};"
                    cursor.execute(use_database)

                    show_tables = "SHOW TABLES;"
                    cursor.execute(show_tables)

                    all_tables = cursor.fetchall()

                    new = staking(database)

                    all_data[database] = {}


                    for table in all_tables:
                        select = f"SELECT * FROM {table[0]}"
                        cursor.execute(select)

                        rows = cursor.fetchall()

                        cur_price = current_price(table[0])

                        try:
                            staked_value = new["staking"][rows[0][1]]

                        except KeyError:
                            staked_value = 0

                        avg_price = average_price(rows, staked_value)[0]
                        avg_price4_pnl = average_price(rows, staked_value)[1]
                        total_value = total(rows, new, database)
                        try:
                            all_data[database][table[0]] = {'Coin': table[0], 'Current': num(cur_price),
                                                            'Staked': num(staked_value), 'Earn': num(cur_price * staked_value),
                                                            'Total': num(total_value), 'Average': num(avg_price),
                                                            'Cap': num(total_value * cur_price),
                                                            'PNL': num((cur_price - avg_price) / avg_price * 100),
                                                            'PNL Earn': num((cur_price - avg_price4_pnl) / avg_price * 100),
                                                            'Path_to_photo': f"{path_to_photo}{table[0].replace('_', ' ').upper()}.png"}
                        except ZeroDivisionError:
                            all_data[database][table[0]] = {'Coin': table[0], 'Current': num(cur_price),
                                                            'Staked': num(staked_value), 'Earn': num(cur_price * staked_value),
                                                            'Total': num(total_value), 'Average': num(avg_price),
                                                            'Cap': num(total_value * cur_price),
                                                            'PNL': "-",
                                                            'PNL Earn': "-",
                                                            'Path_to_photo': f"{path_to_photo}{table[0].replace('_', ' ').upper()}.png"}

                    with open("Scripts\\Investments\\json_data.json", "w", encoding="utf-8") as f:
                        f.write(dumps(all_data, sort_keys=True, indent=4))

                connection.commit()

        except Exception as ex:
            print(ex)

        finally:
            cursor.close()


def staking(database):

    try:
        with connect(
                host=host,
                user=user,
                password=password,
                database="staking"
        ) as connection:
            with connection.cursor() as cursor:

                new = {}

                select = f"SELECT * FROM {database};"
                cursor.execute(select)
                rows = cursor.fetchall()

                if "staking" not in new:
                    new["staking"] = {}

                for row in rows:
                    if row[1] not in new["staking"]:
                        new["staking"][row[1]] = row[2]

                    else:
                        new["staking"][row[1]] += row[2]

                return new

    except Exception as ex:
        print(ex)

    finally:
        cursor.close()


def average_price(data, staked):
    values_cur_crypto = array('d', ())
    prices_cur_crypto = array('d', ())

    for row in data:
        if row[2] == "b":
            values_cur_crypto.append(row[3])
            prices_cur_crypto.append(row[4])
        elif row[2] == "e":
            return 0, 0

    all_volume = sum(i for i in values_cur_crypto)
    hard_formula = sum(values_cur_crypto[i] * prices_cur_crypto[i] for i in range(len(values_cur_crypto)))

    avg_price = hard_formula / all_volume

    avg_price_4_pnl = hard_formula / (all_volume + staked)

    return avg_price, avg_price_4_pnl


def total(data, staking, database):
    """without staking"""

    value = 0
    for row in data:
        if row[2] == "b":
            value += row[3]

        elif row[2] == "s":
            value -= row[3]

        elif row[2] == "e":
            value += row[3]

    try:
        value += staking[database][data[0][1]]

    except KeyError:
        pass

    return value


def current_price(name):
    try:
        request = get(f"https://coinmarketcap.com/currencies/{name.lower().replace('_', '-')}")

        with open("Scripts\\Investments\\crypto.html", "w", encoding="utf-8") as file:
            file.write(request.text)

        with open("Scripts\\Investments\\crypto.html", "r", encoding="utf-8") as ready_file:
            content = ready_file.read()

        soup = BeautifulSoup(content, "lxml")

        price = soup.find("div", class_="priceValue")

    except Exception as ex:
        print(ex)

    finally:
        os.remove("Scripts\\Investments\\crypto.html")

    return float(price.text[1:].replace(",", ""))


def num(number):
    res = 0
    if number >= 500:
        res = 0

    if 50 <= number < 500:
        res = 1

    elif 1 <= number < 50:
        res = 2

    elif 0.1 <= number < 1:
        res = 3

    elif 0.001 <= number < 0.1:
        res = 4

    elif 0.0001 <= number < 0.001:
        res = 6

    elif 0.00001 <= number < 0.0001:
        res = 7

    elif 0.000001 <= number < 0.00001:
        res = 8

    return f"{number:.{res}f}"


# print(staking("binance"))
# update_db()
