from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtCore import Qt

class SpinWidget(QSpinBox):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setStyleSheet('QSpinBox { border-radius: 8px; font: 13pt" 나눔스퀘어" } \
        QSpinBox::up-arrow { border-left: 8px solid none; border-right: 8px solid none; border-bottom: 8px solid black; width: 0px; height: 0px; margin-right: 8px }\
        QSpinBox::up-button { min-width: 15px; min-height: 8px; background-color: white; border-radius: 8px}\
        QSpinBox::down-arrow { border-left: 8px solid none; border-right: 8px solid none; border-top: 8px solid black; width: 0px; height: 0px; margin-right: 8px}\
        QSpinBox::down-button { min-width: 15px; min-height: 8px; background-color: white; border-radius: 8px; }') 
        self.setAlignment(Qt.AlignCenter)