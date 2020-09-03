from .login_gui import *
from PyQt5.QtWidgets import QDialog
import requests, json

class SignupDlg():
    def __init__(self, parent):
        self.dlg = QDialog(parent)
        self.ui = Ui_LoginDlg()
        self.ui.setupUi(self.dlg)
        self.ui.loginBtn.clicked.connect(self.onRegister)
        self.ui.signupBtn.clicked.connect(self.dlg.done)
        self.ui.title.setText('회원가입')
        self.ui.signupBtn.setText('취소')
        self.ui.loginBtn.setText('확인')
        self.dlg.exec()

    def onRegister(self):
        id = self.ui.idEdit.text()
        pw = self.ui.pwEdit.text()
        url='http://localhost:5000/signup'
        headers = {'Content-Type' : 'application/json; charset=utf-8'}
        data = {'id' : id, 'password' : pw}
        res = requests.post(url, headers = headers, data=json.dumps(data))
        if res.text == 'success':
            self.ui.title.setText('회원가입 성공!')
            self.ui.loginBtn.disconnect()
            self.ui.loginBtn.setText('확인')
            self.ui.signupBtn.hide()
            self.ui.loginBtn.clicked.connect(self.dlg.done)
        else:
            self.ui.title.setText('다시 시도하십시오.')

    def onSignUp(self):
        pass

