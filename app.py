#!/usr/bin/env python3

import sys
import subprocess
# import keyboard

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
    QTabWidget,
    QGridLayout
)
from PyQt6.QtGui import QPalette, QColor
# from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QHBoxLayout()
        # layout.addWidget(Color("red"))
        layout.addWidget(Screen_lock("Lock"))
        layout.addWidget(Shut_Down("Shutdown"))
        layout.addWidget(Restart("Restart"))
        layout.addWidget(Logout("Logout"))
  
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class Screen_lock(QPushButton):
    def __init__(self, text):
        super(Screen_lock,self).__init__()
        self.setCheckable(False)
        self.setText(text)
        self.clicked.connect(self.screen_locked)

        # if keyboard.read_key() == "L":
            # (self.screen_locked)

    def screen_locked(self):
        print("The screen was locked")
        subprocess.run("swaylock")
     
class Shut_Down(QPushButton):
    def __init__(self, text):
        super(Shut_Down, self).__init__()
        self.setCheckable(False)
        self.setText(text)
        self.clicked.connect(self.shutdown)

    def shutdown(self):
        print("The system is shutting down")
        subprocess.run(["systemctl","poweroff"],capture_output=True, text=True, timeout=1.0)

class Restart(QPushButton):
    def __init__(self, text):
        super(Restart, self).__init__()
        self.setCheckable(False)
        self.setText(text)
        self.clicked.connect(self.restart)

    def restart(self):
        print("The system is restarting")
        subprocess.run(["systemctl","reboot"],capture_output=True, text=True, timeout=1.0)


class Logout(QPushButton):
    def __init__(self, text):
        super(Logout, self).__init__()
        self.setCheckable(False)
        self.setText(text)
        self.clicked.connect(self.softreboot)

    def softreboot(self):
        print("The system is soft rebooting")
        subprocess.run(["systemctl","soft-reboot"],capture_output=True, text=True, timeout=1.0)


app = QApplication(sys.argv)
w = MainWindow()

# app.setStyleSheet("""
    # QMainWindow {
        # background-color: "green";
        # color: "white";
    # }
    # QPushButton {
        # font-size: 16px;
        # background-color: "blue";
    # }
# """)

w.show()

with open('app.css', 'r') as f:
    style = f.read()
    app.setStyleSheet(style)

app.exec()
