import requests
import sys
from PyQt5.Qt import *
import os

MAP_SCALE, x, y = 11, 0, 0


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.hLayout = QHBoxLayout(self)
        self.btn_getimage = QPushButton(self)
        self.line_x = QLineEdit(self)
        self.line_y = QLineEdit(self)
        self.image = QLabel(self)
        self.setWindowTitle('Yandex Api')
        self.setFixedSize(600, 600)
        self.pixMap = QPixmap("temp/map_image.png")

        self.btn_getimage.clicked.connect(self.update_map)
        self.initUi()

    def initUi(self):
        self.btn_getimage.setText("Получить карту")
        self.layout.addLayout(self.hLayout)
        self.hLayout.addWidget(self.btn_getimage)
        self.hLayout.addWidget(self.line_x)
        self.hLayout.addWidget(self.line_y)
        self.layout.addWidget(self.image)

    def keyPressEvent(self, event):
        global MAP_SCALE
        if str(event.key()) == "16777239":
            if MAP_SCALE > 0:
                MAP_SCALE -= 1
        elif str(event.key()) == "16777238":
            if MAP_SCALE < 17:
                MAP_SCALE += 1
        self.update_map()

    def update_map(self):
        response = requests.get(
            f"https://static-maps.yandex.ru/1.x/?ll={self.line_x.text()},{self.line_y.text()}&l=map&z={MAP_SCALE}")
        if response:
            with open("map_image.png", 'wb') as image:
                image.write(response.content)
            self.pixMap = QPixmap("map_image.png")
            self.pixMap = self.pixMap.scaledToWidth(600, Qt.SmoothTransformation)
            self.image.setPixmap(self.pixMap)
            os.remove("map_image.png")

    def keyPressEvent(self, event):
        global MAP_SCALE
        print(str(event.key()))
        if str(event.key()) == "16777239":
            if MAP_SCALE > 0:
                MAP_SCALE -= 1
        elif str(event.key()) == "16777238":
            if MAP_SCALE < 17:
                MAP_SCALE += 1
        self.update_map()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fc = Application()
    fc.show()
    sys.exit(app.exec())
