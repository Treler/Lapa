from json import loads
from json import dumps
from psycopg2 import connect
from requests import Session
from ui_investments.backend.sql import select_all_crypto_from_db, staking_values
from ui_investments.backend.my_math import current, staked, earn, total, average, cap, pnl, pnle,\
                                           total_value_crypto, average_price, path_photo

main_path = "D:\\Projects\\Python\\MultyProgram"

with open(f"{main_path}\\ui_investments\\data\\db_credentials.txt", "r", encoding="utf-8") as data:
    lines = data.readlines()

user = lines[0].strip()
password = lines[1].strip()
host = lines[2].strip()
port = lines[3].strip()
trash_db = lines[4].strip()

with open(f"{main_path}\\ui_investments\\data\\all_databases.txt", "r", encoding="utf-8") as all_db:
    databases = all_db.readlines()

all_databases = [database.strip() for database in databases]


def update_db():
    """should be some interesting"""

    all_data = {}

    for database in all_databases:

        all_cryptos = select_all_crypto_from_db(database)

        staking = staking_values(database)

        all_data[database] = {}

        all_params_4every_crypto_to_json(database, all_cryptos, staking, all_data)


def current_price(cryptos):

    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    parameters = {
        "slug": ",".join(i for i in cryptos),
        "convert": "USD"
    }

    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": "602b5e84-4094-4134-91bc-9b302e8cf1aa"
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)

    answer = response.text
    id_cryptos = loads(answer)["data"]
    new = []
    for crypto in id_cryptos:
        new.append(loads(answer)["data"][crypto]["quote"]["USD"]["price"])

    return new


def all_params_4every_crypto_to_json(exchange, all_cryptos, staking, all_data):

    path_to_photo = "D:\\Scripts (main)\\pictures\\investments\\coins\\"

    try:
        with connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=exchange
        ) as connection:
            with connection.cursor() as cursor:

                cur_prices = current_price(all_cryptos)
                i = 0

                for crypto in all_cryptos:
                    cur_price = cur_prices[i]
                    select = f"SELECT * FROM {crypto}"
                    cursor.execute(select)

                    all_crypto_actions = cursor.fetchall()

                    try:
                        staked_value = staking["staking"][all_crypto_actions[0][1]]

                    except KeyError:
                        staked_value = 0

                    avg = average_price(all_crypto_actions, staked_value)
                    avg_price = avg[0]
                    avg_price4_pnl = avg[1]

                    total_value = total_value_crypto(all_crypto_actions, staking, exchange)

                    try:
                        all_data[exchange][crypto] = {'Coin': crypto, 'Current': current(cur_price),
                                                      'Staked': staked(staked_value), 'Earn': earn(cur_price, staked_value),
                                                      'Total': total(total_value), 'Average': average(avg_price),
                                                      'Cap': cap(total_value, cur_price),
                                                      'PNL': pnl(cur_price, avg_price),
                                                      'PNL Earn': pnle(cur_price, avg_price4_pnl, avg_price),
                                                      'Path_to_photo': path_photo(path_to_photo, crypto)}
                    except ZeroDivisionError:
                        all_data[exchange][crypto] = {'Coin': crypto, 'Current': current(cur_price),
                                                      'Staked': staked(staked_value), 'Earn': earn(cur_price, staked_value),
                                                      'Total': total(total_value), 'Average': average(avg_price),
                                                      'Cap': cap(total_value, cur_price),
                                                      'PNL': "-",
                                                      'PNL Earn': "-",
                                                      'Path_to_photo': path_photo(path_to_photo, crypto)}
                    i += 1

    except Exception as ex:
        print(ex)

    finally:
        cursor.close()
        connection.close()

    with open(f"{main_path}\\ui_investments\\data\\inv_money_data.json", "w", encoding="utf-8") as f:
        f.write(dumps(all_data, sort_keys=True, indent=4))


update_db()
