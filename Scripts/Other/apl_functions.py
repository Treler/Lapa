from PyQt5.QtWidgets import QApplication
from PIL import Image
from os import environ


def center(window):
    window.move(window.width() * -2, 0)
    desktop = QApplication.desktop()
    x = (desktop.width() - window.frameSize().width()) // 2
    y = (desktop.height() - window.frameSize().height()) // 2
    window.move(x, y)


def resize_photo(path_to_ph):
    image = Image.open(f"{path_to_ph}")
    # 40 40 - crypto-coins
    new_size = (30, 30)
    ratio = min(float(new_size[0]) / image.size[0], float(new_size[1]) / image.size[1])
    w = int(image.size[0] * ratio)
    h = int(image.size[1] * ratio)
    resized = image.resize((w, h), Image.Resampling.LANCZOS)
    resized.save("apl_icon_now.png")


def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


# resize_photo("apl_icon_old.png")
