from PyQt5.QtWidgets import QWidget, QGridLayout, QTabWidget, QTableView, QPushButton, QLabel, QDialog, QLineEdit, \
                            QComboBox, QDateEdit
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
from ui_investments.frontend.loop_diagram import Example
from ui_investments.backend.inv_backend import insert_data_to_all_tables, create_loop_diagram, NumberSortModel
from ui_profile.frontend.animated_toggle import AnimatedToggle
from ui_investments.backend.sql import select_all_databases, select_all_crypto_from_db, select_all_info_about_crypto, \
                                   select_buy_sell_info_about_crypto, add_coin_full, delete_coin_full, check_staking, \
                                   change_coin_info
from ui_investments.backend.db_to_json import update_db


class Investments(QWidget):

    # function of cryptocurrencies, usd and eur widget
    def currencies_widget_window(self):

        update_db()
        self.currenc_widget = QWidget()
        self.currenc_grid = QGridLayout(self.currenc_widget)
        self.currenc_widget.setStyleSheet("background-color: rgb(140, 140, 140)")

        self.currenc_tab_widget = QTabWidget()
        self.tab_total = QWidget()
        self.tab_binance = QWidget()
        self.tab_raydium = QWidget()
        self.tab_pancake = QWidget()
        self.tab_xdrado = QWidget()

        self.counter_exc = 0
        self.counter_crypto = 0

        self.currenc_tab_widget.addTab(self.tab_total, "Total")
        self.currenc_tab_widget.addTab(self.tab_binance, "Binance")
        self.currenc_tab_widget.addTab(self.tab_raydium, "Pancakeswap")
        self.currenc_tab_widget.addTab(self.tab_pancake, "Biswap")

        # -------------------------- TOTAL -------------------------- #
        Investments.total_tab_grid_setting(self)
        Investments.total_tab_buttons(self)



        Investments.total_tab_add_window(self)
        Investments.total_tab_delete_window(self)
        Investments.total_tab_change_window(self)

        Investments.actions_for_crypto_db_buttons(self)


        self.tab_total.setStyleSheet("background-color: rgb(170, 170, 170)")
        # ----------------------------------------------------------- #

        # ------------------------- BINANCE ------------------------- #
        Investments.binance_tab_grid_settings(self)
        self.tab_binance.setStyleSheet("background-color: rgb(200, 200, 200)")

        self.binance_item_model = QStandardItemModel(self)
        self.binance_table_view = QTableView(self)


        Investments.table_for_all_initialize(self, self.binance_item_model, self.binance_table_view,
                                             self.binance_tab_grid, 0,
                                             0, 0, 0, 5)

        insert_data_to_all_tables(self.binance_item_model, self.binance_table_view)

        binance_diagram = Example(create_loop_diagram('binance'))
        self.binance_tab_grid.addWidget(binance_diagram.chart_view, 0, 5, 0, 4)
        # ----------------------------------------------------------- #

        # ------------------------- SQL ------------------------- #

        Investments.add_window_init(self)
        Investments.delete_window_init(self)
        Investments.change_window_init(self)

        Investments.actions_for_add_crypto_window(self)
        Investments.actions_for_delete_crypto_window(self)
        Investments.actions_for_change_crypto_window(self)

        # ------------------------------------------------------- #


        self.currenc_grid.addWidget(self.currenc_tab_widget, 0, 0, 2, 2)

    def table_for_all_initialize(self, item_model, table_view, grid, param, r, c, cr, cc):
        # убрать в бекенд

        if param == 0:
            heads = ("Coin", "Name", "Current price", "Staked", "Earn", "Total",
                     "Avg purchase price", "Cap", "PNL (B/S)", "PNLE (B/S/E)")

        elif param == 1:
            heads = ("Name", "B/S", "Count", "Price", "Date")

        elif param == 2:
            heads = ("ID", "Name", "B/S", "Count", "Price", "Date")

        else:
            heads = ("Name", )

        item_model.setHorizontalHeaderLabels(heads)
        w_proxy = NumberSortModel(self)
        w_proxy.setSourceModel(item_model)
        table_view.setModel(w_proxy)
        table_view.setSortingEnabled(True)

        table_view.setFont(QFont("Times", 12))

        grid.addWidget(table_view, r, c, cr, cc)


    def total_tab_delete_window(self):

        self.delete_dialog_window = QDialog()
        self.delete_dialog_window.resize(1200, 600)
        self.delete_dialog_window.setWindowTitle("Delete window")

        Investments.total_tab_delete_window_grid_settings(self)

        self.total_delete_tab_item_model = QStandardItemModel(self)
        self.total_delete_tab_table_view = QTableView(self)

        self.total_delete_tab_item_model = QStandardItemModel(self)
        self.total_delete_tab_table_view = QTableView(self)

        self.delete_exchange_label = QLabel("Exchange")
        self.delete_exchange_combo = QComboBox()

        self.delete_cryptocur_label = QLabel("Cryptocurrency")
        self.delete_cryptocur_combo = QComboBox()

        self.delete_buy_sell_label = QLabel("All/buy/sell")
        self.delete_buy_sell_combo = QComboBox()

        self.delete_id_label = QLabel("ID")
        self.delete_id_edit = QLineEdit()

        self.delete_show_button = QPushButton("Show")
        self.delete_show_button.setMaximumWidth(40)

        self.delete_all_button = QPushButton("Delete")
        self.delete_cancel_button = QPushButton("Cancel")

        self.dateEdit = QDateEdit(calendarPopup=True)

        self.total_tab_delete_window_grid.addWidget(self.delete_exchange_label, 0, 1, 1, 1, alignment=Qt.AlignBottom)
        self.total_tab_delete_window_grid.addWidget(self.delete_exchange_combo, 1, 1, 1, 1)

        self.total_tab_delete_window_grid.addWidget(self.delete_cryptocur_label, 2, 1, 1, 1, alignment=Qt.AlignBottom)
        self.total_tab_delete_window_grid.addWidget(self.delete_cryptocur_combo, 3, 1, 1, 1)

        self.total_tab_delete_window_grid.addWidget(self.delete_buy_sell_label, 4, 1, 1, 1, alignment=Qt.AlignBottom)
        self.total_tab_delete_window_grid.addWidget(self.delete_buy_sell_combo, 5, 1, 1, 1)

        self.total_tab_delete_window_grid.addWidget(self.delete_id_label, 0, 3, 1, 1, alignment=Qt.AlignBottom)
        self.total_tab_delete_window_grid.addWidget(self.delete_id_edit, 1, 3, 1, 1)

        self.total_tab_delete_window_grid.addWidget(self.delete_all_button, 8, 3, 1, 2)
        self.total_tab_delete_window_grid.addWidget(self.delete_cancel_button, 8, 5, 1, 2)

        self.total_tab_delete_window_grid.addWidget(self.dateEdit, 8, 7, 1, 2)

        self.total_tab_delete_window_grid.addWidget(self.delete_show_button, 6, 1, 1, 1, alignment=Qt.AlignTop | Qt.AlignCenter)



    def total_tab_add_window(self):

        self.add_dialog_window = QDialog()
        self.add_dialog_window.resize(1200, 600)
        self.add_dialog_window.setWindowTitle("Add window")

        Investments.total_tab_add_window_grid_settings(self)

        self.total_add_tab_item_model = QStandardItemModel(self)
        self.total_add_tab_table_view = QTableView(self)

        self.add_exchange_label = QLabel("Exchange")
        self.add_exchange_combo = QComboBox()
        self.add_exchange_edit = QLineEdit()
        self.add_exchange_edit.hide()
        self.add_exchange_toggle = AnimatedToggle()

        self.add_cryptocur_label = QLabel("Cryptocurrency")
        self.add_cryptocur_combo = QComboBox()
        self.add_cryptocur_edit = QLineEdit()
        self.add_cryptocur_edit.hide()
        self.add_cryptocur_toggle = AnimatedToggle()

        self.add_buy_sell_label = QLabel("All/buy/sell")
        self.add_buy_sell_combo = QComboBox()

        self.add_price_label = QLabel("Price")
        self.add_price_edit = QLineEdit()

        self.add_value_label = QLabel("Value")
        self.add_value_edit = QLineEdit()

        self.add_staking_label = QLabel("Staking")
        self.add_staking_edit = QLineEdit()

        self.add_date_label = QLabel("Date")
        self.add_date_edit = QLineEdit()

        self.add_show_button = QPushButton("Show")
        self.add_show_button.setMaximumWidth(40)

        self.add_all_button = QPushButton("Add")
        self.add_cancel_button = QPushButton("Cancel")


        self.total_tab_add_window_grid.addWidget(self.add_exchange_label, 0, 1, 1, 1, alignment=Qt.AlignBottom)
        self.total_tab_add_window_grid.addWidget(self.add_exchange_combo, 1, 1, 1, 1)
        self.total_tab_add_window_grid.addWidget(self.add_exchange_edit, 1, 1, 1, 1)


        self.total_tab_add_window_grid.addWidget(self.add_exchange_toggle, 1, 2, 1, 1, alignment=Qt.AlignLeft)


        self.total_tab_add_window_grid.addWidget(self.add_cryptocur_label, 2, 1, 1, 1, alignment=Qt.AlignBottom)
        self.total_tab_add_window_grid.addWidget(self.add_cryptocur_combo, 3, 1, 1, 1)
        self.total_tab_add_window_grid.addWidget(self.add_cryptocur_edit, 3, 1, 1, 1)
        self.total_tab_add_window_grid.addWidget(self.add_cryptocur_toggle, 3, 2, 1, 1, alignment=Qt.AlignLeft)


        self.total_tab_add_window_grid.addWidget(self.add_buy_sell_label, 4, 1, 1, 1, alignment=Qt.AlignBottom)
        self.total_tab_add_window_grid.addWidget(self.add_buy_sell_combo, 5, 1, 1, 1)

        self.total_tab_add_window_grid.addWidget(self.add_show_button, 6, 1, 1, 1, alignment=Qt.AlignTop | Qt.AlignCenter)



        self.total_tab_add_window_grid.addWidget(self.add_price_label, 0, 3, 1, 1, alignment=Qt.AlignBottom)
        self.total_tab_add_window_grid.addWidget(self.add_price_edit, 1, 3, 1, 1)

        self.total_tab_add_window_grid.addWidget(self.add_value_label, 0, 5, 1, 1, alignment=Qt.AlignBottom)
        self.total_tab_add_window_grid.addWidget(self.add_value_edit, 1, 5, 1, 1)

        self.total_tab_add_window_grid.addWidget(self.add_staking_label,    2, 3, 1, 1, alignment=Qt.AlignBottom)
        self.total_tab_add_window_grid.addWidget(self.add_staking_edit, 3, 3, 1, 1)

        self.total_tab_add_window_grid.addWidget(self.add_date_label, 2, 5, 1, 1, alignment=Qt.AlignBottom)
        self.total_tab_add_window_grid.addWidget(self.add_date_edit, 3, 5, 1, 1)



        self.total_tab_add_window_grid.addWidget(self.add_all_button, 8, 3, 1, 2)
        self.total_tab_add_window_grid.addWidget(self.add_cancel_button, 8, 5, 1, 2)


    def total_tab_change_window(self):

        self.change_dialog_window = QDialog()
        self.change_dialog_window.resize(1200, 600)
        self.change_dialog_window.setWindowTitle("Change window")

        Investments.total_tab_change_window_grid_settings(self)

        self.total_change_tab_item_model = QStandardItemModel(self)
        self.total_change_tab_table_view = QTableView(self)

        self.change_exchange_label = QLabel("Exchange")
        self.change_exchange_combo = QComboBox()

        self.change_cryptocur_label = QLabel("Cryptocurrency")
        self.change_cryptocur_combo = QComboBox()

        self.change_buy_sell_label = QLabel("All/buy/sell")
        self.change_buy_sell_combo = QComboBox()
        self.change_buy_sell_combo.addItems(["", "all", "buy", "sell"])
        ch_bs_combo_model = self.change_buy_sell_combo.model()
        ch_bs_combo_model.item(0).setEnabled(False)

        self.change_id_label = QLabel("ID")
        self.change_id_edit = QLineEdit()

        self.change_price_label = QLabel("New price")
        self.change_price_edit = QLineEdit()

        self.change_value_label = QLabel("New value")
        self.change_value_edit = QLineEdit()

        self.change_new_staking_label = QLabel("New staking")
        self.change_new_staking_edit = QLineEdit()

        self.change_old_staking_label = QLabel("Old staking")
        self.change_old_staking_edit = QLineEdit()
        self.change_old_staking_edit.setEnabled(False)

        self.change_date_label = QLabel("New date")
        self.change_date_edit = QLineEdit()

        self.change_action_label = QLabel("New action")
        self.change_action_edit = QLineEdit()

        self.change_show_button = QPushButton("Show")
        self.change_show_button.setMaximumWidth(40)

        self.change_all_button = QPushButton("Change")
        self.change_cancel_button = QPushButton("Cancel")

        self.total_tab_change_window_grid.addWidget(self.change_exchange_label, 0, 1, 1, 1, alignment=Qt.AlignBottom)
        self.total_tab_change_window_grid.addWidget(self.change_exchange_combo, 1, 1, 1, 1)


        self.total_tab_change_window_grid.addWidget(self.change_cryptocur_label, 2, 1, 1, 1, alignment=Qt.AlignBottom)
        self.total_tab_change_window_grid.addWidget(self.change_cryptocur_combo, 3, 1, 1, 1)


        self.total_tab_change_window_grid.addWidget(self.change_buy_sell_label, 4, 1, 1, 1, alignment=Qt.AlignBottom)
        self.total_tab_change_window_grid.addWidget(self.change_buy_sell_combo, 5, 1, 1, 1)

        self.total_tab_change_window_grid.addWidget(self.change_show_button, 6, 1, 1, 1,
                                                 alignment=Qt.AlignTop | Qt.AlignCenter)

        self.total_tab_change_window_grid.addWidget(self.change_id_label, 0, 3, 1, 1, alignment=Qt.AlignBottom)
        self.total_tab_change_window_grid.addWidget(self.change_id_edit, 1, 3, 1, 1)

        self.total_tab_change_window_grid.addWidget(self.change_price_label, 0, 5, 1, 1, alignment=Qt.AlignBottom)
        self.total_tab_change_window_grid.addWidget(self.change_price_edit, 1, 5, 1, 1)

        self.total_tab_change_window_grid.addWidget(self.change_value_label, 2, 3, 1, 1, alignment=Qt.AlignBottom)
        self.total_tab_change_window_grid.addWidget(self.change_value_edit, 3, 3, 1, 1)

        self.total_tab_change_window_grid.addWidget(self.change_action_label, 2, 5, 1, 1, alignment=Qt.AlignBottom)
        self.total_tab_change_window_grid.addWidget(self.change_action_edit, 3, 5, 1, 1)

        self.total_tab_change_window_grid.addWidget(self.change_new_staking_label, 4, 3, 1, 1, alignment=Qt.AlignBottom)
        self.total_tab_change_window_grid.addWidget(self.change_new_staking_edit, 5, 3, 1, 1)

        self.total_tab_change_window_grid.addWidget(self.change_date_label, 4, 5, 1, 1, alignment=Qt.AlignBottom)
        self.total_tab_change_window_grid.addWidget(self.change_date_edit, 5, 5, 1, 1)

        self.total_tab_change_window_grid.addWidget(self.change_old_staking_label, 6, 3, 1, 1, alignment=Qt.AlignBottom)
        self.total_tab_change_window_grid.addWidget(self.change_old_staking_edit, 7, 3, 1, 1)

        self.total_tab_change_window_grid.addWidget(self.change_all_button, 8, 3, 1, 2, alignment=Qt.AlignBottom)
        self.total_tab_change_window_grid.addWidget(self.change_cancel_button, 8, 5, 1, 2, alignment=Qt.AlignBottom)


    def total_tab_buttons(self):

        self.currenc_total_label = QLabel("Total: 200$")

        self.currenc_add_button = QPushButton("Add")
        self.currenc_add_button.setMinimumHeight(40)

        self.currenc_delete_button = QPushButton("Delete")
        self.currenc_delete_button.setMinimumHeight(40)

        self.currenc_change_button = QPushButton("Change")
        self.currenc_change_button.setMinimumHeight(40)

        all_cryptocurrencies_diagram = Example(create_loop_diagram('binance'))

        all_exchanges_diagram = Example(create_loop_diagram('binance'))

        self.total_tab_grid.addWidget(self.currenc_total_label, 1, 0, 1, 1, alignment=Qt.AlignTop | Qt.AlignRight)

        self.total_tab_grid.addWidget(self.currenc_add_button, 1, 2, 1, 1)
        self.total_tab_grid.addWidget(self.currenc_delete_button, 1, 3, 1, 1)
        self.total_tab_grid.addWidget(self.currenc_change_button, 1, 4, 1, 1)

        self.total_tab_grid.addWidget(all_cryptocurrencies_diagram.chart_view, 3, 0, 6, 5)
        self.total_tab_grid.addWidget(all_exchanges_diagram.chart_view, 3, 5, 6, 5)

    def change_edit_to_side_exch(self):

        if self.add_exchange_toggle.isEnabled():
            self.counter_exc += 1

            # --- edit show --- #

            if self.counter_exc % 2 != 0:
                self.add_exchange_combo.hide()
                self.add_exchange_edit.show()

                self.add_cryptocur_toggle.hide()
                self.add_cryptocur_combo.hide()
                self.add_cryptocur_edit.show()

                self.add_cryptocur_combo.clear()
                self.add_buy_sell_combo.clear()

                Investments.add_window_lock_unlock_edits(self, True)
                self.add_buy_sell_combo.addItems(["", "all", "buy", "sell"])
                self.add_buy_sell_combo.setEnabled(True)

            else:

                # --- combo show --- #

                self.add_exchange_edit.hide()
                self.add_exchange_combo.show()

                self.add_cryptocur_toggle.show()
                self.add_cryptocur_edit.hide()
                self.add_cryptocur_combo.show()

                self.add_buy_sell_combo.removeItem(3)
                self.add_buy_sell_combo.removeItem(2)
                self.add_buy_sell_combo.removeItem(1)
                self.add_buy_sell_combo.removeItem(0)
                self.add_buy_sell_combo.setEnabled(False)
                Investments.add_window_lock_unlock_edits(self, False)

                text = self.add_exchange_combo.currentText()
                if text != "":
                    self.add_cryptocur_combo.addItems(select_all_crypto_from_db(text))

    def change_edit_to_side_crypto(self):

        if self.add_cryptocur_toggle.isEnabled():
            self.counter_crypto += 1

            if self.counter_crypto % 2 != 0:

                # --- edit show --- #

                self.add_cryptocur_combo.hide()
                self.add_cryptocur_combo.clear()
                self.add_cryptocur_edit.show()

                self.add_buy_sell_combo.clear()

                self.add_buy_sell_combo.setEnabled(True)

                self.add_buy_sell_combo.addItems(["", "all", "buy", "sell"])
                add_bs_combo_model = self.add_buy_sell_combo.model()
                add_bs_combo_model.item(0).setEnabled(False)

            else:

                # --- combo show --- #

                self.add_cryptocur_edit.hide()
                self.add_cryptocur_edit.clear()
                self.add_cryptocur_combo.show()

                self.add_buy_sell_combo.clear()

                cryptos = select_all_crypto_from_db(self.add_exchange_combo.currentText())
                cryptos.insert(0, "")
                self.add_cryptocur_combo.addItems(cryptos)

                if self.add_cryptocur_combo.currentText() == "":
                    self.add_buy_sell_combo.setEnabled(False)

    def add_window_lock_unlock_edits(self, F):

        self.add_price_edit.setEnabled(F)
        self.add_date_edit.setEnabled(F)
        self.add_value_edit.setEnabled(F)

    def delete_window_lock_unlock_edits(self, F):

        self.delete_id_edit.setEnabled(F)

    def change_window_lock_unlock_edits(self, F):

        self.change_price_edit.setEnabled(F)
        self.change_date_edit.setEnabled(F)
        self.change_new_staking_edit.setEnabled(F)
        self.change_value_edit.setEnabled(F)
        self.change_id_edit.setEnabled(F)
        self.change_action_edit.setEnabled(F)

    def add_window_init(self):

        databases = select_all_databases()
        databases.insert(0, "")

        self.add_exchange_combo.addItems(databases)
        add_exchange_combo_model = self.add_exchange_combo.model()
        add_exchange_combo_model.item(0).setEnabled(False)

        self.add_cryptocur_combo.addItems([""])
        add_cryptocur_combo_model = self.add_cryptocur_combo.model()
        add_cryptocur_combo_model.item(0).setEnabled(False)

        Investments.add_window_lock_unlock_edits(self, False)
        self.add_staking_edit.setEnabled(False)

        self.add_cryptocur_combo.setEnabled(False)
        self.add_buy_sell_combo.setEnabled(False)


    def delete_window_init(self):

        databases = select_all_databases()
        databases.insert(0, "")

        self.delete_exchange_combo.addItems(databases)
        delete_exchange_combo_model = self.delete_exchange_combo.model()
        delete_exchange_combo_model.item(0).setEnabled(False)

        self.delete_cryptocur_combo.addItems([""])
        delete_cryptocur_combo_model = self.delete_cryptocur_combo.model()
        delete_cryptocur_combo_model.item(0).setEnabled(False)

        Investments.delete_window_lock_unlock_edits(self, False)

        self.delete_cryptocur_combo.setEnabled(False)
        self.delete_buy_sell_combo.setEnabled(False)


    def change_window_init(self):

        databases = select_all_databases()
        databases.insert(0, "")

        self.change_exchange_combo.addItems(databases)
        change_exchange_combo_model = self.change_exchange_combo.model()
        change_exchange_combo_model.item(0).setEnabled(False)

        self.change_cryptocur_combo.addItems([""])
        change_cryptocur_combo_model = self.change_cryptocur_combo.model()
        change_cryptocur_combo_model.item(0).setEnabled(False)

        Investments.change_window_lock_unlock_edits(self, False)

        self.change_cryptocur_combo.setEnabled(False)
        self.change_buy_sell_combo.setEnabled(False)

    def database_selected(self, echange_combo, crypto_combo, bs_combo, locker):

        if echange_combo.currentText() != "":
            crypto_combo.clear()
            cryptos = select_all_crypto_from_db(echange_combo.currentText())
            cryptos.insert(0, "")
            crypto_combo.addItems(cryptos)

            add_cryptocur_combo_model = crypto_combo.model()
            add_cryptocur_combo_model.item(0).setEnabled(False)

            crypto_combo.setEnabled(True)
            bs_combo.clear()
            bs_combo.setEnabled(False)

            if locker == "add":
                Investments.add_window_lock_unlock_edits(self, False)

            elif locker == "delete":
                Investments.delete_window_lock_unlock_edits(self, False)

            else:
                Investments.change_window_lock_unlock_edits(self, False)

    def crypto_selected(self, crypto_combo, bs_combo):

        if crypto_combo.currentText() != "":
            bs_combo.clear()
            bs_combo.addItems(["", "all", "buy", "sell"])
            add_bs_combo_model = bs_combo.model()
            add_bs_combo_model.item(0).setEnabled(False)

            bs_combo.setEnabled(True)

    def action_selected(self, bs_combo, action):

        if action == "add":
            if bs_combo.currentText() != "":
                Investments.add_window_lock_unlock_edits(self, True)
                self.add_staking_edit.setText("-")

                if (self.add_exchange_toggle.isChecked()) or (self.add_cryptocur_toggle.isChecked()):
                    self.add_staking_edit.setEnabled(True)
                    self.add_staking_edit.clear()

            else:
                Investments.add_window_lock_unlock_edits(self, False)
                self.add_staking_edit.setEnabled(False)
                self.add_staking_edit.clear()

        elif action == "delete":
            if bs_combo.currentText() != "":
                Investments.delete_window_lock_unlock_edits(self, True)

            else:
                Investments.delete_window_lock_unlock_edits(self, False)

        else:
            if bs_combo.currentText() != "":
                Investments.change_window_lock_unlock_edits(self, True)
                self.change_old_staking_edit.setText(check_staking(self.change_exchange_combo.currentText(),
                                                            self.change_cryptocur_combo.currentText()))

            else:
                Investments.change_window_lock_unlock_edits(self, False)
                self.change_old_staking_edit.clear()


    def show_btn_clicked(self, action):

        # self, item_model, table_view, grid, param, r, c, cr, cc

        if action == "add":
            self.total_add_tab_item_model.setRowCount(0)

            table_view = self.total_add_tab_table_view
            window_grid = self.total_tab_add_window_grid
            item_model = self.total_add_tab_item_model

            exchange = self.add_exchange_combo.currentText()
            cryptocurrency = self.add_cryptocur_combo.currentText()
            buy_sell = self.add_buy_sell_combo.currentText()

        elif action == "delete":
            self.total_delete_tab_item_model.setRowCount(0)

            table_view = self.total_delete_tab_table_view
            window_grid = self.total_tab_delete_window_grid
            item_model = self.total_delete_tab_item_model

            exchange = self.delete_exchange_combo.currentText()
            cryptocurrency = self.delete_cryptocur_combo.currentText()
            buy_sell = self.delete_buy_sell_combo.currentText()

        else:
            self.total_change_tab_item_model.setRowCount(0)

            table_view = self.total_change_tab_table_view
            window_grid = self.total_tab_change_window_grid
            item_model = self.total_change_tab_item_model

            exchange = self.change_exchange_combo.currentText()
            cryptocurrency = self.change_cryptocur_combo.currentText()
            buy_sell = self.change_buy_sell_combo.currentText()

        if exchange == "":
            Investments.table_for_all_initialize(self, item_model, table_view,
                                                 window_grid, 3, 1, 7, 6, 1)

            databases = select_all_databases()

            for value in databases:
                item_model.appendRow(QStandardItem(value))

        elif cryptocurrency == "":
            Investments.table_for_all_initialize(self, item_model, table_view,
                                                 window_grid, 3, 1, 7, 6, 2)

            all_info = select_all_crypto_from_db(exchange)

            for crypto in all_info:
                item_model.appendRow(QStandardItem(crypto))

        elif buy_sell == "":
            Investments.table_for_all_initialize(self, item_model, table_view,
                                                 window_grid, 1, 1, 7, 6, 3)

            all_info = select_all_info_about_crypto(exchange, cryptocurrency)

            for row in all_info:
                _, name, action, count, price, date = row

                day, month, year = date.day, date.month, date.year

                if date.day < 10:
                    day = f"0{date.day}"

                if date.month < 10:
                    month = f"0{date.month}"

                new_date = f"{day}.{month}.{year}"
                item_model.appendRow([QStandardItem(name),
                                                         QStandardItem(action),
                                                         QStandardItem(str(count)),
                                                         QStandardItem(str(price)),
                                                         QStandardItem(new_date),
                                                         ])

        else:
            Investments.table_for_all_initialize(self, item_model, table_view,
                                                 window_grid, 2, 1, 7, 6, 3)

            all_info = select_buy_sell_info_about_crypto(exchange, cryptocurrency, buy_sell)

            for row in all_info:
                coin_id, name, action, count, price, date = row

                # скорее всего переделаем формат DATE в VARCHAR
                day, month, year = date.day, date.month, date.year

                if date.day < 10:
                    day = f"0{date.day}"

                if date.month < 10:
                    month = f"0{date.month}"

                new_date = f"{day}.{month}.{year}"
                item_model.appendRow([QStandardItem(str(coin_id)),
                                      QStandardItem(name),
                                      QStandardItem(action),
                                      QStandardItem(str(count)),
                                      QStandardItem(str(price)),
                                      QStandardItem(new_date),
                                      ])

        table_view.resizeColumnsToContents()
        table_view.resizeRowsToContents()
        table_view.sortByColumn(0, Qt.AscendingOrder)

    def add_cancel_button(self):

        self.add_exchange_combo.setCurrentIndex(0)
        self.add_exchange_edit.clear()

        self.add_cryptocur_combo.clear()
        self.add_cryptocur_edit.clear()

        self.add_buy_sell_combo.clear()

        self.add_price_edit.clear()
        self.add_value_edit.clear()
        self.add_staking_edit.clear()
        self.add_date_edit.clear()
        self.total_add_tab_item_model.setRowCount(0)

        Investments.add_window_lock_unlock_edits(self, False)
        self.add_cryptocur_combo.setEnabled(False)
        self.add_buy_sell_combo.setEnabled(False)

    def delete_cancel_button(self):

        self.delete_exchange_combo.setCurrentIndex(0)

        self.delete_cryptocur_combo.clear()

        self.delete_buy_sell_combo.clear()

        self.total_add_tab_item_model.setRowCount(0)

        Investments.delete_window_lock_unlock_edits(self, False)
        self.delete_cryptocur_combo.setEnabled(False)
        self.delete_buy_sell_combo.setEnabled(False)

    def change_cancel_button(self):

        self.change_exchange_combo.setCurrentIndex(0)

        self.change_cryptocur_combo.clear()

        self.change_buy_sell_combo.clear()

        self.change_id_edit.clear()
        self.change_price_edit.clear()
        self.change_value_edit.clear()
        self.change_new_staking_edit.clear()
        self.change_action_edit.clear()
        self.change_date_edit.clear()
        self.change_old_staking_edit.clear()
        self.total_add_tab_item_model.setRowCount(0)

        Investments.change_window_lock_unlock_edits(self, False)
        self.change_cryptocur_combo.setEnabled(False)
        self.change_buy_sell_combo.setEnabled(False)

    def action_for_add_button(self):

        if self.add_exchange_combo.isHidden(): exchange = self.add_exchange_edit.text().lower()

        else: exchange = self.add_exchange_combo.currentText()

        if self.add_cryptocur_combo.isHidden(): cryptocurrency = self.add_cryptocur_edit.text().lower().replace(" ", "_")

        else: cryptocurrency = self.add_cryptocur_combo.currentText()

        current_action = self.add_buy_sell_combo.currentText()

        if current_action == "all":
            print("Do anything, idiot")

        else:
            add_coin_full(exchange, cryptocurrency, float(self.add_value_edit.text()),
                          self.add_date_edit.text(), float(self.add_price_edit.text()),
                          current_action[0], self.add_staking_edit.text())

            # --- here function for micro changes json file (no fuck you) --- #
            update_db()
            # ----------------------------------------------------- #

            # update old table data #
            insert_data_to_all_tables(self.binance_item_model, self.binance_table_view)
            # --------------------- #

            # clear edits and another #
            Investments.add_cancel_button(self)
            # ----------------------- #

            # update loop diagram #
            binance_diagram = Example(create_loop_diagram('binance'))
            self.binance_tab_grid.addWidget(binance_diagram.chart_view, 0, 5, 0, 4)
            # ------------------- #

    def action_for_delete_button(self):

        exchange = self.delete_exchange_combo.currentText()
        cryptocurrency = self.delete_cryptocur_combo.currentText()
        crypto_id = self.delete_id_edit.text()

        self.delete_id_edit.clear()

        delete_coin_full(exchange, cryptocurrency, crypto_id)

        update_db()

        insert_data_to_all_tables(self.binance_item_model, self.binance_table_view)

        Investments.delete_cancel_button(self)

        binance_diagram = Example(create_loop_diagram('binance'))
        self.binance_tab_grid.addWidget(binance_diagram.chart_view, 0, 5, 0, 4)

    def action_for_change_button(self):

        exchange = self.change_exchange_combo.currentText()
        cryptocurrency = self.change_cryptocur_combo.currentText()
        crypto_id = self.change_id_edit.text()
        new_price = self.change_price_edit.text()
        new_count = self.change_value_edit.text()
        new_action = self.change_action_edit.text()
        new_staking = self.change_new_staking_edit.text()
        new_date = self.change_date_edit.text()

        change_coin_info(exchange, cryptocurrency, crypto_id, new_price, new_count, new_action, new_staking, new_date)

        update_db()

        insert_data_to_all_tables(self.binance_item_model, self.binance_table_view)

        Investments.change_cancel_button(self)

        binance_diagram = Example(create_loop_diagram('binance'))
        self.binance_tab_grid.addWidget(binance_diagram.chart_view, 0, 5, 0, 4)


    def add_dialog_window_open(self):
        if not self.add_dialog_window.isVisible():
            self.add_dialog_window.exec()
            Investments.add_cancel_button(self)

    def delete_dialog_window_open(self):
        if not self.delete_dialog_window.isVisible():
            self.delete_dialog_window.exec()
            Investments.delete_cancel_button(self)

    def change_dialog_window_open(self):
        if not self.change_dialog_window.isVisible():
            self.change_dialog_window.exec()
            Investments.change_cancel_button(self)


    def actions_for_crypto_db_buttons(self):

        self.currenc_add_button.clicked.connect(lambda: Investments.add_dialog_window_open(self))
        self.currenc_delete_button.clicked.connect(lambda: Investments.delete_dialog_window_open(self))
        self.currenc_change_button.clicked.connect(lambda: Investments.change_dialog_window_open(self))


    def actions_for_add_crypto_window(self):

        self.add_exchange_toggle.clicked.connect(lambda: Investments.change_edit_to_side_exch(self))
        self.add_cryptocur_toggle.clicked.connect(lambda: Investments.change_edit_to_side_crypto(self))

        self.add_exchange_combo.currentTextChanged.connect(lambda: Investments.database_selected(self,
                                                                                                 self.add_exchange_combo,
                                                                                                 self.add_cryptocur_combo,
                                                                                                 self.add_buy_sell_combo,
                                                                                                 "add"))

        self.add_cryptocur_combo.currentTextChanged.connect(lambda: Investments.crypto_selected(self,
                                                                                                self.add_cryptocur_combo,
                                                                                                self.add_buy_sell_combo))

        self.add_buy_sell_combo.currentTextChanged.connect(lambda: Investments.action_selected(self,
                                                                                               self.add_buy_sell_combo,
                                                                                               "add"))

        self.add_show_button.clicked.connect(lambda: Investments.show_btn_clicked(self, "add"))

        self.add_cancel_button.clicked.connect(lambda: Investments.add_cancel_button(self))

        self.add_all_button.clicked.connect(lambda: Investments.action_for_add_button(self))


    def actions_for_delete_crypto_window(self):

        self.delete_exchange_combo.currentTextChanged.connect(lambda: Investments.database_selected(self,
                                                                                                    self.delete_exchange_combo,
                                                                                                    self.delete_cryptocur_combo,
                                                                                                    self.delete_buy_sell_combo,
                                                                                                    "delete"))

        self.delete_cryptocur_combo.currentTextChanged.connect(lambda: Investments.crypto_selected(self,
                                                                                                   self.delete_cryptocur_combo,
                                                                                                   self.delete_buy_sell_combo))

        self.delete_buy_sell_combo.currentTextChanged.connect(lambda: Investments.action_selected(self,
                                                                                                  self.delete_buy_sell_combo,
                                                                                                  "delete"))

        self.delete_show_button.clicked.connect(lambda: Investments.show_btn_clicked(self, "delete"))

        self.delete_cancel_button.clicked.connect(lambda: Investments.delete_cancel_button(self))

        self.delete_all_button.clicked.connect(lambda: Investments.action_for_delete_button(self))

    def actions_for_change_crypto_window(self):
        self.change_exchange_combo.currentTextChanged.connect(lambda: Investments.database_selected(self,
                                                                                                    self.change_exchange_combo,
                                                                                                    self.change_cryptocur_combo,
                                                                                                    self.change_buy_sell_combo,
                                                                                                    "change"))

        self.change_cryptocur_combo.currentTextChanged.connect(lambda: Investments.crypto_selected(self,
                                                                                                   self.change_cryptocur_combo,
                                                                                                   self.change_buy_sell_combo))

        self.change_buy_sell_combo.currentTextChanged.connect(lambda: Investments.action_selected(self,
                                                                                                  self.change_buy_sell_combo,
                                                                                                  "change"))

        self.change_show_button.clicked.connect(lambda: Investments.show_btn_clicked(self, "change"))

        self.change_cancel_button.clicked.connect(lambda: Investments.change_cancel_button(self))

        self.change_all_button.clicked.connect(lambda: Investments.action_for_change_button(self))




    def total_tab_grid_setting(self):

        self.total_tab_grid = QGridLayout(self.tab_total)

        self.total_tab_grid.setColumnStretch(0, 1)
        self.total_tab_grid.setColumnStretch(1, 1)
        self.total_tab_grid.setColumnStretch(2, 1)
        self.total_tab_grid.setColumnStretch(3, 1)
        self.total_tab_grid.setColumnStretch(4, 1)
        self.total_tab_grid.setColumnStretch(5, 1)
        self.total_tab_grid.setColumnStretch(6, 1)
        self.total_tab_grid.setColumnStretch(7, 1)
        self.total_tab_grid.setColumnStretch(8, 1)
        self.total_tab_grid.setColumnStretch(9, 1)

        self.total_tab_grid.setRowStretch(0, 1)
        self.total_tab_grid.setRowStretch(1, 1)
        self.total_tab_grid.setRowStretch(2, 1)
        self.total_tab_grid.setRowStretch(3, 1)
        self.total_tab_grid.setRowStretch(4, 1)
        self.total_tab_grid.setRowStretch(5, 1)
        self.total_tab_grid.setRowStretch(6, 1)
        self.total_tab_grid.setRowStretch(7, 2)


    def binance_tab_grid_settings(self):

        self.binance_tab_grid = QGridLayout(self.tab_binance)

        self.binance_tab_grid.setColumnStretch(0, 1)
        self.binance_tab_grid.setColumnStretch(1, 1)
        self.binance_tab_grid.setColumnStretch(2, 1)
        self.binance_tab_grid.setColumnStretch(3, 1)
        self.binance_tab_grid.setColumnStretch(4, 1)
        self.binance_tab_grid.setColumnStretch(5, 1)
        self.binance_tab_grid.setColumnStretch(6, 1)
        self.binance_tab_grid.setColumnStretch(7, 1)
        self.binance_tab_grid.setColumnStretch(8, 1)

        self.binance_tab_grid.setRowStretch(0, 1)
        self.binance_tab_grid.setRowStretch(1, 1)
        self.binance_tab_grid.setRowStretch(2, 1)
        self.binance_tab_grid.setRowStretch(3, 1)




    def total_tab_add_window_grid_settings(self):

        self.total_tab_add_window_grid = QGridLayout(self.add_dialog_window)

        self.total_tab_add_window_grid.setRowStretch(0, 1)
        self.total_tab_add_window_grid.setRowStretch(1, 1)
        self.total_tab_add_window_grid.setRowStretch(2, 1)
        self.total_tab_add_window_grid.setRowStretch(3, 1)
        self.total_tab_add_window_grid.setRowStretch(4, 1)
        self.total_tab_add_window_grid.setRowStretch(5, 1)
        self.total_tab_add_window_grid.setRowStretch(6, 1)
        self.total_tab_add_window_grid.setRowStretch(7, 3)
        self.total_tab_add_window_grid.setRowStretch(8, 1)
        self.total_tab_add_window_grid.setRowStretch(9, 1)

        self.total_tab_add_window_grid.setColumnStretch(0, 1)
        self.total_tab_add_window_grid.setColumnStretch(1, 1)
        self.total_tab_add_window_grid.setColumnStretch(2, 1)
        self.total_tab_add_window_grid.setColumnStretch(3, 1)
        self.total_tab_add_window_grid.setColumnStretch(4, 1)
        self.total_tab_add_window_grid.setColumnStretch(5, 1)
        self.total_tab_add_window_grid.setColumnStretch(6, 1)
        self.total_tab_add_window_grid.setColumnStretch(7, 1)
        self.total_tab_add_window_grid.setColumnStretch(8, 1)
        self.total_tab_add_window_grid.setColumnStretch(9, 1)

    def total_tab_delete_window_grid_settings(self):

        self.total_tab_delete_window_grid = QGridLayout(self.delete_dialog_window)

        self.total_tab_delete_window_grid.setRowStretch(0, 1)
        self.total_tab_delete_window_grid.setRowStretch(1, 1)
        self.total_tab_delete_window_grid.setRowStretch(2, 1)
        self.total_tab_delete_window_grid.setRowStretch(3, 1)
        self.total_tab_delete_window_grid.setRowStretch(4, 1)
        self.total_tab_delete_window_grid.setRowStretch(5, 1)
        self.total_tab_delete_window_grid.setRowStretch(6, 1)
        self.total_tab_delete_window_grid.setRowStretch(7, 3)
        self.total_tab_delete_window_grid.setRowStretch(8, 1)
        self.total_tab_delete_window_grid.setRowStretch(9, 1)

        self.total_tab_delete_window_grid.setColumnStretch(0, 1)
        self.total_tab_delete_window_grid.setColumnStretch(1, 1)
        self.total_tab_delete_window_grid.setColumnStretch(2, 1)
        self.total_tab_delete_window_grid.setColumnStretch(3, 1)
        self.total_tab_delete_window_grid.setColumnStretch(4, 1)
        self.total_tab_delete_window_grid.setColumnStretch(5, 1)
        self.total_tab_delete_window_grid.setColumnStretch(6, 1)
        self.total_tab_delete_window_grid.setColumnStretch(7, 1)
        self.total_tab_delete_window_grid.setColumnStretch(8, 1)
        self.total_tab_delete_window_grid.setColumnStretch(9, 1)

    def total_tab_change_window_grid_settings(self):

        self.total_tab_change_window_grid = QGridLayout(self.change_dialog_window)

        self.total_tab_change_window_grid.setRowStretch(0, 1)
        self.total_tab_change_window_grid.setRowStretch(1, 1)
        self.total_tab_change_window_grid.setRowStretch(2, 1)
        self.total_tab_change_window_grid.setRowStretch(3, 1)
        self.total_tab_change_window_grid.setRowStretch(4, 1)
        self.total_tab_change_window_grid.setRowStretch(5, 1)
        self.total_tab_change_window_grid.setRowStretch(6, 1)
        self.total_tab_change_window_grid.setRowStretch(7, 1)
        self.total_tab_change_window_grid.setRowStretch(8, 1)
        self.total_tab_change_window_grid.setRowStretch(9, 1)

        self.total_tab_change_window_grid.setColumnStretch(0, 1)
        self.total_tab_change_window_grid.setColumnStretch(1, 1)
        self.total_tab_change_window_grid.setColumnStretch(2, 1)
        self.total_tab_change_window_grid.setColumnStretch(3, 1)
        self.total_tab_change_window_grid.setColumnStretch(4, 1)
        self.total_tab_change_window_grid.setColumnStretch(5, 1)
        self.total_tab_change_window_grid.setColumnStretch(6, 1)
        self.total_tab_change_window_grid.setColumnStretch(7, 1)
        self.total_tab_change_window_grid.setColumnStretch(8, 1)
        self.total_tab_change_window_grid.setColumnStretch(9, 1)




    def currencies_grid_settings(self):
        self.currenc_grid.setColumnStretch(0, 1)
        self.currenc_grid.setColumnStretch(1, 1)
        self.currenc_grid.setColumnStretch(1, 1)

        self.currenc_grid.setRowStretch(0, 1)
        self.currenc_grid.setRowStretch(1, 1)
        self.currenc_grid.setRowStretch(1, 1)
