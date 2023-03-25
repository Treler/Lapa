from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QFileDialog, QLabel, QLineEdit, QSlider
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize, Qt
from ui_profile.frontend.animated_toggle import AnimatedToggle


class Profile(QWidget):
    # function of profile settings widget
    def profile_settings_window(self):
        self.profile_widget = QWidget()
        self.profile_grid = QGridLayout(self.profile_widget)
        self.profile_widget.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.central_grid.addWidget(self.profile_widget, 1, 1)

        Profile.chose_photo(self)
        Profile.settings(self)
        Profile.save_btn(self)
        Profile.user_labels(self)
        # Profile.cancel_btn(self)
        Profile.buttons_connect(self)

    def chose_photo(self):

        self.path_to_file = ""
        self.btn_chose_file = QPushButton("Выбрать файл")
        self.label_path_to_photo = QLabel("Файл не выбран")
        self.label_photo = QLabel("")

        pixmap = QPixmap("pictures/profile_photos/current_avatar.jpg")
        self.label_photo.setPixmap(pixmap)

        self.profile_grid.addWidget(self.label_photo, 1, 1, 1, 1, alignment=Qt.AlignCenter)
        self.profile_grid.addWidget(self.btn_chose_file, 2, 1, 1, 1, alignment=Qt.AlignCenter)
        self.profile_grid.addWidget(self.label_path_to_photo, 3, 1, 1, 1, alignment=Qt.AlignCenter)


    def save_btn(self):

        self.save_button = QPushButton("Сохранить")
        self.save_button.setMinimumWidth(100)
        self.save_button.setMinimumHeight(40)

        self.profile_grid.addWidget(self.save_button, 9, 6, 1, 1, alignment=Qt.AlignCenter)


    def save_actions(self):

        if self.label_path_to_photo != "Файл не выбран" and self.path_to_file != "":

            self.btn_photo.setIcon(QIcon(self.path_to_file))
            self.btn_photo.setIconSize(QSize(150, 150))

        if self.edit_nickname.text() != "":

            if len(self.edit_nickname.text()) < 16:

                self.nickname_label.setText(self.edit_nickname.text())


    def user_labels(self):

        self.label_nickname = QLabel("Nickname")
        self.edit_nickname = QLineEdit()

        self.btn_change_password = QPushButton("Сменить пароль")


        self.profile_grid.addWidget(self.label_nickname, 1, 5, 1, 1, alignment=Qt.AlignBottom)
        self.profile_grid.addWidget(self.edit_nickname, 2, 5, 1, 1, alignment=Qt.AlignTop)

        self.profile_grid.addWidget(self.btn_change_password, 3, 5, 1, 1, alignment=Qt.AlignTop)


    def settings(self):

        self.black_theme_toggle = AnimatedToggle(
            checked_color="#009900",
            pulse_checked_color="#000000"
        )

        self.black_theme_label = QLabel("Темная тема")

        self.defense_mode_toggle = AnimatedToggle()
        self.defense_mode_label = QLabel("Защищенный режим")

        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setStyleSheet("""
                    QSlider{
                        background: #FFFFFF;
                    }
                    QSlider::groove:horizontal {  
                        height: 10px;
                        margin: 0px;
                        border-radius: 5px;
                        background: #B0AEB1;
                    }
                    QSlider::handle:horizontal {
                        background: #fff;
                        border: 1px solid #E3DEE2;
                        width: 17px;
                        margin: -5px 0; 
                        border-radius: 8px;
                    }
                    QSlider::sub-page:qlineargradient {
                        background: #3B99FC;
                        border-radius: 5px;
                    }
                """)

        self.value_slider = QLabel("omg")

        self.profile_grid.addWidget(self.black_theme_toggle, 2, 10, 1, 1, alignment=Qt.AlignTop)
        self.profile_grid.addWidget(self.black_theme_label, 2, 9, 1, 1, alignment=Qt.AlignRight)

        self.profile_grid.addWidget(self.defense_mode_toggle, 3, 10, 1, 1, alignment=Qt.AlignTop)
        self.profile_grid.addWidget(self.defense_mode_label, 3, 9, 1, 1, alignment=Qt.AlignRight)

        self.profile_grid.addWidget(self.volume_slider, 4, 9, 1, 2, alignment=Qt.AlignBottom)
        self.profile_grid.addWidget(self.value_slider, 5, 9, 1, 2, alignment=Qt.AlignTop | Qt.AlignCenter)


    def change_volume_value(self):

        self.value_slider.setText(f"Volume {str(self.volume_slider.value() + 1)}%")




    # def cancel_btn(self):
    #
    #     self.cancel_button = QPushButton("Отмена")
    #     self.cancel_button.setMinimumWidth(100)
    #     self.cancel_button.setMinimumHeight(40)
    #
    #     self.profile_grid.addWidget(self.cancel_button, 9, 7, 1, 1, alignment=Qt.AlignCenter)







    def buttons_connect(self):
        self.btn_chose_file.clicked.connect(lambda: Profile.open_dialog_box(self))
        self.save_button.clicked.connect(lambda: Profile.save_actions(self))

        self.volume_slider.valueChanged.connect(lambda: Profile.change_volume_value(self))


    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        self.path_to_file = filename[0]

        self.label_path_to_photo.setText("Файл не выбран")
        if self.path_to_file != "":
            pixmap = QPixmap(self.path_to_file).scaled(150, 150)
            self.label_photo.setPixmap(pixmap)

            if len(self.path_to_file) < 20:
                self.label_path_to_photo.setText(self.path_to_file[self.path_to_file.rfind("/") + 1::])

            else:
                self.label_path_to_photo.setText("Файл выбран")

    def profile_grid_settings(self):
        self.profile_grid.setColumnStretch(0, 1)
        self.profile_grid.setColumnStretch(1, 1)
        self.profile_grid.setColumnStretch(2, 1)
        self.profile_grid.setColumnStretch(3, 1)
        self.profile_grid.setColumnStretch(4, 1)
        self.profile_grid.setColumnStretch(5, 1)
        self.profile_grid.setColumnStretch(6, 1)
        self.profile_grid.setColumnStretch(7, 1)
        self.profile_grid.setColumnStretch(8, 1)
        self.profile_grid.setColumnStretch(9, 1)
        self.profile_grid.setColumnStretch(10, 1)
        self.profile_grid.setColumnStretch(11, 1)
        self.profile_grid.setColumnStretch(12, 1)

        self.profile_grid.setRowStretch(0, 2)
        self.profile_grid.setRowStretch(1, 1)
        self.profile_grid.setRowStretch(2, 1)
        self.profile_grid.setRowStretch(3, 1)
        self.profile_grid.setRowStretch(4, 1)
        self.profile_grid.setRowStretch(5, 1)
        self.profile_grid.setRowStretch(6, 1)
        self.profile_grid.setRowStretch(7, 1)
        self.profile_grid.setRowStretch(8, 1)
        self.profile_grid.setRowStretch(9, 3)
        self.profile_grid.setRowStretch(10, 1)

