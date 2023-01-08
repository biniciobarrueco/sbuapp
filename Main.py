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

# _____GETTING THE DIRECTORY WHERE WE STORE THE UI FILE______#
directory = PureWindowsPath(os.path.dirname(__file__) + "\Sistema_Empresa.ui")
file_directory = Path(directory)


# _____________MAIN CLASS BUILTED____________#
class MainWindow(QMainWindow):
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

        # 3) mainBodyContent pages
        self.animDBproyectos = QPropertyAnimation(self.pageDBproyectos, b"maximumWidth")
        self.settings_animations(self.animDBproyectos)

        self.animDBtrabajadores = QPropertyAnimation(
            self.pageDBtrabajadores, b"maximumWidth"
        )
        self.settings_animations(self.animDBtrabajadores)

        self.animDBfacturas = QPropertyAnimation(self.pageDBfacturas, b"maximumWidth")
        self.settings_animations(self.animDBfacturas)

        self.animDBprevisionales = QPropertyAnimation(
            self.pageDBprevisionales, b"maximumWidth"
        )
        self.settings_animations(self.animDBprevisionales)

        # 4) rightMenu widgets
        self.animEdtProyectos = QPropertyAnimation(self.editProyectos, b"maximumWidth")
        self.settings_animations(self.animEdtProyectos)

        self.animEdtTrabajadores = QPropertyAnimation(
            self.editTrabajadores, b"maximumWidth"
        )
        self.settings_animations(self.animEdtTrabajadores)

        self.animEdtFacturas = QPropertyAnimation(
            self.editPrevisionales, b"maximumWidth"
        )
        self.settings_animations(self.animEdtFacturas)

        self.animEdtPrevisionales = QPropertyAnimation(
            self.editFacturas, b"maximumWidth"
        )
        self.settings_animations(self.animEdtPrevisionales)

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

        if connection_number == 1:
            Animations.toggle_left(self, self.animLftMenu, self.leftMenu)
            Animations.toggle_left(self, self.animLftWdgt, self.widgetLft)

        elif connection_number == 2:
            #We can do this in a toggle function to pass only a fixed width
            #widthDB=self.pageDBproyectos.width()
            #widthEdt=self.editProyectos.width()
            #if (widthDB and widthEdt) ==0:
            #    self.pageDBproyectos.setFixedWidth(800)
            #    self.editProyectos.setFixedWidth(350)
                #self.stackedWidget_2.setCurrentWidget(obj2)
                #self.stackedWidget.setCurrentWidget(obj1)
            Animations.toggle_right(
                self, 
                self.animEdtProyectos,
                self.animDBproyectos, 
                self.editProyectos, 
                self.pageDBproyectos
            )

        elif connection_number == 3:
            Animations.toggle_right(
                self, 
                self.animEdtFacturas, 
                self.animDBfacturas, 
                self.editFacturas, 
                self.pageDBfacturas
            )

        elif connection_number == 4:
            Animations.toggle_right(
                self,
                self.animEdtPrevisionales,
                self.animDBprevisionales,
                self.editPrevisionales,
                self.pageDBprevisionales,
            )
        else:
            Animations.toggle_right(
                self,
                self.animEdtTrabajadores,
                self.animDBtrabajadores,
                self.editTrabajadores,
                self.pageDBtrabajadores,
            )

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
        if self.windowState() == Qt.WindowFullScreen:
            self.showNormal()
            self.expandirBtn.setIcon(QtGui.QIcon(":/newPrefix/ICONS/square.png"))

        else:
            self.showFullScreen()
            self.expandirBtn.setIcon(QtGui.QIcon(":/newPrefix/ICONS/multiple-file.png"))


# _____________________________________________________#
# WE LAUNCH EXECUTE Qapplication WITH sys.argv TO KEEPING IN LOOP THE APP.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MainWindow()
    my_app.show()
    sys.exit(app.exec())
