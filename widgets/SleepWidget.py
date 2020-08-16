from .CodeWidget import *
from .SpinWidget import *
from .ComboWidget import *

class SleepWidget(CodeWidget):
    def __init__(self, parent):
        super().__init__('#5188BC', 15, parent)
        self.spinTime = SpinWidget(self)
        self.spinTime.setGeometry(15,15,60,40)
        self.spinTime.setValue(0)
        self.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.setText('쉬기   ')

        self.comboWidget = ComboWidget('white', 8, 13, "나눔스퀘어", self, 15)
        self.comboWidget.setGeometry(85,15,50,40)
        self.comboWidget.addItems(['ms', 's', 'm', 'h'])
        self.comboWidget.setCurrentIndex(0)

    def getCode(self):
        return ('sleep%4s%2s' % (self.spinTime.text(), self.comboWidget.currentText())).encode()
