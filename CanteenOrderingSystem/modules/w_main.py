from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from . import (
    AbstractMainWindow,
    Settings,
    AppFunctions,
    UIFunctions,
    LoginFunctions,
    HomeFunctions,
    CanteenFunctions,
    OrderFunctions,
    TraderBackstageFunctions
)

class MainWindow(AbstractMainWindow):

    def __init__(self):
        super().__init__()

    def launch(self):
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.setupUi(self)
        self.btn_widgets.setVisible(False)

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "校园食堂外送点餐系统"
        # APPLY TEXTS
        self.setWindowTitle(title)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        self.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        self.btn_home.clicked.connect(self.menuButtonClick)
        self.btn_widgets.clicked.connect(self.menuButtonClick)
        self.btn_order.clicked.connect(self.menuButtonClick)
        self.btn_message.clicked.connect(self.menuButtonClick)
        self.btn_trader_backstage.clicked.connect(self.menuButtonClick)
        self.btn_admin_backstage.clicked.connect(self.menuButtonClick)

        # EXTRA LEFT BOX
        openCloseLeftBox=lambda: UIFunctions.toggleLeftBox(self, True)
        self.toggleLeftBox.clicked.connect(openCloseLeftBox)
        self.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        openCloseRightBox=lambda: UIFunctions.toggleRightBox(self, True)
        self.accountTopBtn.clicked.connect(openCloseRightBox)

        LoginFunctions.allConnect(self)
        HomeFunctions.allConnect(self)
        CanteenFunctions.allConnect(self)
        OrderFunctions.allConnect(self)
        TraderBackstageFunctions.allConnect(self)
        

        # 部件状态初始化
        # ///////////////////////////////////////////////////////////////
        LoginFunctions.widgetInit(self)
        HomeFunctions.widgetInit(self)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = True
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        self.stackedWidget.setCurrentWidget(self.home)
        self.btn_home.setStyleSheet(UIFunctions.selectMenu(self.btn_home.styleSheet()))

    # 左侧菜单按钮响应
    def menuButtonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            self.stackedWidget.setCurrentWidget(self.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW ORDER PAGE
        if btnName == "btn_order":
            if self.userType!='User':
                QMessageBox.warning(self,' ','您的权限无法查看此内容',QMessageBox.Ok)
                return
            self.stackedWidget.setCurrentWidget(self.order_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            OrderFunctions.widgetInit(self)  # 每次进入都要刷新页面

        # SHOW trader backstage PAGE
        if btnName == "btn_trader_backstage":
            if self.userType!='Trader':
                QMessageBox.warning(self,' ','您的权限无法查看此内容',QMessageBox.Ok)
                return
            self.stackedWidget.setCurrentWidget(self.trader_backstage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            TraderBackstageFunctions.widgetInit(self)  # 每次进入都要刷新页面

        # SHOW admin backstage PAGE
        if btnName == "btn_admin_backstage":
            if self.userType!='CanteenAdmin':
                QMessageBox.warning(self,' ','您的权限无法查看此内容',QMessageBox.Ok)
                return
            self.stackedWidget.setCurrentWidget(self.admin_backstage)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            self.stackedWidget.setCurrentWidget(self.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
    
    

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        # if event.buttons() == Qt.LeftButton:
        #     print('Mouse click: LEFT CLICK')
        # if event.buttons() == Qt.RightButton:
        #     print('Mouse click: RIGHT CLICK')