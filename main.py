from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from widgets.LabelWidget import *

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1500,800)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('Main { background-color: #0070C0 }')
        self.widgetBox = LabelWidget('white', 0, self)
        self.widgetBox.setGeometry(20,20,260,760)
        self.codeBox = LabelWidget('white', 0, self)
        self.codeBox.setGeometry(300,120,1180,660)

    def mousePressEvent(self, e):
        print('clicked')

    def mouseMoveEvent(self, e):
        if (e.buttons() & ~Qt.NoButton):
            print('moving')

    def mouseReleaseEvent(self, e):
        print('released')
        




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())