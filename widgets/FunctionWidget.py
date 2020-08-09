from .CodeWidget import *

class FunctionWidget(CodeWidget):
    def __init__(self, parent, pt, name, code):
        super().__init__('#202020', 25, parent)

        self.move(pt)        
        self.setParentState(True)
        self.setText(name)
        endWidget = CodeWidget('#303030', 25, parent)
        endWidget.move(pt.x(), pt.y() + self.height())
        endWidget.setChildState(True)
        endWidget.setEnableMove(False)
        self.childList = [endWidget]
        
    def moveEvent(self, e):
        y = self.pos().y() + self.height()
        for child in self.childList:
            child.move(e.pos().x(), y)
            y += child.height()
 