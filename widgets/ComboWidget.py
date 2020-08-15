from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import Qt

class ComboWidget(QComboBox):
    def __init__(self, color, border, size, fontStyle, parent = None, width = 30):
        super().__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('ComboWidget { background-color: %s; border-radius: %d; font: %dpt %s; } \
        					QComboBox::drop-down { \
			    				width: %dpx; \
			    				border-top-right-radius: 3px; border-bottom-right-radius: 3px;} \
			    			QComboBox::down-arrow { border-left: 8px solid none; border-right: 8px solid none; border-top: 8px solid black; width: 0px; height: 0px; margin-right: 8px; }' \
							% (color, border, size, fontStyle, width))


