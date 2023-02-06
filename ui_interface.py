from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QFrame, QStackedWidget
from ui_left_mainwidget import LeftWidget
from ui_profile.profile import Profile
from ui_weather.weather import Weather
from ui_passwords.passwords import Passwords
from ui_books.books import Books
from ui_birthdays.birthdays import Birthdays
from ui_investments.investments import Investments


# main class which has key functions for this program
class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):

        self.central_grid = QGridLayout(MainWindow)  # main grid
        self.central_grid_configuration()
        self.F = False


        # Initialization main widgets
        LeftWidget.left_widget(self)
        Profile.profile_settings_window(self)
        Weather.weather_widget_window(self)
        Passwords.password_widget_window(self)
        Books.books_widget_window(self)
        Birthdays.birth_widget_window(self)
        Investments.currencies_widget_window(self)

        # Initialization StackedWidget for correct visualization main widgets
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.books_widget)
        self.stackedWidget.addWidget(self.currenc_widget)
        self.stackedWidget.addWidget(self.weather_widget)
        self.stackedWidget.addWidget(self.passw_widget)
        self.stackedWidget.addWidget(self.birth_widget)
        self.stackedWidget.addWidget(self.profile_widget)
        self.stackedWidget.setCurrentWidget(self.profile_widget)

        self.central_grid.addWidget(self.stackedWidget, 1, 1, 1, 4)



        # Configuration grid settings for main widgets
        LeftWidget.left_widget_grid_settings(self)
        Profile.profile_grid_settings(self)
        Weather.weather_grid_settings(self)
        Birthdays.birth_holidays_grid_settings(self)
        Investments.currencies_grid_settings(self)


        # self.top_menu()

        # Configuration settings for main window
        self.main_frame_settings(MainWindow)

        # Add icon to header of program
        self.add_icon(MainWindow)

        self.top_frames()
        self.bottom_frames()



    def top_menu(self):
        self.toolbar = MenuBar()
        self.real_menu = self.toolbar.menu()
        self.central_grid.addWidget(self.real_menu, 0, 0, 1, 0)

    def top_frames(self):

        self.left_header_frame = QFrame()
        self.left_header_frame.setStyleSheet("background-color: rgb(0, 255, 0)")
        self.left_header_frame_grid = QGridLayout(self.left_header_frame)
        self.left_header_frame_grid.setColumnStretch(0, 1)



        self.right_header_frame = QFrame()
        self.right_header_frame.setStyleSheet("background-color: rgb(255, 0, 0)")
        self.right_header_frame_grid = QGridLayout(self.right_header_frame)

        self.right_header_frame_grid.setColumnStretch(0, 3)
        self.right_header_frame_grid.setColumnStretch(1, 1)
        self.right_header_frame_grid.setColumnStretch(2, 1)
        self.right_header_frame_grid.setColumnStretch(3, 1)



        self.central_header_frame = QFrame()
        self.central_header_frame.setStyleSheet("background-color: rgb(0, 0, 255)")

        self.central_header_frame_grid = QGridLayout(self.central_header_frame)
        self.central_header_frame_grid.setColumnStretch(0, 1)
        self.central_header_frame_grid.setColumnStretch(1, 1)


        self.label = QLabel("Lapa's")
        self.label.setStyleSheet('color: rgb(255, 255, 255);')
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Terminus")
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)


        self.app_logo = QLabel()
        self.app_logo.setObjectName(u"app_logo")
        self.app_logo.setPixmap(QPixmap(u"apl_icon_now.png"))

        self.central_header_frame_grid.addWidget(self.app_logo, 0, 0, alignment=Qt.AlignRight)
        self.central_header_frame_grid.addWidget(self.label, 0, 1, alignment=Qt.AlignLeft)





        self.minimizeWindowButton = QPushButton()
        self.minimizeWindowButton.setObjectName(u"minimizeWindowButton")
        icon1 = QIcon()
        icon1.addFile(u"Pictures\\Apl_icon\\minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeWindowButton.setIcon(icon1)
        self.minimizeWindowButton.setFlat(True)


        self.restoreWindowButton = QPushButton()
        self.restoreWindowButton.setObjectName(u"restoreWindowButton")
        icon2 = QIcon()
        icon2.addFile(u"Pictures\\Apl_icon\\restore.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreWindowButton.setIcon(icon2)
        self.restoreWindowButton.setFlat(True)


        self.closeWindowButton = QPushButton()
        self.closeWindowButton.setObjectName(u"closeWindowButton")
        icon3 = QIcon()
        icon3.addFile(u"Pictures\\Apl_icon\\exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeWindowButton.setIcon(icon3)
        self.closeWindowButton.setFlat(True)

        self.right_header_frame_grid.addWidget(self.minimizeWindowButton, 0, 1)
        self.right_header_frame_grid.addWidget(self.restoreWindowButton, 0, 2)
        self.right_header_frame_grid.addWidget(self.closeWindowButton, 0, 3)



        self.open_close_side_bar_btn = QPushButton("")
        self.open_close_side_bar_btn.setObjectName(u"open_close_side_bar_btn")
        self.open_close_side_bar_btn.setStyleSheet('color: rgb(255, 255, 255);')
        font1 = QFont()
        font1.setFamily(u"Terminus")
        font1.setPointSize(8)
        font1.setBold(True)
        self.open_close_side_bar_btn.setFont(font1)
        icon = QIcon()
        icon.addFile(u"Pictures\\align-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon)
        self.open_close_side_bar_btn.setIconSize(QSize(32, 32))
        self.open_close_side_bar_btn.setFlat(True)

        self.left_header_frame_grid.addWidget(self.open_close_side_bar_btn, 0, 0, alignment=Qt.AlignLeft)






        self.left_header_frame.setStyleSheet(open("CSS-styles/Main widgets/left_widget.css").read())
        self.central_header_frame.setStyleSheet(open("CSS-styles/Main widgets/left_widget.css").read())
        self.right_header_frame.setStyleSheet(open("CSS-styles/Main widgets/left_widget.css").read())

        self.central_grid.addWidget(self.left_header_frame, 0, 0)
        self.central_grid.addWidget(self.central_header_frame, 0, 1, 1, 3)
        self.central_grid.addWidget(self.right_header_frame, 0, 4)


    def bottom_frames(self):

        self.bottom_frame = QFrame()
        self.bottom_frame.setStyleSheet(open("CSS-styles/Main widgets/left_widget.css").read())
        self.bottom_frame_grid = QGridLayout(self.bottom_frame)
        self.bottom_frame_grid.setColumnStretch(0, 1)
        self.bottom_frame_grid.setColumnStretch(1, 1)


        self.help_button = QPushButton("?")
        self.help_button.setStyleSheet('color: rgb(255, 255, 255);')
        self.help_button.setFlat(True)
        font2 = QFont()
        font2.setFamily(u"Terminus")
        font2.setPointSize(12)
        font2.setBold(True)
        self.help_button.setFont(font2)


        self.copyrights = QLabel("Version 1.0 | Copyright Lapa Co.")
        self.copyrights.setStyleSheet('color: rgb(255, 255, 255);')
        font1 = QFont()
        font1.setFamily(u"Terminus")
        font1.setPointSize(10)
        font1.setBold(True)
        self.copyrights.setFont(font1)


        self.bottom_frame_grid.addWidget(self.copyrights, 0, 0, alignment=Qt.AlignLeft)
        self.bottom_frame_grid.addWidget(self.help_button, 0, 1, alignment=Qt.AlignRight)

        self.central_grid.addWidget(self.bottom_frame, 2, 0, 1, 0)


    def central_grid_configuration(self):
        """Configuration setting for central grid"""

        self.central_grid.setContentsMargins(0, 0, 0, 0)  # distance between widgets, grid... and border of the window
        self.central_grid.setSpacing(0)  # distance between widgets located on main grid


        self.central_grid.setColumnStretch(0, 1)
        self.central_grid.setColumnStretch(1, 5)
        self.central_grid.setColumnStretch(2, 5)
        self.central_grid.setColumnStretch(3, 5)
        self.central_grid.setColumnStretch(4, 5)


        self.central_grid.setRowStretch(0, 1)
        self.central_grid.setRowStretch(1, 24)
        self.central_grid.setRowStretch(2, 1)




    def main_frame_settings(self, MainWindow):
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setWindowTitle("Lapa")
        MainWindow.resize(1420, 880)

    def add_icon(self, MainWindow):
        MainWindow.setWindowIcon(QIcon("Pictures\\Apl_icon\\apl_icon_now.png"))

    def omgShit(self):

        if not self.F:

            self.central_grid.setColumnStretch(0, 4)
            self.F = True
            self.btn_weather.setText('Weather')
            self.btn_birth.setText('Celebrations')
            self.btn_currenc.setText('Investments')
            self.btn_passw.setText('Passwords')
            self.btn_books.setText('Books')
            self.btn_photo.show()
            self.nickname_label.show()

        else:

            self.central_grid.setColumnStretch(0, 1)
            self.F = False
            self.btn_weather.setText('')
            self.btn_birth.setText('')
            self.btn_currenc.setText('')
            self.btn_passw.setText('')
            self.btn_books.setText('')
            self.btn_photo.hide()
            self.nickname_label.hide()





# the class for menu in the top of the window
# class MenuBar(QMainWindow):
#     def __init__(self):
#         super(MenuBar, self).__init__()
#
#     def menu(self):
#         menu = QMainWindow.menuBar(self)
#         main = QMenu("File", self)
#         menu.addMenu(main)
#         menu.addMenu("Edit")
#         menu.addMenu("About")
#         return menu
