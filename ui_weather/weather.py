from PyQt5.QtWidgets import QWidget, QGridLayout
from Scripts.Weather.weather import week
from ui_weather.backend import weather_grid_settings_4_every_day, weather_grid_info_4_every_day


class Weather(QWidget):

    # function of weather widget
    def weather_widget_window(self):
        self.weather_widget = QWidget()
        self.weather_grid = QGridLayout(self.weather_widget)
        self.weather_widget.setStyleSheet("background-color: rgb(40, 40, 40)")

        self.weather_day_0 = QWidget()
        self.weather_day_0_grid = QGridLayout(self.weather_day_0)
        weather_grid_settings_4_every_day(self.weather_day_0_grid)

        self.weather_day_1 = QWidget()
        self.weather_day_1_grid = QGridLayout(self.weather_day_1)
        weather_grid_settings_4_every_day(self.weather_day_1_grid)

        self.weather_day_2 = QWidget()
        self.weather_day_2_grid = QGridLayout(self.weather_day_2)
        weather_grid_settings_4_every_day(self.weather_day_2_grid)

        self.weather_day_3 = QWidget()
        self.weather_day_3_grid = QGridLayout(self.weather_day_3)
        weather_grid_settings_4_every_day(self.weather_day_3_grid)

        self.weather_day_4 = QWidget()
        self.weather_day_4_grid = QGridLayout(self.weather_day_4)
        weather_grid_settings_4_every_day(self.weather_day_4_grid)

        self.weather_day_5 = QWidget()
        self.weather_day_5_grid = QGridLayout(self.weather_day_5)
        weather_grid_settings_4_every_day(self.weather_day_5_grid)

        self.weather_day_6 = QWidget()
        self.weather_day_6_grid = QGridLayout(self.weather_day_6)
        weather_grid_settings_4_every_day(self.weather_day_6_grid)

        self.weather_today = QWidget()
        self.weather_today.setStyleSheet("background-color: rgb(130, 130, 130)")

        self.weather_grid.addWidget(self.weather_day_0, 5, 0, 3, 1)
        self.weather_grid.addWidget(self.weather_day_1, 5, 1, 3, 1)
        self.weather_grid.addWidget(self.weather_day_2, 5, 2, 3, 1)
        self.weather_grid.addWidget(self.weather_day_3, 5, 3, 3, 1)
        self.weather_grid.addWidget(self.weather_day_4, 5, 4, 3, 1)
        self.weather_grid.addWidget(self.weather_day_5, 5, 5, 3, 1)
        self.weather_grid.addWidget(self.weather_day_6, 5, 6, 3, 1)

        self.weather_grid.addWidget(self.weather_today, 1, 1, 3, 5)

        self.weather_grid.setSpacing(3)
        self.weather_grid.setContentsMargins(3, 3, 3, 3)

        Weather.insert_data_to_add_weather_days(self)

    def insert_data_to_add_weather_days(self):

        res = week()

        weather_grid_info_4_every_day(res[0], self.weather_day_0, self.weather_day_0_grid)
        weather_grid_info_4_every_day(res[1], self.weather_day_1, self.weather_day_1_grid)
        weather_grid_info_4_every_day(res[2], self.weather_day_2, self.weather_day_2_grid)
        weather_grid_info_4_every_day(res[3], self.weather_day_3, self.weather_day_3_grid)
        weather_grid_info_4_every_day(res[4], self.weather_day_4, self.weather_day_4_grid)
        weather_grid_info_4_every_day(res[5], self.weather_day_5, self.weather_day_5_grid)
        weather_grid_info_4_every_day(res[6], self.weather_day_6, self.weather_day_6_grid)

    def weather_grid_settings(self):
        self.weather_grid.setColumnStretch(0, 1)
        self.weather_grid.setColumnStretch(1, 1)
        self.weather_grid.setColumnStretch(2, 1)
        self.weather_grid.setColumnStretch(3, 1)
        self.weather_grid.setColumnStretch(4, 1)
        self.weather_grid.setColumnStretch(5, 1)
        self.weather_grid.setColumnStretch(6, 1)

        self.weather_grid.setRowStretch(0, 2)
        self.weather_grid.setRowStretch(1, 1)
        self.weather_grid.setRowStretch(2, 1)
        self.weather_grid.setRowStretch(3, 1)
        self.weather_grid.setRowStretch(4, 1)
        self.weather_grid.setRowStretch(5, 1)
        self.weather_grid.setRowStretch(6, 1)
        self.weather_grid.setRowStretch(7, 1)
        self.weather_grid.setRowStretch(8, 1)
