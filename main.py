from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from widgets.ButtonWidget import *
from widgets.ComboWidget import *
from widgets.LabelWidget import *
from widgets.CodeWidget import *
from widgets.FunctionWidget import *

# rgb(91, 155, 213)

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

        self.temp = CodeWidget('#000000', 15, self, self.releaseSignal, self.draggingSignal)
        self.temp.setGeometry(50, 50, 200, 70)
        self.temp.setAlignment(Qt.AlignCenter)
        self.temp.setText('code block : 1')

    def createFunctions(self):
        self.funcList = [
            FunctionWidget(self, QPoint(500,500), '반복', 'ㅇ')
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
            place = QRect(rect.x(), rect.y(), 200, 70)
            while rect.contains(place.center()):
                if place.contains(pos):
                    function.makeBlank(i)
                    return
                place.moveTop(-70)
                i += 1


    def onCodeReleased(self, code):
        print('released', code)
        pt = code.geometry().center()
        for function in self.funcList:
            if not function.area().contains(pt):
                continue
            if function.blank.contains(pt):
                function.addCode(code)
                return
        if code.hasParent:
            code.setChildState(False)
            code.setParentState(False)
            for function in self.funcList:
                if code in function.childList:
                    function.childList.remove(code)
                    function.locationRefresh()
        
                
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())