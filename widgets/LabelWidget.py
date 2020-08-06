from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

class LabelWidget(QLabel):
    def __init__(self, color, border, parent = None):
        super().__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('LabelWidget { background-color: %s; border-radius: %d; }' % (color, border))