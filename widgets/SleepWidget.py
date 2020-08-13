from .CodeWidget import *
from .SpinWidget import *
from .ComboWidget import *

class SleepWidget(CodeWidget):
    def __init__(self, parent):
        super().__init__('#5188BC', 15, parent)
        self.spinTime = SpinWidget(self)
        self.spinTime.setGeometry(10,15,50,40)
        self.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.setText('동안 쉬기  ')

        self.comboWidget = ComboWidget('white', 8, 13, "나눔스퀘어", self, 15)
        self.comboWidget.setGeometry(70,15,50,40)