from PyQt5.QtGui import QPainter
from LabelWidget import *
class CodeWidget(LabelWidget):
    def __init__(self, color, border, parent = None):
        super().__init__(color, border, parent)
        self.hasParent = False
        self.hasChild = False
        self.color = color
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(0,0,self.width(), self.height() / 2, QColor(self.color))
    
    
        

