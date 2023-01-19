from PyQt5 import QtGui, Qt
import Source_rc
from PyQt5.QtWidgets import QMainWindow


#______ANIMATION CLASS THAT HAS THE BEHAVIOR OF THE OBJECTS_______#
class Animations(QMainWindow):

    def toggle_left(self, animation, obj):

        #calculate the end postition for the menu
        width = obj.width()

        if width == 0:
            #If the menu es currently hidden, show it by moving it onto the screen
            new_width = 190
            self.miempresaBtn.setIcon(
                QtGui.QIcon(":/newPrefix/ICONS/angle-small-left (1).png"))
        else:
            #If the menu es currently visible, hide it by moving it off the left edge of the screen
            new_width = 0
            self.miempresaBtn.setIcon(
                QtGui.QIcon(":/newPrefix/ICONS/menu-hamburguesa.png"))

        #set the start and end values for the animation

        animation.setStartValue(width)
        animation.setEndValue(new_width)
        animation.start()

    def toggle_right(self, obj1, obj2, mb_width, stack_widht):

        obj1.setMaximumWidth(stack_widht)
        obj2.setMaximumWidth(mb_width)
        self.stackedWidget_2.setCurrentWidget(obj2)
        self.stackedWidget.setCurrentWidget(obj1)

