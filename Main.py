import Source_rc
import sys
import os
import PySide6
from pathlib import Path, PureWindowsPath
from PyQt5.QtGui import QColor, QFocusEvent
from PyQt5 import QtGui, QtCore
from PyQt5.uic import loadUi
from PyQt5.QtCore import (
    QPropertyAnimation,
    QEasingCurve,
    Qt,
    QPoint,
    QEvent

)
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
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
        self.header.installEventFilter(self)
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
        for w in self.widgetLft.findChildren(QPushButton):
            w.clicked.connect(self.applyButtonStyle)

        # Defining items in the combobox objects
        Afps = ["Capital", "Cuprum", "Habitat",
                "PlanVital", "ProVida", "Modelo", "Uno"]
        PrevisionSalud = [
            "Banmédica", "Consalud", "Colmena",
            "CruzBlanca", "Nueva Masvida", "Vida tres", "Fonasa",
        ]
        Bancos = ["Banco de Chile", "Scotiabank ", "Banco Internacional", "BCI", "Corpbanca", "BICE ", "HSBC Bank", "Santander" "Itaú",
                  "The Royal Bank of Scotland ", "Security", "Falabella", "Deutsche Bank", "Rabobank", "Ripley", "Consorcio", "Penta", "Paris"]
        TipoCuenta = ["Vista", "Ahorro", "Corriente",
                      "Valores", "Chequera electrónica", "Cuenta rut"]
        TipoContrato = ["Obra", "Fijo", "Indefinido", "Trato"]
        TipoFactura = ["Crédito", "Debito", "Nota de Credito"]

        self.CbBxTipoFactura.addItems(TipoFactura)
        self.CbBxTipoContrato.addItems(TipoContrato)
        self.CbBxTipoContrato_2.addItems(TipoContrato)
        self.CbBxNombreAFP.addItems(Afps)
        self.CbBxTipoCuenta.addItems(TipoCuenta)
        self.CbBxBanco.addItems(Bancos)
        self.CbBxAfp.addItems(Afps)
        self.CbBxPrevisionSalud.addItems(PrevisionSalud)

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
            Animations.toggle_right(
                self, self.editProyectos, self.pageDBproyectos, mb_width, stack_widht
            )

        elif connection_number == 3:

            Animations.toggle_right(
                self, self.editFacturas, self.pageDBfacturas, mb_width, stack_widht
            )

        elif connection_number == 4:
            Animations.toggle_right(
                self,
                self.editPrevisionales,
                self.pageDBprevisionales,
                mb_width,
                stack_widht,
            )
        else:
            Animations.toggle_right(
                self,
                self.editTrabajadores,
                self.pageDBtrabajadores,
                mb_width,
                stack_widht,
            )

    # _______________DEFINING GENERAL SETTINGS___________________#

    #apply style to the buttons in widgetLft
    def applyButtonStyle(self):
        #define the style
        style = str(
            "border-left: 2px solid rgb(0, 171, 179);\n"
            "border-bottom: 2px solid rgb(0, 171, 179);\n"
            "border-top: 2px solid rgb(0, 171, 179);\n"
            "background-color:rgb(30,35,40);\n"
            "border-top-left-radius:15px;\n"
            "border-bottom-left-radius:15px;"
        )
        #for each object within the widget left
        for w in self.widgetLft.findChildren(QPushButton):
            #if the button name is different from the clicked button that send the click signal
            if w.objectName() != self.sender().objectName():
                #replace and reset the style of the button
                defaultStyle = w.styleSheet().replace(style, "")
                w.setStyleSheet(defaultStyle)

        newstyle = self.sender().styleSheet() + (style)
        self.sender().setStyleSheet(newstyle)

        return

    def settings_animations(self, objct):
        objct.setDuration(600)
        objct.setEasingCurve(QEasingCurve.InQuad)
        return objct

    # ________________DEFINING MainWindow EVENTS_____________________#

    #The actions to filter when an object is triggered
    def eventFilter(self, obj, event):

        if obj == self.header:
            #turn opacitiy of the header when is moved from its postition
            if event.type() == QtCore.QEvent.MouseMove:
                self.setWindowOpacity(.8)
                #To control when is move if the mainwindow is exapanded
                if self.windowState() == Qt.WindowFullScreen:
                    self.expand_mainwindow_actions()
                #get the pointer position and move the window to its position
                delta = QPoint(event.globalPos() - self.oldposition)
                self.move(self.x() + delta.x(), self.y() + delta.y())
                self.oldposition = event.globalPos()

            #turn the opcitiy as original when the mouse is released
            if event.type() == QtCore.QEvent.MouseButtonRelease:
                self.setWindowOpacity(1)
            #when the event is double click call expand mainwindow actions method
            elif event.type() == QtCore.QEvent.MouseButtonDblClick:
                lambda: self.expand_mainwindow_actions()

        return super(MainWindow, self).eventFilter(obj, event)

    def mousePressEvent(self, event):
        self.oldposition = event.globalPos()
        # ---Launch event at double clicked---
        if event.type() == QEvent.MouseButtonDblClick:
            self.expand_mainwindow_actions()

    def expand_mainwindow_actions(self):
        #To control if there is a object inside the Stacked widget in main body content and expand with the window width
        if self.stackedWidget_2.currentWidget().width() != 0:
            self.stackedWidget.currentWidget().setMaximumWidth(16777215)
            self.stackedWidget_2.currentWidget().setMaximumWidth(16777215)

        #To show normal the window if it's axpanded
        if self.windowState() == Qt.WindowFullScreen:
            self.showNormal()
            self.expandirBtn.setIcon(QtGui.QIcon(
                ":/newPrefix/ICONS/square.png"))

        else:
            self.showFullScreen()
            self.expandirBtn.setIcon(QtGui.QIcon(
                ":/newPrefix/ICONS/multiple-file.png"))

        

# _____________________________________________________#
# WE LAUNCH EXECUTE Qapplication WITH sys.argv TO KEEPING IN LOOP THE APP.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MainWindow()
    my_app.show()
    sys.exit(app.exec())

    ###########################################################################################
    # PUT INSIDE OF CLASS MAINQINDOW
    # __________________________ONLY TO MOVE FROM ANYWHERE_________________________
    ######################################################################################
    """
        def mouseMoveEvent(self, event):
        ######################################### TO DO THIS
        #NEED TO PUT A TRY EXCEPTION TO ERROR:
        #AttributeError: 'MainWindow' object has no attribute 'oldposition'. Did you mean: 'tabPosition'?
        ##########################################

        if self.windowState() == Qt.WindowFullScreen:
            self.expand_mainwindow_actions()

        delta = QPoint(event.globalPos() - self.oldposition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldposition = event.globalPos()
    """
    ######################################################################################
