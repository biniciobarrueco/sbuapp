import Source_rc
import sys
import os
import PySide6
from pathlib import Path, PureWindowsPath
from PyQt5.QtGui import QColor
from PyQt5 import QtGui, QtCore
from PyQt5.uic import loadUi
from PyQt5.QtCore import (QPropertyAnimation, QEasingCurve, Qt, QPoint,
                          QPointF, QEvent, QSize, pyqtSignal, pyqtSlot)
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QGraphicsDropShadowEffect, QPushButton, QLabel,
                             QLayout, QLineEdit, QGraphicsView, QGraphicsScene,
                             QGraphicsEllipseItem, QHeaderView, QWidget,
                             QGraphicsObject, QSizeGrip, QSlider, QFrame)
from animations_sbu import Animations


# _____GETTING THE DIRECTORY WHERE WE STORE THE UI FILE______#
directory = PureWindowsPath(os.path.dirname(__file__) + "\Sistema_Empresa.ui")
file_directory = Path(directory)


# _____________BUILTED MAIN CLASS WITH THE UI APP____________#
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(file_directory, self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        #--------------------defining animations--------------------#
        # 1) widgetLft
        self.animationLftWdgt = QPropertyAnimation(self.widgetLft,
                                                   b'maximumWidth')
        self.settings_animations(self.animationLftWdgt)

        # 2) leftMenu
        self.animationLftMenu = QPropertyAnimation(self.leftMenu,
                                                   b'maximumWidth')
        self.animationLftMenu.setDuration(400)
        self.animationLftMenu.setEasingCurve(QEasingCurve.InQuad)

        #-------Setting hiden the objects of the main window at the  begin-----#
        self.rightMenu.hide()
        self.stackedWidget_2.hide()

        # ------Defining connections of the widgets within UI APP-----#
        self.salirBtn.clicked.connect(self.close)
        self.minimizarBtn.clicked.connect(self.showMinimized)
        self.expandirBtn.clicked.connect(self.expand_mainwindow_actions)
        self.miempresaBtn.clicked.connect(self.on_clicked)
        
        
# _____CREATING THE CONNECTIONS TO THE EXTERNAL MODULES______#

    def on_clicked(self):
        Animations.toggle_left(self, self.animationLftMenu, self.leftMenu)
        Animations.toggle_left(self, self.animationLftWdgt, self.widgetLft)

# _______________DEFINING GENERAL SETTINGS___________________#

    def settings_animations(self, qproperty):
        qproperty.setDuration(600)
        qproperty.setEasingCurve(QEasingCurve.InQuad)
        return qproperty
    
# ________________DEFINING MainWindow EVENTS_____________________#    
    #this action is not able to launch dblclick event specifically in the header, it works to any place where the event has been launch
    def mousePressEvent(self, event):
        self.oldposition = event.globalPos()
        #---Launch event at double clicked---
        if event.type() == QEvent.MouseButtonDblClick:
            self.expand_mainwindow_actions()

    def mouseMoveEvent(self, event):
        if self.windowState() == Qt.WindowFullScreen:
            self.expand_mainwindow_actions()

        delta = QPoint(event.globalPos() - self.oldposition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldposition = event.globalPos()
    
    
    def expand_mainwindow_actions(self):
        if self.windowState() == Qt.WindowFullScreen:
            self.showNormal()
            self.expandirBtn.setIcon(
                QtGui.QIcon(":/newPrefix/ICONS/square.png"))

        else:
            self.showFullScreen()
            self.expandirBtn.setIcon(
                QtGui.QIcon(":/newPrefix/ICONS/multiple-file.png"))
        


# _____________________________________________________#
# WE LAUNCH EXECUTE Qapplication WITH sys.argv TO KEEPING IN LOOP THE APP.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MainWindow()
    my_app.show()
    sys.exit(app.exec())
