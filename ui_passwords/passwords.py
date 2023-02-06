from PyQt5.QtWidgets import QWidget, QGridLayout


class Passwords(QWidget):
    # function of password widget
    def password_widget_window(self):
        self.passw_widget = QWidget()
        self.passw_grid = QGridLayout(self.passw_widget)
        self.passw_widget.setStyleSheet("background-color: rgb(70, 70, 70)")

    # function for firstly add a password for database
    def first_password_input_window(self):
        self.first_passw_input = QWidget()
        self.first_passw_input_grid = QGridLayout(self.first_passw_input)
        self.first_passw_input.setStyleSheet("background-color: rgb(10, 10, 10)")
        self.central_grid.addWidget(self.first_passw_input, 1, 1)
        self.first_passw_input.hide()

    # function for input password
    def password_input_window(self):
        self.passw_input = QWidget()
        self.passw_input_grid = QGridLayout(self.passw_input)
        self.passw_input.setStyleSheet("background-color: rgb(10, 10, 10)")
        self.central_grid.addWidget(self.passw_input, 1, 1)
