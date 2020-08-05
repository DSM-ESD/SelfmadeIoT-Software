from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from widgets.LabelWidget import *
from widgets.ButtonWidget import *

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1300,800)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('Main { background-color: #0070C0 }')
        self.widgetBox = QRect(20,20,260,760)
        self.codeBox = QRect(300,120,980,660)

        self.setButton = ButtonWidget('white', 10, 15, 'Arial', '기기 설정', self) # 기기 설정 버튼
        self.setButton.setGeometry(860,20,200,80)
        self.chageButton = ButtonWidget('white', 10, 12, 'Arial', 'like', self) # 기기 변경 버튼
        self.chageButton.setGeometry(1080,20,200,80)
        self.isDragging = False
        self.temp = LabelWidget('red', 12, self)
        self.temp.setGeometry(50,50,50,50)

    def paintEvent(self, e):
        qp = QPainter(self)
        qp.fillRect(self.widgetBox, QColor('white'))
        qp.fillRect(self.codeBox, QColor('white'))
        qp.end()

    def mousePressEvent(self, e):
        if not self.widgetBox.contains(e.x(), e.y()):
            return
        self.isDragging = True

    def mouseMoveEvent(self, e):
        if not self.isDragging or e.buttons() & Qt.NoButton:
            return
        self.temp.move(e.x(), e.y())
        
    def mouseReleaseEvent(self, e):
        self.isDragging = False
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())