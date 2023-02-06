from PyQt5.QtWidgets import QWidget, QGridLayout, QTextEdit, QPushButton
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QFont
from ui_birthdays.birth_backend import birth_info_output, holidays_info_output


class Birthdays(QWidget):

    # function of birthday widget
    def birth_widget_window(self):
        self.birth_widget = QWidget()

        self.birth_widget.setStyleSheet(open("CSS-styles/Main widgets/birth_widget.css").read())

        self.birth_holidays_grid = QGridLayout(self.birth_widget)

        Birthdays.birth_actions(self)
        Birthdays.holidays_actions(self)
        Birthdays.actions_for_birthdays_buttons(self)


    def birth_actions(self):
        self.birth_info = QTextEdit()
        # self.birth_info.setStyleSheet(open("CSS-styles/Other/QTextEdit.css").read())
        self.birth_info.setFont(QFont("Monospace", 11))

        self.birth_info_btn = QPushButton("День рождения!")
        self.birth_info_btn.setStyleSheet(open("CSS-styles/Buttons/Birthdays/btn_birthdays.css").read())

        self.birth_info_add_btn = QPushButton()
        self.birth_info_add_btn.setIcon(QIcon("Добавить.jpg"))
        self.birth_info_add_btn.setIconSize(QSize(40, 40))
        self.birth_info_add_btn.setStyleSheet("QPushButton{background: transparent;}")

        self.birth_info_rem_btn = QPushButton()
        self.birth_info_rem_btn.setIcon(QIcon("Удалить.jpg"))
        self.birth_info_rem_btn.setIconSize(QSize(40, 40))
        self.birth_info_rem_btn.setStyleSheet("QPushButton{background: transparent;}")

        self.birth_info_chg_btn = QPushButton()
        self.birth_info_chg_btn.setIcon(QIcon("Изменить.jpg"))
        self.birth_info_chg_btn.setIconSize(QSize(40, 40))
        self.birth_info_chg_btn.setStyleSheet("QPushButton{background: transparent;}")

        self.birth_info_show_btn = QPushButton()
        self.birth_info_show_btn.setIcon(QIcon("Фулл БД.jpg"))
        self.birth_info_show_btn.setIconSize(QSize(40, 40))
        self.birth_info_show_btn.setStyleSheet("QPushButton{background: transparent;}")

        self.birth_holidays_grid.addWidget(self.birth_info, 4, 0, 4, 5)

        self.birth_holidays_grid.addWidget(self.birth_info_btn, 10, 2, 1, 1, alignment=Qt.AlignCenter)

        self.birth_holidays_grid.addWidget(self.birth_info_add_btn, 8, 1, 1, 1, alignment=Qt.AlignLeft)
        self.birth_holidays_grid.addWidget(self.birth_info_rem_btn, 8, 2, 1, 1, alignment=Qt.AlignLeft)
        self.birth_holidays_grid.addWidget(self.birth_info_chg_btn, 8, 2, 1, 1, alignment=Qt.AlignRight)
        self.birth_holidays_grid.addWidget(self.birth_info_show_btn, 8, 3, 1, 1, alignment=Qt.AlignRight)

    def holidays_actions(self):
        self.holidays_info = QTextEdit()
        # self.holidays_info.setStyleSheet(open("CSS-styles/Other/QTextEdit.css").read())
        self.holidays_info.setFont(QFont("Times", 11))

        self.holidays_info_btn = QPushButton("Праздники!")
        self.holidays_info_btn.setStyleSheet(open("CSS-styles/Buttons/Birthdays/btn_holidays.css").read())

        self.holidays_info_btn.setFixedSize(160, 40)

        self.holi_info_add_btn = QPushButton("+")
        self.holi_info_add_btn.setFixedSize(40, 40)

        self.holi_info_rem_btn = QPushButton("-")
        self.holi_info_rem_btn.setFixedSize(40, 40)

        self.holi_info_chg_btn = QPushButton("?")
        self.holi_info_chg_btn.setFixedSize(40, 40)

        self.holi_info_show_btn = QPushButton("!")
        self.holi_info_show_btn.setFixedSize(40, 40)

        self.birth_holidays_grid.addWidget(self.holidays_info, 4, 5, 4, 5)

        self.birth_holidays_grid.addWidget(self.holidays_info_btn, 10, 7, 1, 1)

        self.birth_holidays_grid.addWidget(self.holi_info_add_btn, 8, 6, 1, 1, alignment=Qt.AlignLeft)
        self.birth_holidays_grid.addWidget(self.holi_info_rem_btn, 8, 7, 1, 1, alignment=Qt.AlignLeft)
        self.birth_holidays_grid.addWidget(self.holi_info_chg_btn, 8, 7, 1, 1, alignment=Qt.AlignRight)
        self.birth_holidays_grid.addWidget(self.holi_info_show_btn, 8, 8, 1, 1, alignment=Qt.AlignRight)

    def actions_for_birthdays_buttons(self):

        # Birthday page info output
        self.birth_info_btn.clicked.connect(lambda: birth_info_output(self.birth_info))

        # Holidays page info output
        self.holidays_info_btn.clicked.connect(lambda: holidays_info_output(self.holidays_info))


    def birth_holidays_grid_settings(self):
        self.birth_holidays_grid.setColumnStretch(0, 1)
        self.birth_holidays_grid.setColumnStretch(1, 1)
        self.birth_holidays_grid.setColumnStretch(2, 1)
        self.birth_holidays_grid.setColumnStretch(3, 1)
        self.birth_holidays_grid.setColumnStretch(4, 1)
        self.birth_holidays_grid.setColumnStretch(5, 1)
        self.birth_holidays_grid.setColumnStretch(6, 1)
        self.birth_holidays_grid.setColumnStretch(7, 1)
        self.birth_holidays_grid.setColumnStretch(8, 1)
        self.birth_holidays_grid.setColumnStretch(9, 1)

        self.birth_holidays_grid.setRowStretch(0, 1)
        self.birth_holidays_grid.setRowStretch(1, 1)
        self.birth_holidays_grid.setRowStretch(2, 1)
        self.birth_holidays_grid.setRowStretch(3, 1)
        self.birth_holidays_grid.setRowStretch(4, 1)
        self.birth_holidays_grid.setRowStretch(5, 1)
        self.birth_holidays_grid.setRowStretch(6, 1)
        self.birth_holidays_grid.setRowStretch(7, 1)
        self.birth_holidays_grid.setRowStretch(8, 1)
        self.birth_holidays_grid.setRowStretch(9, 1)
        self.birth_holidays_grid.setRowStretch(10, 1)
        self.birth_holidays_grid.setRowStretch(11, 1)
        self.birth_holidays_grid.setRowStretch(12, 1)
        self.birth_holidays_grid.setRowStretch(13, 1)
