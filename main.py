from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from widgets.ButtonWidget import *
from widgets.ComboWidget import *
from widgets.LabelWidget import *
from widgets.CodeWidget import *

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1500,900)
        self.setFixedSize(1500, 900)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('Main { background-color: #0070AA }')
        self.widgetBox = QRect(20,20,260,860)
        self.codeBox = QRect(300,120,1180,760)

        self.setButton = ButtonWidget('white', 10, 16, '나눔스퀘어', '기기 설정', self) # 기기 설정 버튼
        self.setButton.setGeometry(1060,20,200,70)

        self.changeCombo = ComboWidget('white', 10, 16, '나눔스퀘어', self) # 기기 변경 버튼
        self.changeCombo.setGeometry(1280,20,200,70)
        self.changeCombo.addItem(' 안방 조명')
        self.changeCombo.addItem(' 거실 환풍기')
        self.changeCombo.addItem(' 거실 에어컨')

        self.temp = CodeWidget('rgb(91, 155, 213)', 15, self)
        self.temp.setGeometry(50, 50, 200, 70)
        self.temp.setAlignment(Qt.AlignCenter)
        self.temp.setText('code block : 1')

        self.humi = CodeWidget('rgb(91, 155, 213)', 15, self)
        self.humi.setGeometry(50, 140, 200, 70)
        self.humi.setAlignment(Qt.AlignCenter)
        self.humi.setText('code blck : 2')

    def paintEvent(self, e):
        qp = QPainter(self)
        qp.fillRect(self.widgetBox, QColor('white'))
        qp.fillRect(self.codeBox, QColor('white'))
        qp.end()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())