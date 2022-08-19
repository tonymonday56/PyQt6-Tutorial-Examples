#!/usr/bin/python

"""
ZetCode PyQt6 tutorial

In this example, we display an image
on the window.

Author: Jan Bodnar
Website: zetcode.com
"""

from PyQt6.QtWidgets import (QWidget, QHBoxLayout,
        QLabel, QApplication)
from PyQt6.QtGui import QPixmap
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        hbox = QHBoxLayout(self)
        pixmap1 = QPixmap('C:\\Users\\tony_\\Google Drive\\Python\\Projects\\PyQt6-Tutorial-Examples\\widgets2\\sid.jpg')
        pixmap2 = QPixmap('C:\\Users\\tony_\\Google Drive\\Python\\Projects\\PyQt6-Tutorial-Examples\\widgets2\\sid.jpg')
        pixmap3 = QPixmap('C:\\Users\\tony_\\Google Drive\\Python\\Projects\\PyQt6-Tutorial-Examples\\widgets2\\sid.jpg')
        pixmap4 = QPixmap('C:\\Users\\tony_\\Google Drive\\Python\\Projects\\PyQt6-Tutorial-Examples\\widgets2\\sid.jpg')



        lbl1 = QLabel(self)
        lbl1.setPixmap(pixmap1)
        lbl2 = QLabel(self)
        lbl2.setPixmap(pixmap2)
        lbl3 = QLabel(self)
        lbl3.setPixmap(pixmap3)
        lbl4 = QLabel(self)
        lbl4.setPixmap(pixmap4)

        hbox.addWidget(lbl1)
        hbox.addWidget(lbl2)
        hbox.addWidget(lbl3)
        hbox.addWidget(lbl4)

        self.setLayout(hbox)

        self.move(150, 100)
        self.setWindowTitle('Sid')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
