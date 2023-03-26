#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import argv, exit
from ui_interface import *
from apl_functions import center, suppress_qt_warnings
from ui_progress_bar.frontend.progress_bar import Ui_SplashScreen
from PyQt5 import QtTest, QtCore
from PyQt5.QtWidgets import QSplashScreen, QApplication

def func1():
    QtTest.QTest.qWait(200)

def func2():
    QtTest.QTest.qWait(200)


class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(int, str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        data1 = ["First", "Second"]
        data2 = [func2, func1]
        j = 0
        for i in range(len(data1)):
            j += 25
            self.mysignal.emit(j, data1[i])
            data2[i]()


class Progress(QSplashScreen):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

    def potok(self, window, progress):

        self.main_window = window
        self.progress = progress

        self.mythread = MyThread()  # Создаем экземпляр класса
        self.on_clicked()
        self.mythread.finished.connect(self.on_finished)
        self.mythread.mysignal.connect(self.on_change)

    def on_clicked(self):
        self.mythread.start()         # Запускаем поток
        self.ui.progressBar.setValue(0)

    def on_change(self, progress, message):
        self.ui.process_now_label.setText(message)
        self.ui.progressBar.setValue(progress)

    def on_finished(self):      # Вызывается при завершении потока
        self.ui.process_now_label.setText("Complete")
        self.ui.loading_label.setText("")
        QtTest.QTest.qWait(500)

        self.main_window.show()
        self.progress.finish(self.main_window)

        del self.main_window
        del self.progress


class MainWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.actions_for_left_main_buttons()
        self.actions_for_close_minimize_fullscr_buttons()

        # Profile is a start page
        self.ui.stackedWidget.setCurrentWidget(self.ui.profile_widget)

        self.ui.left_header_frame.mouseMoveEvent = self.moveWindow
        self.ui.right_header_frame.mouseMoveEvent = self.moveWindow
        self.ui.central_header_frame.mouseMoveEvent = self.moveWindow


    def moveWindow(self, e):
        # Detect if the window is  normal size
        if self.isMaximized() == False:  # Not maximized
            # Move window only when window is normal size
            # ###############################################
            # if left mouse button is clicked (Only accept left mouse button clicks)
            if e.buttons() == QtCore.Qt.LeftButton:
                # Move window
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()

    def actions_for_left_main_buttons(self):

        # navigate to Profile page
        self.ui.btn_photo.clicked.connect(lambda: self.btn_profile_click())

        # navigate to weather page
        self.ui.btn_weather.clicked.connect(lambda: self.btn_weather_click())

        # navigate to birthdays/Holidays page
        self.ui.btn_birth.clicked.connect(lambda: self.btn_birth_click())

        # navigate to investments page
        self.ui.btn_currenc.clicked.connect(lambda: self.btn_currenc_click())

        # navigate to passwords page
        self.ui.btn_passw.clicked.connect(lambda: self.btn_passw_click())

        # navigate to books page
        self.ui.btn_books.clicked.connect(lambda: self.btn_books_click())

        self.ui.open_close_side_bar_btn.clicked.connect(lambda: self.ui.side_bar())


    def all_css(self):
        self.ui.btn_weather.setStyleSheet(open("css-styles/main_buttons/btn_weather.css").read())
        self.ui.btn_birth.setStyleSheet(open("css-styles/main_buttons/btn_birth.css").read())
        self.ui.btn_currenc.setStyleSheet(open("css-styles/main_buttons/btn_currenc.css").read())
        self.ui.btn_passw.setStyleSheet(open("css-styles/main_buttons/btn_passw.css").read())
        self.ui.btn_books.setStyleSheet(open("css-styles/main_buttons/btn_book.css").read())


    def btn_profile_click(self):
        self.all_css()
        self.ui.stackedWidget.setCurrentWidget(self.ui.profile_widget)

    def btn_weather_click(self):
        self.all_css()
        self.ui.stackedWidget.setCurrentWidget(self.ui.weather_widget)
        self.ui.btn_weather.setStyleSheet(open("css-styles/main_buttons/btn_weather_active.css").read())

    def btn_birth_click(self):
        self.all_css()
        self.ui.stackedWidget.setCurrentWidget(self.ui.birth_widget)
        self.ui.btn_birth.setStyleSheet(open("css-styles/main_buttons/btn_birth_active.css").read())

    def btn_currenc_click(self):
        self.all_css()
        self.ui.stackedWidget.setCurrentWidget(self.ui.currenc_widget)
        self.ui.btn_currenc.setStyleSheet(open("css-styles/main_buttons/btn_currenc_active.css").read())

    def btn_passw_click(self):
        self.all_css()
        self.ui.stackedWidget.setCurrentWidget(self.ui.passw_widget)
        self.ui.btn_passw.setStyleSheet(open("css-styles/main_buttons/btn_passw_active.css").read())

    def btn_books_click(self):
        self.all_css()
        self.ui.stackedWidget.setCurrentWidget(self.ui.books_widget)
        self.ui.btn_books.setStyleSheet(open("css-styles/main_buttons/btn_books_active.css").read())






    def actions_for_close_minimize_fullscr_buttons(self):

        # Minimize window
        self.ui.minimizeWindowButton.clicked.connect(lambda: self.showMinimized())

        # Close window
        self.ui.closeWindowButton.clicked.connect(lambda: self.close())

        # Restore/Maximize window
        self.ui.restoreWindowButton.clicked.connect(lambda: self.restore_or_maximize_window())

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def mousePressEvent(self, event):
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()


if __name__ == "__main__":
    # execute all only if run from this script

    # QApllication - entry point to our application (only one instance)
    # sys.argv - arguments, which may be send to cmd when our application starting
    suppress_qt_warnings()
    app = QApplication(argv)

    progress = Progress()
    center(progress)
    progress.show()

    window = MainWindow()
    center(window)

    progress.potok(window, progress)

    # sys.exit - exit from Python, app.exec_() - eternal cycle of events
    exit(app.exec_())
