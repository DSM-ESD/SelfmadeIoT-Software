from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from widgets.ButtonWidget import *
from widgets.ComboWidget import *
from widgets.LabelWidget import *
from widgets.CodeWidget import *
from widgets.SpinWidget import *
from widgets.FunctionWidget import *
from widgets.TimeFunctionWidget import *
from widgets.SleepWidget import *

class Main(QWidget):
    releaseSignal = pyqtSignal(QWidget)
    draggingSignal = pyqtSignal(QWidget, QPoint)
    def __init__(self):
        super().__init__()
        self.resize(1500,900)
        self.setFixedSize(1500, 900)
        self.setWindowTitle('Selfmade-IoT')
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowIcon(QIcon('res/icon.ico'))
        self.setStyleSheet('Main { background-color: #0070AA }')
        self.widgetBox = QRect(20,120,260,760)
        self.codeBox = QRect(300,120,1180,760)
        self.binBox = QRect(840,20,200,70)
        self.releaseSignal.connect(self.onCodeReleased)
        self.draggingSignal.connect(self.onCodeDragging)     

        self.setButton = ButtonWidget('white', 0, 16, '나눔스퀘어 Bold', '기기 설정', self) # 기기 설정 버튼
        self.setButton.setGeometry(1060,20,200,70)
        self.setButton.clicked.connect(self.onSetModule)
        self.uploadButton = ButtonWidget('white', 0, 16, '나눔스퀘어 Bold', '업로드', self) # 기기 변경 버튼
        self.uploadButton.setGeometry(1280,20,200,70)
        self.uploadButton.clicked.connect(self.onUpload)

        self.widgetList = [None for _ in range(5)]
        self.createFunctions()
        self.createWidgets()

    def onUpload(self):
        code = b''
        for function in self.funcList:
            code += function.sourceCode()
        print(code)

    def onSetModule(self):
        pass

    def createFunctions(self):
        self.funcList = [
            FunctionWidget(self, QPoint(330,150), '계속 반복', b'loop'),
            FunctionWidget(self, QPoint(660,150), '원격 신호 1', b'sig1'),
            FunctionWidget(self, QPoint(960,150), '원격 신호 2', b'sig2'),
            TimeFunctionWidget(self, QPoint(1260,150), 'das')
        ]


    def paintEvent(self, e):
        pix = QPixmap('res/trash.png')
        qp = QPainter(self)
        rect = QRect(self.binBox)
        qp.fillRect(self.widgetBox, QColor('white'))
        qp.fillRect(self.codeBox, QColor('white'))
        qp.fillRect(rect, QColor('white'))
        rect.setRect(rect.center().x() - 20, rect.center().y() - 20, 40, 40)
        qp.drawPixmap(rect, pix)
        qp.end()

    def onCodeDragging(self, code, pos):
        for function in self.funcList:
            if code in function.childList:
                continue
            rect = function.area()
            if not rect.contains(pos):
                function.locationRefresh()
                continue
            
            for i, child in enumerate(function.childList):
                if child.geometry().contains(pos):
                    if function.isBlanked:
                        function.locationRefresh()
                    function.makeBlank(i)
                    return
    

    def onCodeReleased(self, code):
        try:
            idx = self.widgetList.index(code)
            self.widgetList[idx] = None
            self.createWidgets()
        except:
            pass        

        if self.binBox.contains(code.geometry().center()):
            code.deleteLater()
            return
        pt = code.geometry().center()
        for function in self.funcList:
            if not function.area().contains(pt):
                function.locationRefresh()
                continue
            if function.blank.contains(pt):
                if code.hasParent:
                    code.exitFunction.emit(code)
                function.addCode(code)
                
                break
            function.locationRefresh()

    def createWidgets(self):
        if not self.widgetList[0]:
            on = CodeWidget('#44BD41', 15, self, b'son')
            on.setGeometry(50, 250, 200, 70)
            on.setDraggingSignal(self.draggingSignal)
            on.setReleaseSignal(self.releaseSignal)
            on.setText('스위치 ON')
            on.show()
            self.widgetList[0] = on

        if not self.widgetList[1]:
            off = CodeWidget('#E22929', 15, self, b'soff')
            off.setGeometry(50, 350, 200, 70)
            off.setDraggingSignal(self.draggingSignal)
            off.setReleaseSignal(self.releaseSignal)
            off.setText('스위치 OFF')
            off.show()
            self.widgetList[1] = off


        if not self.widgetList[2]:
            sleep = SleepWidget(self)
            sleep.setGeometry(50, 450, 200, 70)
            sleep.setDraggingSignal(self.draggingSignal)
            sleep.setReleaseSignal(self.releaseSignal)
            sleep.show()
            self.widgetList[2] = sleep

        if not self.widgetList[3]:
            buzzon = CodeWidget('#81158A', 15, self, b'bon')
            buzzon.setGeometry(50, 550, 200, 70)
            buzzon.setDraggingSignal(self.draggingSignal)
            buzzon.setReleaseSignal(self.releaseSignal)
            buzzon.setText('부저 ON')
            buzzon.show()        
            self.widgetList[3] = buzzon

        if not self.widgetList[4]:
            buzzoff = CodeWidget('#C21066', 15, self, b'boff')
            buzzoff.setGeometry(50, 650, 200, 70)
            buzzoff.setDraggingSignal(self.draggingSignal)
            buzzoff.setReleaseSignal(self.releaseSignal)
            buzzoff.setText('부저 OFF')
            buzzoff.show()
            self.widgetList[4] = buzzoff
        
                
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())


    