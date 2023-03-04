from MySQLdb import connect


with open("ui_investments\\database.txt", "r", encoding="utf-8") as data:
    lines = data.readlines()


host = lines[0].strip()
user = lines[1].strip()
password = lines[2].strip()


def select_all_databases():
    try:
        with connect(
                host=host,
                user=user,
                password=password
        ) as connection:
            with connection.cursor() as cursor:

                select_all_db = "SHOW DATABASES"
                cursor.execute(select_all_db)

                full = cursor.fetchall()

                new = [i[0] for i in full]
                new.remove('information_schema')
                new.remove('performance_schema')
                new.remove('sys')
                new.remove('mysql')
                new.remove('staking')

        return new

    except Exception:
        print("Error")

    finally:
        cursor.close()


def select_all_crypto_from_db(database):

    try:
        with connect(
                host=host,
                user=user,
                password=password,
                database=database
        ) as connection:
            with connection.cursor() as cursor:

                select_all_db = "SHOW TABLES"
                cursor.execute(select_all_db)

                full = cursor.fetchall()

                new = [i[0] for i in full]

        return new

    except Exception:
        print("Error")

    finally:
        cursor.close()


def select_all_info_about_crypto(database, crypto):

    try:
        with connect(
                host=host,
                user=user,
                password=password,
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


def select_buy_sell_info_about_crypto(database, crypto, action):

    try:
        with connect(
                host=host,
                user=user,
                password=password
        ) as connection:
            with connection.cursor() as cursor:

                cursor.execute(f"USE {database}")

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


def add_coin_full(exchange, name_coin, count, date_trade, price, b_or_s, staking):

    try:
        with connect(
                host=host,
                user=user,
                password=password
        ) as connection:
            with connection.cursor() as cursor:

                all_databases = select_all_databases()

                new_date_trade = f"{date_trade[6:10]}-{date_trade[3:5]}-{date_trade[0:2]}"

                if exchange not in all_databases:

                    create_database = f"CREATE DATABASE IF NOT EXISTS {exchange}"
                    cursor.execute(create_database)
                    connection.commit()

                use_exchange = f"USE {exchange}"

                cursor.execute(use_exchange)

                select_all_table = "SHOW TABLES"

                cursor.execute(select_all_table)

                all_tables = [coin[0] for coin in cursor.fetchall()]

                if name_coin not in all_tables:

                    create_new_coin_table = f"CREATE TABLE IF NOT EXISTS {name_coin} ("\
                                            "id INT NOT NULL AUTO_INCREMENT,"\
                                            "Name_coin VARCHAR(30)," \
                                            "b_or_s VARCHAR(1)," \
                                            "count FLOAT," \
                                            "price FLOAT," \
                                            "date_trade DATE,"\
                                            "primary key(id));"

                    cursor.execute(create_new_coin_table)
                    connection.commit()

                    insert_new_coin = f"INSERT INTO {name_coin} (Name_coin, b_or_s, count, price, date_trade)" \
                                      f"VALUES {name_coin.replace('_', '-'), b_or_s, count, price, new_date_trade}"

                    cursor.execute(insert_new_coin)
                    connection.commit()

                    if staking != "-":
                        staking = float(staking)
                        use_staking = "USE staking"
                        cursor.execute(use_staking)

                        select_staking_tables = "SHOW TABLES"
                        cursor.execute(select_staking_tables)

                        full = cursor.fetchall()

                        all_staking_tables = [i[0] for i in full]

                        if exchange not in all_staking_tables:

                            create_new_exchange_table_staking = f"CREATE TABLE IF NOT EXISTS {exchange} ("\
                                                                "id INT NOT NULL AUTO_INCREMENT,"\
                                                                "Name_coin VARCHAR(30)," \
                                                                "count FLOAT," \
                                                                "primary key(id)"\
                                                                ");"

                            cursor.execute(create_new_exchange_table_staking)
                            connection.commit()

                        insert_new_coin_staking = f"INSERT INTO {exchange} (Name_coin, count)" \
                                                  f"VALUES {name_coin.replace('_', '-'), staking};"

                        cursor.execute(insert_new_coin_staking)
                        connection.commit()

                else:

                    insert_new_coin = f"INSERT INTO {name_coin} (Name_coin, b_or_s, count, price, date_trade)" \
                                      f"VALUES {name_coin, b_or_s, count, price, new_date_trade}"

                    cursor.execute(insert_new_coin)

                    connection.commit()

    except Exception as ex:
        print(ex)

    finally:
        cursor.close()


def delete_coin_full(exchange, name_coin, crypto_id):

    try:
        with connect(
                host=host,
                user=user,
                password=password
        ) as connection:
            with connection.cursor() as cursor:

                use_exchange = f"USE {exchange}"
                cursor.execute(use_exchange)

                delete_coin = f"DELETE FROM {name_coin} WHERE id = '{int(crypto_id)}'"
                cursor.execute(delete_coin)

                connection.commit()

    except Exception as ex:
        print(ex)

    finally:
        cursor.close()


def check_staking(exchange, name_coin):

    try:
        with connect(
                host=host,
                user=user,
                password=password
        ) as connection:
            with connection.cursor() as cursor:

                use_exchange = "USE staking"
                cursor.execute(use_exchange)

                get_staking = f"SELECT count FROM {exchange} WHERE Name_coin = '{name_coin.replace('_', '-')}'"
                cursor.execute(get_staking)

                staking_value = cursor.fetchall()

        return str(staking_value[0][0])  # necessary number float

    except Exception as ex:
        print(ex)

    finally:
        cursor.close()


def change_coin_info(exchange, name_coin, id, new_price, new_count, new_action, new_staking, new_date):

    try:
        with connect(
                host=host,
                user=user,
                password=password
        ) as connection:
            with connection.cursor() as cursor:

                use_exchange = f"USE {exchange}"
                cursor.execute(use_exchange)

                if new_price != "":
                    update_price = f"UPDATE IGNORE {name_coin}  SET price = {float(new_price)} WHERE id = {int(id)}"
                    cursor.execute(update_price)

                if new_count != "":
                    update_count = f"UPDATE IGNORE {name_coin}  SET count = {float(new_count)} WHERE id = {int(id)}"
                    cursor.execute(update_count)

                if new_action != "":
                    update_action = f"UPDATE IGNORE {name_coin}  SET b_or_s = {new_action} WHERE id = {int(id)}"
                    cursor.execute(update_action)

                if new_date != "":
                    update_date = f"UPDATE IGNORE {name_coin}  SET date_trade = {new_date} WHERE id = {int(id)}"
                    cursor.execute(update_date)

                if new_staking != "":

                    use_staking = "USE staking"
                    cursor.execute(use_staking)

                    update_staking = f"UPDATE IGNORE {exchange} SET count = {float(new_staking)}" \
                                     f" WHERE Name_coin = {name_coin}"
                    cursor.execute(update_staking)

                connection.commit()

    except Exception as ex:
        print(ex)

    finally:
        cursor.close()
