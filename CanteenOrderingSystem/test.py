from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication,QMainWindow
from PySide6.QtCore import Signal
import sys

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(480, 240)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        LoginWindow.setMinimumSize(QtCore.QSize(480, 240))
        LoginWindow.setMaximumSize(QtCore.QSize(480, 240))
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 190, 461, 44))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_register = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setKerning(True)
        self.btn_register.setFont(font)
        self.btn_register.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_register.setAutoDefault(False)
        self.btn_register.setFlat(False)
        self.btn_register.setObjectName("btn_register")
        self.horizontalLayout_2.addWidget(self.btn_register)
        self.btn_login = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_login.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btn_login.setAutoDefault(False)
        self.btn_login.setDefault(False)
        self.btn_login.setObjectName("btn_login")
        self.horizontalLayout_2.addWidget(self.btn_login)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 70, 461, 130))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_password = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_password.setText("")
        self.lineEdit_password.setMaxLength(16)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout_2.addWidget(self.lineEdit_password, 1, 1, 1, 1)
        self.label_user_name = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_user_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_user_name.setObjectName("label_user_name")
        self.gridLayout_2.addWidget(self.label_user_name, 0, 0, 1, 1)
        self.lineEdit_user_name = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_user_name.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_user_name.setText("")
        self.lineEdit_user_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_user_name.setPlaceholderText("")
        self.lineEdit_user_name.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_user_name.setClearButtonEnabled(False)
        self.lineEdit_user_name.setObjectName("lineEdit_user_name")
        self.gridLayout_2.addWidget(self.lineEdit_user_name, 0, 1, 1, 1)
        self.label_password = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_password.setAlignment(QtCore.Qt.AlignCenter)
        self.label_password.setObjectName("label_password")
        self.gridLayout_2.addWidget(self.label_password, 1, 0, 1, 1)
        self.radio_admin = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radio_admin.setObjectName("radio_admin")
        self.gridLayout_2.addWidget(self.radio_admin, 2, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 461, 61))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.title = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.horizontalLayout_4.addWidget(self.title)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        self.btn_register.clicked['bool'].connect(LoginWindow.hide)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)
        LoginWindow.setTabOrder(self.lineEdit_user_name, self.lineEdit_password)
        LoginWindow.setTabOrder(self.lineEdit_password, self.radio_admin)
        LoginWindow.setTabOrder(self.radio_admin, self.btn_register)
        LoginWindow.setTabOrder(self.btn_register, self.btn_login)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "????"))
        self.btn_register.setText(_translate("LoginWindow", "??????"))
        self.btn_login.setText(_translate("LoginWindow", "??????"))
        self.label_user_name.setText(_translate("LoginWindow", "?????????"))
        self.label_password.setText(_translate("LoginWindow", "??????"))
        self.radio_admin.setText(_translate("LoginWindow", "???????????????"))
        self.title.setText(_translate("LoginWindow", "???? HITsz Canteen ????"))

class LoginWindow(Ui_LoginWindow, QMainWindow):
    login_done_signal = Signal(int)

    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)

if __name__=='__main__':
    app = QApplication(sys.argv)
    ui = LoginWindow()
    ui.show()
    sys.exit(app.exec_())