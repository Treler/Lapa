from json import load, loads
from random import choice
from ui_investments.frontend.loop_diagram import Data
from PyQt5.QtGui import QStandardItem, QImage
from PyQt5.QtCore import QSortFilterProxyModel, Qt


def create_loop_diagram(exchange=""):
    data = []

    with open('ui_investments\\data\\loop_digram_colors.txt') as d:
        lines = d.readlines()

    with open('ui_investments\\data\\inv_money_data.json') as f:
        templates = load(f)

    for coin_name in templates[exchange]:
        data.append(Data(coin_name, float(templates[exchange][coin_name]['Cap']), choice(lines).strip()))

    return data


def insert_data_to_all_tables(model, table):
    model.clear()
    heads = ("Coin", "Name", "Current price", "Staked", "Earn", "Total",
                     "Avg purchase price", "Cap", "PNL (B/S)", "PNLE (B/S/E)")
    model.setHorizontalHeaderLabels(heads)

    databases = ("binance", )
    with open("ui_investments\\data\\inv_money_data.json", "r", encoding="utf-8") as f1:
        all_data = loads(f1.read())

    for database in databases:
        for coin in all_data[database]:
            coin_name = all_data[database][coin]['Coin'].replace("_", " ").title()
            coin_cur_price = "$" + str(all_data[database][coin]['Current'])
            coin_staked = str(all_data[database][coin]['Staked'])
            coin_earn = "$" + all_data[database][coin]['Earn']
            coin_total = str(all_data[database][coin]['Total'])
            coin_avg_price = "$" + str(all_data[database][coin]['Average'])
            coin_cap = "$" + str(all_data[database][coin]['Cap'])
            coin_pnl = all_data[database][coin]['PNL'] + "%"
            coin_pnl_staked = all_data[database][coin]['PNL Earn'] + "%"

            model.appendRow([ItemImage("", f"Pictures\\Investments\\Coins\\{coin.upper().replace('_', ' ')}.png"),
                             QStandardItem(coin_name),
                             QStandardItem(coin_cur_price),
                             QStandardItem(coin_staked),
                             QStandardItem(coin_earn),
                             QStandardItem(coin_total),
                             QStandardItem(coin_avg_price),
                             QStandardItem(coin_cap),
                             QStandardItem(coin_pnl),
                             QStandardItem(coin_pnl_staked),
                             ])

    table.resizeColumnsToContents()
    table.resizeRowsToContents()


class ItemImage(QStandardItem):
    def __init__(self, txt, image_path):
        super().__init__()

        self.setEditable(False)
        self.setText(txt)

        if image_path:
            image = QImage(image_path)
            self.setData(image, Qt.DecorationRole)


class NumberSortModel(QSortFilterProxyModel):

    def lessThan(self, left_index, right_index) -> bool:

        left_var: str = left_index.data(Qt.EditRole)
        right_var: str = right_index.data(Qt.EditRole)

        try:
            return float(left_var.replace("$", "")) < float(right_var.replace("$", ""))

        except (ValueError, TypeError, AttributeError):
            pass

        try:
            return left_var < right_var

        except TypeError:  # in case of NoneType
            return True
