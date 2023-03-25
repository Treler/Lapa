from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

main_path = "D:\\Projects\\Python\\MultyProgram"

with open(f"{main_path}\\ui_investments\\data\\db_credentials.txt", "r", encoding="utf-8") as data:
    lines = data.readlines()


user = lines[0].strip()
password = lines[1].strip()
host = lines[2].strip()
port = lines[3].strip()
trash_db = lines[4].strip()


def select_all_databases():
    try:
        with connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=trash_db
        ) as connection:
            with connection.cursor() as cursor:

                select_all_db = "SELECT datname FROM pg_database"
                cursor.execute(select_all_db)

                full = cursor.fetchall()

                new = [i[0] for i in full]
                new.remove("template0")
                new.remove("template1")
                new.remove("trash")
                new.remove("staking")

        return new

    except Exception as error:
        print(error)

    finally:
        cursor.close()
        connection.close()


def select_all_crypto_from_db(database):

    try:
        with connect(
                host=host,
                user=user,
                password=password,
                database=database
        ) as connection:
            with connection.cursor() as cursor:

                select_all_tables = f"SELECT tablename FROM pg_tables WHERE schemaname = 'public'"

                cursor.execute(select_all_tables)

                full = cursor.fetchall()

                new = [i[0] for i in full]

        return new

    except Exception:
        print("Error")

    finally:
        cursor.close()
        connection.close()


def select_all_info_about_crypto(database, crypto):

    try:
        with connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=database
        ) as connection:
            with connection.cursor() as cursor:

                select_all_db = f"SELECT * FROM {crypto}"
                cursor.execute(select_all_db)

                full = cursor.fetchall()

        return full

    except Exception:
        print('error')

    finally:
        cursor.close()
        connection.close()


def select_buy_sell_info_about_crypto(database, crypto, action):

    try:
        with connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=database
        ) as connection:
            with connection.cursor() as cursor:

                if action == "all":
                    select_all_db = f"SELECT * FROM {crypto}"

                else:
                    select_all_db = f"SELECT * FROM {crypto} WHERE b_or_s = '{action[0]}'"

                cursor.execute(select_all_db)

                full = cursor.fetchall()

        return full

    except Exception:
        print('error')

    finally:
        cursor.close()
        connection.close()


def add_staking(exchange, name_coin, staking):

    try:
        with connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database='staking'
        ) as connection:
            with connection.cursor() as cursor:

                if staking != "-" and staking != "":
                    staking = float(staking)

                    cursor.execute(f"SELECT tablename FROM pg_tables WHERE tablename = '{exchange}'")
                    exists = cursor.fetchone()
                    if not exists:
                        create_new_exchange_table_staking = f"CREATE TABLE IF NOT EXISTS {exchange} (" \
                                                            "id SERIAL PRIMARY KEY NOT NULL," \
                                                            "Name_coin VARCHAR(30)," \
                                                            "count FLOAT)"

                        cursor.execute(create_new_exchange_table_staking)

                    cursor.execute(f"SELECT name_coin FROM {exchange} WHERE name_coin = '{name_coin}'")
                    exists = cursor.fetchone()
                    if not exists:
                        insert_new_coin_staking = f"INSERT INTO {exchange} (name_coin, count)" \
                                                  f"VALUES {name_coin.replace('_', '-'), staking}"

                        cursor.execute(insert_new_coin_staking)

    except Exception as ex:
        print(ex)

    finally:
        cursor.close()
        connection.close()


