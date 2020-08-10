from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPoint, pyqtSignal
from PyQt5.QtWidgets import QWidget
from .LabelWidget import *

class CodeWidget(LabelWidget):
    exitFunction = pyqtSignal(QWidget)
    def __init__(self, color, border, parent):
        super().__init__(color, border, parent)
        self.resize(200,70)
        
        self.onDragging = None
        self.onRelease = None
        self.hasParent = False
        self.hasChild = False
        self.enableMove = True
        self.isDragging = False
        self.color = color
        self.startPt = QPoint()
        self.setStyleSheet(self.styleSheet() + 'CodeWidget { font: 15pt 나눔스퀘어; color: white} ')
        self.setAlignment(Qt.AlignCenter)
        
    def setReleaseSignal(self, signal):
        self.onRelease = signal

    def setDraggingSignal(self, signal):
        self.onDragging = signal

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.hasChild:
            painter.fillRect(0, 0, self.width(), self.height() / 2, QColor(self.color))
        if self.hasParent:
            painter.fillRect(0, self.height() / 2, self.width(), self.height() / 2, QColor(self.color))
        painter.end()
        super().paintEvent(event)
    
    def setEnableMove(self, enable):
        self.enableMove = enable

    def setParentState(self, parent):
        self.hasParent = parent
        self.update()

    def setChildState(self, child):
        self.hasChild = child
        self.update()

    def mousePressEvent(self, e):
        if self.enableMove:
            self.isDragging = True
        self.startPt = e.pos()

    def mouseMoveEvent(self, e):
        if not self.isDragging or e.buttons() & Qt.NoButton:
            return
        pt = self.mapToParent(e.pos())
        if self.onDragging:
            self.onDragging.emit(self, pt)
        pt -= self.startPt
        self.move(pt)
        
    def mouseReleaseEvent(self, e):
        if self.isDragging and self.onRelease:
            self.onRelease.emit(self)
        self.isDragging = False
        
