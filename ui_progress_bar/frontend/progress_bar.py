from PyQt5.QtCore import QSize, Qt, QRect, QMetaObject
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import QGridLayout, QLabel, QSplashScreen, QProgressBar


class Ui_SplashScreen(QSplashScreen):

    def setupUi(self, ProgressWindow):

        if ProgressWindow.objectName():
            ProgressWindow.setObjectName(u"ProgressWindow")

        ProgressWindow.resize(600, 300)

        self.MainProgressWindow = ProgressWindow

        self.central_grid = QGridLayout(self.MainProgressWindow)
        self.main_grid_settings()


        oImage = QImage("pictures\\progress_bar\\new_bg.jpg")
        sImage = oImage.scaled(QSize(600, 300))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.MainProgressWindow.setPalette(palette)


        self.created_by_label = QLabel("Created: Lapa")
        self.loading_label = QLabel("Loading...")
        self.app_name_label = QLabel("Lapa")
        self.process_now_label = QLabel("")


        self.progressBar = QProgressBar()
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 280, 561, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
                                       "	\n"
                                       "	background-color: rgb(98, 114, 164);\n"
                                       "	color: rgb(200, 200, 200);\n"
                                       "	border-style: none;\n"
                                       "	border-radius: 10px;\n"
                                       "	text-align: center;\n"
                                       "}\n"
                                       "QProgressBar::chunk{\n"
                                       "	border-radius: 10px;\n"
                                       "	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
                                       "}")


        self.central_grid.addWidget(self.progressBar, 7, 1, 1, 3)
        self.central_grid.addWidget(self.app_name_label, 3, 2, 1, 1, alignment=Qt.AlignCenter)
        self.central_grid.addWidget(self.process_now_label, 5, 2, 1, 1, alignment=Qt.AlignCenter)
        self.central_grid.addWidget(self.loading_label, 8, 2, 1, 1, alignment=Qt.AlignCenter)
        self.central_grid.addWidget(self.created_by_label, 9, 4, 1, 1, alignment=Qt.AlignRight)

        QMetaObject.connectSlotsByName(self.MainProgressWindow)

        self.MainProgressWindow.show()

    def main_grid_settings(self):

        self.central_grid.setRowStretch(0, 1)
        self.central_grid.setRowStretch(1, 1)
        self.central_grid.setRowStretch(2, 1)
        self.central_grid.setRowStretch(3, 1)
        self.central_grid.setRowStretch(4, 1)
        self.central_grid.setRowStretch(5, 1)
        self.central_grid.setRowStretch(6, 1)
        self.central_grid.setRowStretch(7, 1)
        self.central_grid.setRowStretch(8, 1)
        self.central_grid.setRowStretch(9, 1)

        self.central_grid.setColumnStretch(0, 1)
        self.central_grid.setColumnStretch(1, 1)
        self.central_grid.setColumnStretch(2, 1)
        self.central_grid.setColumnStretch(3, 1)
        self.central_grid.setColumnStretch(4, 1)
