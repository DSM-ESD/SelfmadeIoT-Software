from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt

class ButtonWidget(QPushButton):
    def __init__(self, color, border, size, fontStyle, text, parent = None):
        super().__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('ButtonWidget { background-color: %s; border-radius: %d; font: %spt %s; }' % (color, border, size, fontStyle))
        self.setText(text)