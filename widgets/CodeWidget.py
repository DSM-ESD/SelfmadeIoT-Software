from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPoint
from .LabelWidget import *
class CodeWidget(LabelWidget):
    def __init__(self, color, border, parent = None):
        super().__init__(color, border, parent)
        self.hasParent = False
        self.hasChild = False
        self.color = color
        
    def paintEvent(self, event):
        painter = QPainter(self)
        if self.hasParent:
            painter.fillRect(0, 0, self.width(), self.height() / 2, QColor(self.color))
        if self.hasChild:
            painter.fillRect(0, self.height() / 2, self.width(), self.height() / 2, QColor(self.color))
        painter.end()
    
    def setParentState(self, parent):
        self.hasParent(parent)
        self.update()

    def setChildState(self, child):
        self.hasParent(child)
        self.update()

    def mousePressEvent(self, e):
        self.isDragging = True

    def mouseMoveEvent(self, e):
        if not self.isDragging or e.buttons() & Qt.NoButton:
            return
        pt = self.mapToParent(QPoint(e.x(), e.y()))
        pt -= QPoint(self.width() / 2, self.height() / 2)
        self.move(pt)
        
    def mouseReleaseEvent(self, e):
        self.isDragging = False
