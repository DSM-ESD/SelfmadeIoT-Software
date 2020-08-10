from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from widgets.ButtonWidget import *
from widgets.ComboWidget import *
from widgets.LabelWidget import *
from widgets.CodeWidget import *
from widgets.FunctionWidget import *

# 

class Main(QWidget):
    releaseSignal = pyqtSignal(QWidget)
    draggingSignal = pyqtSignal(QWidget, QPoint)
    def __init__(self):
        super().__init__()
        self.resize(1500,900)
        self.setFixedSize(1500, 900)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('Main { background-color: #0070AA }')
        self.widgetBox = QRect(20,20,260,860)
        self.codeBox = QRect(300,120,1180,760)
        self.releaseSignal.connect(self.onCodeReleased)
        self.draggingSignal.connect(self.onCodeDragging)

        self.setButton = ButtonWidget('white', 10, 16, '나눔스퀘어', '기기 설정', self) # 기기 설정 버튼
        self.setButton.setGeometry(1060,20,200,70)

        self.changeCombo = ComboWidget('white', 10, 16, '나눔스퀘어', self) # 기기 변경 버튼
        self.changeCombo.setGeometry(1280,20,200,70)
        self.changeCombo.addItem(' 안방 조명')
        self.changeCombo.addItem(' 거실 환풍기')
        self.changeCombo.addItem(' 거실 에어컨')

        self.createFunctions()

        self.temp = CodeWidget('#5B9BD5', 15, self)
        self.temp.setGeometry(50, 50, 200, 70)
        self.temp.setDraggingSignal(self.draggingSignal)
        self.temp.setReleaseSignal(self.releaseSignal)
        self.temp.setText('code block : 1')

        self.humi = CodeWidget('#5B9B00', 15, self)
        self.humi.setGeometry(50, 200, 200, 70)
        self.humi.setDraggingSignal(self.draggingSignal)
        self.humi.setReleaseSignal(self.releaseSignal)
        self.humi.setText('code block : 1')
        
    def createFunctions(self):
        self.funcList = [
            FunctionWidget(self, QPoint(500,500), '계속 반복', ''),
            FunctionWidget(self, QPoint(700,500), '원격 신호 1', '')
        ]

    def paintEvent(self, e):
        qp = QPainter(self)
        qp.fillRect(self.widgetBox, QColor('white'))
        qp.fillRect(self.codeBox, QColor('white'))
        qp.end()

    def onCodeDragging(self, code, pos):
        for function in self.funcList:
            if code in function.childList:
                continue
            i = 0
            rect = function.area()
            if not rect.contains(pos):
                function.locationRefresh()
                continue
            
            for i, child in enumerate(function.childList):
                if child.geometry().contains(pos):
                    function.makeBlank(i)
                    return


    def onCodeReleased(self, code):
        print('released', code)
        isAdded = False
        pt = code.geometry().center()
        for function in self.funcList:
            if not function.area().contains(pt):
                continue
            if function.blank.contains(pt):
                if code.hasParent:
                    code.exitFunction.emit(code)
                function.addCode(code)
                isAdded = True
                break
 
        if not isAdded and code.hasParent:
            code.exitFunction.emit(code)
        
                
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())