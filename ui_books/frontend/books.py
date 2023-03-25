from PyQt5.QtWidgets import QWidget, QGridLayout


class Books(QWidget):

    # books widget window
    def books_widget_window(self):
        self.books_widget = QWidget()
        self.books_grid = QGridLayout(self.books_widget)
        self.books_widget.setStyleSheet("background-color: rgb(200, 200, 200)")
