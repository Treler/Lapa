from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel


class LeftWidget(QWidget):

    # widget with main buttons which have actions
    def left_widget(self):
        self.leftWidget = QWidget()  # leftWidget #262F34
        self.leftWidget.setStyleSheet(open("CSS-styles/Main widgets/left_widget.css").read())

        self.leftGrid = QGridLayout(self.leftWidget)

        LeftWidget.photo_button(self)




        self.nickname_label = QLabel("Lapa")
        self.nickname_label.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.nickname_label.setFont(QFont("Times", 15, QFont.Bold))
        self.nickname_label.hide()

        font2 = QFont()
        font2.setFamily(u"Terminus")
        font2.setPointSize(13)
        font2.setBold(True)

        self.btn_weather = QPushButton("")
        icon6 = QIcon()
        icon6.addFile(u"Pictures\\Weather\\weather.png")
        self.btn_weather.setIcon(icon6)
        self.btn_weather.setIconSize(QSize(52, 52))
        self.btn_weather.setFlat(True)
        self.btn_weather.setFont(font2)
        self.btn_weather.setStyleSheet("text-align: center; color: rgb(255, 255, 255);")



        self.btn_birth = QPushButton("")
        icon5 = QIcon()
        icon5.addFile(u"Pictures\\Birthdays\\celebrations.png")
        self.btn_birth.setIcon(icon5)
        self.btn_birth.setIconSize(QSize(52, 52))
        self.btn_birth.setFlat(True)
        self.btn_birth.setFont(font2)
        self.btn_birth.setStyleSheet("color: rgb(255, 255, 255)")


        self.btn_currenc = QPushButton("")
        icon4 = QIcon()
        icon4.addFile(u"Pictures\\Investments\\investments.png")
        self.btn_currenc.setIcon(icon4)
        self.btn_currenc.setIconSize(QSize(52, 52))
        self.btn_currenc.setFlat(True)
        self.btn_currenc.setFont(font2)
        self.btn_currenc.setStyleSheet("color: rgb(255, 255, 255)")

        self.btn_passw = QPushButton("")
        icon3 = QIcon()
        icon3.addFile(u"Pictures\\Passwords\\passwords.png")
        self.btn_passw.setIcon(icon3)
        self.btn_passw.setIconSize(QSize(52, 52))
        self.btn_passw.setFlat(True)
        self.btn_passw.setFont(font2)
        self.btn_passw.setStyleSheet("color: rgb(255, 255, 255)")

        self.btn_books = QPushButton("")
        icon2 = QIcon()
        icon2.addFile(u"Pictures\\Books\\books.png")
        self.btn_books.setIcon(icon2)
        self.btn_books.setIconSize(QSize(52, 52))
        self.btn_books.setFlat(True)
        self.btn_books.setFont(font2)
        self.btn_books.setStyleSheet("color: rgb(255, 255, 255)")

        self.btn_weather.setStyleSheet(open("CSS-styles/Main buttons/btn_weather.css").read())
        self.btn_birth.setStyleSheet(open("CSS-styles/Main buttons/btn_birth.css").read())
        self.btn_currenc.setStyleSheet(open("CSS-styles/Main buttons/btn_currenc.css").read())
        self.btn_passw.setStyleSheet(open("CSS-styles/Main buttons/btn_passw.css").read())
        self.btn_books.setStyleSheet(open("CSS-styles/Main buttons/btn_book.css").read())

        self.leftGrid.addWidget(self.btn_weather, 15, 0, 1, 5)
        self.leftGrid.addWidget(self.btn_birth, 16, 0, 1, 5)
        self.leftGrid.addWidget(self.btn_currenc, 17, 0, 1, 5)
        self.leftGrid.addWidget(self.btn_passw, 18, 0, 1, 5)
        self.leftGrid.addWidget(self.btn_books, 23, 0, 1, 5)
        self.leftGrid.addWidget(self.nickname_label, 1, 0, 1, 5, alignment=Qt.AlignCenter)

        self.central_grid.addWidget(self.leftWidget, 1, 0)

    def photo_button(self):
        self.btn_photo = QPushButton()
        self.btn_photo.setIcon(QIcon("Pictures/Profile_photos/current_avatar.jpg"))
        self.btn_photo.setIconSize(QSize(150, 150))
        self.btn_photo.setStyleSheet("QPushButton{background: transparent;}")
        self.leftGrid.addWidget(self.btn_photo, 0, 0, 1, 5, alignment=Qt.AlignCenter)
        self.btn_photo.hide()

    def left_widget_grid_settings(self):
        self.leftGrid.setColumnStretch(0, 1)
        self.leftGrid.setColumnStretch(1, 1)
        self.leftGrid.setColumnStretch(2, 1)
        self.leftGrid.setColumnStretch(3, 1)
        self.leftGrid.setColumnStretch(4, 1)

        self.leftGrid.setRowStretch(0, 1)
        self.leftGrid.setRowStretch(28, 1)

        self.leftGrid.setVerticalSpacing(35)
        self.leftGrid.setContentsMargins(7, 7, 7, 7)
