from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import Qt

class ComboButtonWidget(QComboBox):
    def __init__(self, color, border, size, fontStyle, parent = None):
        super().__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('ComboButtonWidget { background-color: %s; border-radius: %d; font: %spt %s; } \
        	QComboBox::drop-down { \
			    width: 30px; border-left-width: 1px; border-left-color: black; \
			    border-left-style: solid;\
			    border-top-right-radius: 3px; border-bottom-right-radius: 3px;} \
			    QComboBox::down-arrow { border-image: url(./arrow.png); } \
			 '\
	% (color, border, size, fontStyle))


'''
QComboBox::down-arrow { \
			    background-color : black; \
			}
'''