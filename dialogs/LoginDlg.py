from .login_gui import *
from .SignupDlg import *
from PyQt5.QtWidgets import QDialog
import requests, json

class LoginDlg():
    def __init__(self, parent):
        self.isLogOn = False
        self.dlg = QDialog(parent)
        self.ui = Ui_LoginDlg()
        self.ui.setupUi(self.dlg)
        self.ui.loginBtn.clicked.connect(self.onLogin)
        self.ui.signupBtn.clicked.connect(self.onSignUp)
        self.info = None
        self.dlg.exec()

    def onLogin(self):
        id = self.ui.idEdit.text()
        pw = self.ui.pwEdit.text()
        url='http://localhost:5000/login'
        headers = {'Content-Type' : 'application/json; charset=utf-8'}
        data = {'id' : id, 'password' : pw}
        res = requests.post(url, headers = headers, data=json.dumps(data))
        if res.text == 'success':
            self.isLogOn = True
            self.dlg.done(0)
            self.info = id, pw
        else:
            self.ui.title.setText('다시 시도하십시오.')

    def onSignUp(self):
        dlg = SignupDlg(self.dlg.parentWidget())


