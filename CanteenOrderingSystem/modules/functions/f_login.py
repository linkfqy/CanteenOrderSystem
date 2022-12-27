from modules import AbstractMainWindow, DbUtil, saltify
from PySide6.QtWidgets import QMessageBox

UNLOGIN = -1
USERLOGIN = 1
ADMINLOGIN = 2
TRADERLOGIN = 3


class LoginFunctions(AbstractMainWindow):
    '''注册/登录相关函数'''

    def widgetInit(self):
        '''相关部件状态初始化'''
        self.radio_user.setChecked(True)

    @classmethod
    def allConnect(cls, self: AbstractMainWindow):
        '''绑定按钮和信号'''
        self.btn_login.clicked.connect(lambda: cls.loginBtnClicked(self))
        self.btn_register.clicked.connect(lambda: cls.registerBtnClicked(self))
        self.btn_logout.clicked.connect(lambda: cls.logoutBtnClicked(self))

        self.loginStatusSignal.connect(lambda x: cls.loginStatusObserver(self, x))
        self.loginStatusSignal.emit(UNLOGIN)

    def loginBtnClicked(self):
        username = self.lineEdit_user_name.text()
        password = self.lineEdit_password.text()
        if '' in [username, password]:
            QMessageBox.warning(self, '警告', '请输入用户名或密码!', QMessageBox.Ok)
            return
        if self.radio_user.isChecked():
            table = 'User'
            status = USERLOGIN
            key = 'user_id'
        elif self.radio_admin.isChecked():
            table = 'CanteenAdmin'
            status = ADMINLOGIN
            key = 'admin_id'
        elif self.radio_trader.isChecked():
            table = 'Trader'
            status = TRADERLOGIN
            key = 'trader_id'
        else:
            print("????")
            return

        db = DbUtil.getInstance()
        res = db.loginVerify(table, username, saltify(password))
        if not res:
            QMessageBox.warning(self, '警告', '用户名或密码错误')
            return
        self.btn_logined_user.setText(res['name'])
        self.loginStatusSignal.emit(status)
        self.userId = res[key]
        self.userType = table
        print(f"LOGIN {self.userType}: {self.userId}")

    def registerBtnClicked(self):
        username = self.lineEdit_user_name.text()
        password = self.lineEdit_password.text()
        if '' in [username, password]:
            QMessageBox.warning(self, '警告', '用户名和密码不能为空', QMessageBox.Ok)
            return
        if self.radio_admin.isChecked() or self.radio_trader.isChecked():
            QMessageBox.warning(self, '警告', '只能注册普通用户', QMessageBox.Ok)
            return
        if not self.radio_user.isChecked():
            print("???")

        db = DbUtil.getInstance()
        if db.userExist(username):
            QMessageBox.warning(self, '警告', '用户已存在')
            return
        db.addUser((username, saltify(password)))
        QMessageBox.information(self, '注册成功', '注册成功，请登录', QMessageBox.Ok)

    def logoutBtnClicked(self):
        self.loginStatusSignal.emit(UNLOGIN)
        self.userId = None
        self.userType = ''

    def loginStatusObserver(self, login_status):
        if login_status == UNLOGIN:
            self.loginArea.setVisible(True)
            self.contentSettings.setVisible(False)
        elif login_status == USERLOGIN:
            self.loginArea.setVisible(False)
            self.contentSettings.setVisible(True)
            self.btn_logined_user.setText(self.btn_logined_user.text()+"\n普通用户")
        elif login_status == ADMINLOGIN:
            self.loginArea.setVisible(False)
            self.contentSettings.setVisible(True)
            self.btn_logined_user.setText(self.btn_logined_user.text()+"\n食堂管理员")
        elif login_status == TRADERLOGIN:
            self.loginArea.setVisible(False)
            self.contentSettings.setVisible(True)
            self.btn_logined_user.setText(self.btn_logined_user.text()+"\n商家")
        else:
            print("UNKNOW STATUS!!!")