def add_coin_full(exchange, name_coin, count, date_trade, price, b_or_s, staking):

    # this realization for operator 'with' (in psycopg2 some with TRANSACTION - check docs)
    creds = {
            'user': user,
            'password': password,
            'host': host,
            'port': port,
            'database': exchange
            }

    try:
        connection = connect(**creds)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        with connection.cursor() as cursor:

            new_date_trade = f"{date_trade[6:10]}-{date_trade[3:5]}-{date_trade[0:2]}"

            cursor.execute(f"SELECT datname FROM pg_database WHERE datname = '{exchange}'")
            exists = cursor.fetchone()
            if not exists:
                cursor.execute(f"CREATE DATABASE {exchange}")

            cursor.execute(f"SELECT tablename FROM pg_tables WHERE tablename = '{name_coin}'")
            exists = cursor.fetchone()
            if not exists:

                create_new_coin_table = f"CREATE TABLE {name_coin} ("\
                                        "id SERIAL PRIMARY KEY NOT NULL,"\
                                        "Name_coin VARCHAR(30)," \
                                        "b_or_s VARCHAR(1)," \
                                        "count FLOAT," \
                                        "price FLOAT," \
                                        "date_trade DATE);"

                cursor.execute(create_new_coin_table)

                insert_new_coin = f"INSERT INTO {name_coin} (Name_coin, b_or_s, count, price, date_trade)" \
                                  f"VALUES {name_coin.replace('_', '-'), b_or_s, count, price, new_date_trade}"

                cursor.execute(insert_new_coin)

            else:

                insert_new_coin = f"INSERT INTO {name_coin} (Name_coin, b_or_s, count, price, date_trade)" \
                                  f"VALUES {name_coin, b_or_s, count, price, new_date_trade}"

                cursor.execute(insert_new_coin)

            add_staking(exchange, name_coin, staking)

    except Exception as ex:
        print(ex)

    finally:
        cursor.close()
        connection.close()


def delete_coin_full(exchange, name_coin, crypto_id):

    try:
        with connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=exchange
        ) as connection:
            with connection.cursor() as cursor:

                delete_coin = f"DELETE FROM {name_coin} WHERE id = '{int(crypto_id)}'"
                cursor.execute(delete_coin)

                connection.commit()

    except Exception as ex:
        print(ex)

    finally:
        cursor.close()
        connection.close()


def check_staking(exchange, name_coin):

    try:
        with connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database="staking"
        ) as connection:
            with connection.cursor() as cursor:

                get_staking = f"SELECT count FROM {exchange} WHERE name_coin = '{name_coin.replace('_', '-')}'"
                cursor.execute(get_staking)

                staking_value = cursor.fetchall()

        return str(staking_value[0][0])  # necessary number float

    except Exception as ex:
        print(ex)

    finally:
        cursor.close()
        connection.close()


def update_staking(exchange, name_coin, new_staking):
    try:
        with connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database="staking"
        ) as connection:
            with connection.cursor() as cursor:

                upd_staking = f"UPDATE {exchange} SET count = {float(new_staking)}" \
                                 f" WHERE name_coin = '{name_coin}'"
                cursor.execute(upd_staking)

    except Exception as ex:
        print(ex)

    finally:
        cursor.close()
        connection.close()


def change_coin_info(exchange, name_coin, id, new_price, new_count, new_action, new_staking, new_date):

    try:
        with connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database=exchange
        ) as connection:
            with connection.cursor() as cursor:

                if new_price != "":
                    update_price = f"UPDATE {name_coin}  SET price = {float(new_price)} WHERE id = {int(id)}"
                    cursor.execute(update_price)

                if new_count != "":
                    update_count = f"UPDATE {name_coin}  SET count = {float(new_count)} WHERE id = {int(id)}"
                    cursor.execute(update_count)

                if new_action != "":
                    update_action = f"UPDATE {name_coin}  SET b_or_s = '{new_action}' WHERE id = {int(id)}"
                    cursor.execute(update_action)

                if new_date != "":
                    update_date = f"UPDATE {name_coin}  SET date_trade = {new_date} WHERE id = {int(id)}"
                    cursor.execute(update_date)

                if new_staking != "":

                    update_staking(exchange, name_coin, new_staking)

                connection.commit()

    except Exception as ex:
        print(ex)

    finally:
        cursor.close()
        connection.close()


def staking_values(exchange):

    try:
        with connect(
                user=user,
                password=password,
                host=host,
                port=port,
                database="staking"
        ) as connection:
            with connection.cursor() as cursor:

                new = {}

                select = f"SELECT * FROM {exchange}"
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
        connection.close()

# print(select_all_databases())
# print(select_all_crypto_from_db("binance"))
# print(select_all_info_about_crypto("binance", "bitcoin"))
# print(select_buy_sell_info_about_crypto("binance", "bitcoin", "s"))
# add_coin_full(exchange, name_coin, count, date_trade, price, b_or_s, staking)
# add_coin_full("binance", "bitcoin", 5, "24.03.2023", 15, 'b', 0.4)
# delete_coin_full("binance", "bitcoin", 9)
# print(check_staking("binance", "solana"))
# change_coin_info(exchange, name_coin, id, new_price, new_count, new_action, new_staking, new_date)
# change_coin_info("binance", "bitcoin", 1, 15000, 0.1, "b", 0.1, "")
