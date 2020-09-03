from .FunctionWidget import *
from .SpinWidget import *

class TimeFunctionWidget(FunctionWidget):
    def __init__(self, parent, pt):
        super().__init__(parent, pt, None, None)

        self.spinHour = SpinWidget(self)
        self.spinHour.setGeometry(18,15,60,40)
        self.spinHour.setValue(0)
        self.spinHour.setMinimum(0)
        self.spinHour.setMaximum(23)

        self.spinMinute = SpinWidget(self)
        self.spinMinute.setGeometry(105,15,60,40)
        self.spinMinute.setValue(0)
        self.spinMinute.setMinimum(0)
        self.spinMinute.setMaximum(59)
        self.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.setText('시              분  ')
        
    def sourceCode(self):
        self.code = ('time%2d%2d' % (self.spinHour.value(), self.spinMinute.value())).encode()
        return super().sourceCode()


