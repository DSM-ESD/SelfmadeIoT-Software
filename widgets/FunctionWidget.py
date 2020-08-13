from PyQt5.QtCore import QRect
from .CodeWidget import *

class FunctionWidget(CodeWidget):
    def __init__(self, parent, pt, name, code):
        super().__init__('#202020', 25, parent, code)

        self.move(pt)        
        self.setParentState(True)
        self.setText(name)
        self.isBlanked = False
        self.blankIdx = -1

        endWidget = CodeWidget('#303030', 25, parent)
        endWidget.move(pt.x(), pt.y() + self.height())
        endWidget.setChildState(True)
        endWidget.setEnableMove(False)
        self.childList = [endWidget]
    
    def sourceCode(self):
        array = self.code + b'|'
        for child in self.childList:
            if child.getCode():
                array += child.getCode() + b'|'
        return array

    def area(self):
        return QRect(self.pos().x(), self.pos().y() + 70, 200, 70 * len(self.childList) + 70)

    def onRemove(self, code):
        code.setChildState(False)
        code.setParentState(False)
        code.exitFunction.disconnect()
        self.childList.remove(code)
        self.locationRefresh()

    def addCode(self, code):
        if self.blankIdx < 0:
            return
        code.setParentState(True)
        code.setChildState(True)
        code.exitFunction.connect(self.onRemove)
        self.childList.insert(self.blankIdx, code)
        self.locationRefresh()

    def makeBlank(self, idx):
        for child in self.childList[idx:]:
            child.move(self.x(), child.y() + 70)
        self.blank = QRect(self.x(), self.y() + (idx + 1) * 70, 200, 70)
        self.blankIdx = idx
        self.isBlanked = True

    def locationRefresh(self):
        y = self.y() + self.height()
        for child in self.childList:
            child.move(self.x(), y)
            y += child.height()
        self.isBlanked = False
        self.blankIdx = -1

    def moveEvent(self, e):
        y = self.pos().y() + self.height()
        for child in self.childList:
            child.move(e.pos().x(), y)
            y += child.height()
        self.isBlanked = False
        self.blankIdx = -1
 