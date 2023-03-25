from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt


def weather_grid_settings_4_every_day(day_grid):
    day_grid.setColumnStretch(0, 1)
    day_grid.setColumnStretch(1, 1)
    day_grid.setColumnStretch(2, 1)
    day_grid.setColumnStretch(3, 1)

    day_grid.setRowStretch(0, 1)
    day_grid.setRowStretch(1, 1)
    day_grid.setRowStretch(2, 1)
    day_grid.setRowStretch(3, 1)
    day_grid.setRowStretch(4, 1)
    day_grid.setRowStretch(5, 1)
    day_grid.setRowStretch(6, 1)

    day_grid.setSpacing(0)
    day_grid.setContentsMargins(0, 0, 0, 0)


def weather_grid_info_4_every_day(day, widget, g_4_every_day):
    """Configuration setting for every day-weather (Monday, Tuesday...) widget"""

    font = "Times"
    font_size = 16
    color_day = ""
    color = ""
    path_weather = ""
    path_wind = ""
    path_pressure = ""

    if round(day["temp"]) in range(12, 40):
        color = "#ffa726"
        color_day = "#ff9800"
        path_weather = "pictures/weather/sun/SunVeryWarm.png"
        path_wind = "pictures/weather/wind/WindVeryWarm.png"
        path_pressure = "pictures/weather/pressure/PresVeryWarm.png"

    elif round(day["temp"]) in range(0, 12):
        # "#ffcc80"  "#ffb74d"
        color = "#ffc93b"
        color_day = "#ffbd2c"
        path_weather = "pictures/weather/sun/SunWarm.png"
        path_wind = "pictures/weather/wind/WindWarm.png"
        path_pressure = "pictures/weather/pressure/PresWarm.png"

    elif round(day["temp"]) in range(-12, 0):
        color = "#89c4ff"
        color_day = "#66b2ff"
        path_weather = "pictures/weather/sun/SunCold.png"
        path_wind = "pictures/weather/wind/WindCold.png"
        path_pressure = "pictures/weather/pressure/PresCold.png"

    elif round(day["temp"]) in range(-40, -12):
        color = "#42a1ff"
        color_day = "#1e8fff"
        path_weather = "pictures/weather/sun/SunVeryCold.png"
        path_wind = "pictures/weather/wind/WindVeryCold.png"
        path_pressure = "pictures/weather/pressure/PresVeryCold.png"

    # day label
    day_label = QLabel(f"{day['title']}")
    day_label.setFont(QFont(font, font_size))
    day_label.setStyleSheet(f"background-color: {color_day}")
    day_label.setAlignment(Qt.AlignCenter)
    g_4_every_day.addWidget(day_label, 0, 0, 1, 0)

    # weather picture settings
    pic_weather_label = QLabel()
    pic_weather = QPixmap(path_weather)
    pic_weather_label.setPixmap(pic_weather)
    g_4_every_day.addWidget(pic_weather_label, 1, 0, 2, 2, Qt.AlignLeft | Qt.AlignTop)

    # weather label settings
    weather_label = QLabel(str(round(day["temp"])) + " C°")
    weather_label.setFont(QFont(font, font_size))
    weather_label.setStyleSheet(f"background-color: {color}")
    g_4_every_day.addWidget(weather_label, 1, 2, 2, 2, Qt.AlignCenter)

    # wind picture settings
    pic_wind_label = QLabel()
    pic_wind = QPixmap(path_wind)
    pic_wind_label.setPixmap(pic_wind)
    g_4_every_day.addWidget(pic_wind_label, 3, 0, 2, 2, Qt.AlignLeft | Qt.AlignTop)

    # wind label settings
    wind_label = QLabel(f"{round(day['wind_speed'])} m/s")
    wind_label.setFont(QFont(font, font_size))
    wind_label.setStyleSheet(f"background-color: {color}")
    g_4_every_day.addWidget(wind_label, 3, 2, 2, 2, Qt.AlignCenter)

    # pressure picture settings
    pic_pres_label = QLabel()
    pic_pres = QPixmap(path_pressure)
    pic_pres_label.setPixmap(pic_pres)
    g_4_every_day.addWidget(pic_pres_label, 5, 0, 2, 2, Qt.AlignLeft | Qt.AlignTop)

    # pressure label settings
    pres_label = QLabel(f"{day['pressure']} mm")
    pres_label.setFont(QFont(font, font_size))
    pres_label.setStyleSheet(f"background-color: {color}")
    g_4_every_day.addWidget(pres_label, 5, 2, 2, 2, Qt.AlignCenter)

    widget.setStyleSheet(f"background-color: {color}")
