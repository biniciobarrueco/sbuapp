
from PyQt5 import QtGui
import Source_rc
from PyQt5.QtWidgets import QMainWindow

#______ANIMATION CLASS THAT HAS THE BEHAVIOR OF THE OBJECTS_______#
class Animations(QMainWindow):

    def toggle_left(self, animation, obj):
        
        #calculate the end postition for the menu
        width = obj.width()

        if width==0:
            #If the menu es currently hidden, show it by moving it onto the screen
            new_width=190
            self.miempresaBtn.setIcon(
                QtGui.QIcon(":/newPrefix/ICONS/angle-small-left (1).png"))
        else:
            #If the menu es currently visible, hide it by moving it off the left edge of the screen
            new_width=0
            self.miempresaBtn.setIcon(
                QtGui.QIcon(":/newPrefix/ICONS/menu-hamburguesa.png"))
        
        #set the start and end values for the animation
        animation.setStartValue(width)
        animation.setEndValue(new_width)
        animation.start()
        
    def toggle_right(self, animation1, animation2, obj1, obj2):
        
        width1=obj1.width()
        width2=obj2.width()
 
        if (width1 and width2) ==0:
            #If the widget is currently hidden, show it by moving it onto the screen
            new_width1=350
            new_width2=800
            self.stackedWidget_2.setCurrentWidget(obj2)
            self.stackedWidget.setCurrentWidget(obj1)
        else:
            #If the widget is currently visible, hide it by moving it off the left edge of the screen
            new_width1=0
            new_width2=0
        
        #set the start and end values for the animation
        animation1.setStartValue(width1)
        animation2.setStartValue(width2)
        animation1.setEndValue(new_width1)
        animation2.setEndValue(new_width2)
        animation1.start()
        animation2.start()