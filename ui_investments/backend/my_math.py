from array import array


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


def current(current_price):
    return num(current_price)


def staked(staked_value):
    return num(staked_value)


def earn(current_price, staked_value):
    return num(current_price * staked_value)


def total(total_value):
    return num(total_value)


def average(avg_price):
    return num(avg_price)


def cap(total_value, current_price):
    return num(total_value * current_price)


def pnl(current_price, avg_price):
    return num((current_price - avg_price) / avg_price * 100)


def pnle(current_price, average_price4_pnl, avg_price):
    return num((current_price - average_price4_pnl) / avg_price * 100)


def total_value_crypto(data, staking, database):
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


def average_price(data, staked_value):
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

    avg_price_4_pnl = hard_formula / (all_volume + staked_value)

    return avg_price, avg_price_4_pnl


def path_photo(path_to_photo, crypto):
    return f"{path_to_photo}{crypto.replace('_', ' ').upper()}.png"
