import Source_rc
import sys
import os
import PySide6
from pathlib import Path, PureWindowsPath
from PyQt5.QtGui import QColor
from PyQt5 import QtGui, QtCore
from PyQt5.uic import loadUi
from PyQt5.QtCore import (
    QPropertyAnimation,
    QEasingCurve,
    Qt,
    QPoint,
    QPointF,
    QEvent,
    QSize,
    pyqtSignal,
    pyqtSlot,
)
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QGraphicsDropShadowEffect,
    QPushButton,
    QLabel,
    QLayout,
    QLineEdit,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsEllipseItem,
    QHeaderView,
    QWidget,
    QGraphicsObject,
    QSizeGrip,
    QSlider,
    QFrame,
)
from animations_sbu import Animations
from Sistema_Empresa import Ui_MainWindow

# _____GETTING THE DIRECTORY WHERE WE STORE THE UI FILE______#
directory = PureWindowsPath(os.path.dirname(__file__) + "\Sistema_Empresa.ui")
file_directory = Path(directory)


# _____________MAIN CLASS BUILTED____________#
class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(file_directory, self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # --------------------defining animations--------------------#
        # 1) widgetLft
        self.animLftWdgt = QPropertyAnimation(self.widgetLft, b"maximumWidth")
        self.settings_animations(self.animLftWdgt)

        # 2) leftMenu
        self.animLftMenu = QPropertyAnimation(self.leftMenu, b"maximumWidth")
        self.animLftMenu.setDuration(400)
        self.animLftMenu.setEasingCurve(QEasingCurve.InQuad)

        # ------Defining connections of the widgets-----#
        self.salirBtn.clicked.connect(self.close)
        self.minimizarBtn.clicked.connect(self.showMinimized)
        self.expandirBtn.clicked.connect(self.expand_mainwindow_actions)
        self.miempresaBtn.clicked.connect(lambda: self.on_clicked(1))
        self.proyectosBtn.clicked.connect(lambda: self.on_clicked(2))
        self.facturasBtn.clicked.connect(lambda: self.on_clicked(3))
        self.previsionalesBtn.clicked.connect(lambda: self.on_clicked(4))
        self.trabajadoresBtn.clicked.connect(lambda: self.on_clicked(5))

        # _____CREATING THE CONNECTIONS TO THE EXTERNAL MODULES______#

    def on_clicked(self, connection_number):
        mb_width = self.stackedWidget_2.width()
        stack_widht = self.stackedWidget.width()

        if connection_number == 1:
            if self.stackedWidget_2.currentWidget().width() != 0:
                self.stackedWidget.currentWidget().setMaximumWidth(16777215)
                self.stackedWidget_2.currentWidget().setMaximumWidth(16777215)
            Animations.toggle_left(self, self.animLftMenu, self.leftMenu)
            Animations.toggle_left(self, self.animLftWdgt, self.widgetLft)

        elif connection_number == 2:
            Animations.toggle_right(self, self.editProyectos,
                                    self.pageDBproyectos, mb_width,
                                    stack_widht)

        elif connection_number == 3:
            Animations.toggle_right(self, self.editFacturas,
                                    self.pageDBfacturas, mb_width, stack_widht)

        elif connection_number == 4:
            Animations.toggle_right(self, self.editPrevisionales,
                                    self.pageDBprevisionales, mb_width,
                                    stack_widht)
        else:
            Animations.toggle_right(self, self.editTrabajadores,
                                    self.pageDBtrabajadores, mb_width,
                                    stack_widht)

    # _______________DEFINING GENERAL SETTINGS___________________#

    def settings_animations(self, objct):
        objct.setDuration(600)
        objct.setEasingCurve(QEasingCurve.InQuad)
        return objct

    # ________________DEFINING MainWindow EVENTS_____________________#

    # this action is not able to launch dblclick event specifically in the header, it works to any place where the event has been launched

    def mousePressEvent(self, event):
        self.oldposition = event.globalPos()
        # ---Launch event at double clicked---
        if event.type() == QEvent.MouseButtonDblClick:
            self.expand_mainwindow_actions()

    def mouseMoveEvent(self, event):
        if self.windowState() == Qt.WindowFullScreen:
            self.expand_mainwindow_actions()

        delta = QPoint(event.globalPos() - self.oldposition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldposition = event.globalPos()

    def expand_mainwindow_actions(self):

        if self.stackedWidget_2.currentWidget().width() != 0:
            self.stackedWidget.currentWidget().setMaximumWidth(16777215)
            self.stackedWidget_2.currentWidget().setMaximumWidth(16777215)

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
