from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPoint
from .LabelWidget import *
class CodeWidget(LabelWidget):
    def __init__(self, color, border, parent = None):
        super().__init__(color, border, parent)
        self.hasParent = False
        self.hasChild = False
        self.enableMove = True
        self.isDragging = False
        self.color = color
        self.startPt = QPoint()
        self.setStyleSheet(self.styleSheet() + 'CodeWidget { font: 15pt 나눔스퀘어; color: white} ')
        
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        if self.hasParent:
            painter.fillRect(0, 0, self.width(), self.height() / 2, QColor(self.color))
        if self.hasChild:
            painter.fillRect(0, self.height() / 2, self.width(), self.height() / 2, QColor(self.color))
        painter.end()
    
    def setEnableMove(self, enable):
        self.enableMove = enable

    def setParentState(self, parent):
        self.hasParent(parent)
        self.update()

    def setChildState(self, child):
        self.hasParent(child)
        self.update()

    def mousePressEvent(self, e):
        if self.enableMove:
            self.isDragging = True
        self.startPt = QPoint(e.x(), e.y())

    def mouseMoveEvent(self, e):
        if not self.isDragging or e.buttons() & Qt.NoButton:
            return
        pt = self.mapToParent(QPoint(e.x(), e.y()))
        pt -= self.startPt
        self.move(pt)
        
    def mouseReleaseEvent(self, e):
        self.isDragging = False
