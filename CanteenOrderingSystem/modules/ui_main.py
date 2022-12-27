# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QScrollArea, QScrollBar, QSizePolicy, QSlider,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1071, 685)
        MainWindow.setMinimumSize(QSize(940, 0))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Source Han Sans SC"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"# BY: WANDERSON M.PIMENTA\n"
"# PROJECT MADE WITH: Qt Designer and PySide6\n"
"# V: 1.0.0\n"
"#\n"
"# This project can be used freely for all uses, as long as they maintain the\n"
"# respective credits only in the Python scripts, any information in the visual\n"
"# interface (GUI) can be modified without any implication.\n"
"#\n"
"# There are limitations on Qt licenses if you want to use your products\n"
"# commercially, I recommend reading them on the official website:\n"
"# https://doc.qt.io/qtforpython/licenses.html\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: #333;\n"
"	font: 12pt \"Source Han Sans SC\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
""
                        "Tooltip */\n"
"QToolTip {\n"
"	color: #333;\n"
"	background-color: #f8f8f2;\n"
"	border: 1px solid #CCC;\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-color: #f8f8f2;\n"
"	border: 1px solid #CCC;\n"
"    color: #44475a;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: #6272a4;\n"
"}\n"
"#topLogo {\n"
"	background-color: #6272a4;\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 12pt; color: #f8f8f2; }\n"
"#titleLeftDescripti"
                        "on { font: 8pt; color: #bd93f9; }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px s"
                        "olid #6a7cb1;\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: #5b6996;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: #f8f8f2;\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: #bd93f9;\n"
"}\n"
"#toggleButton:pressed {	\n"
"	background-color: #ff79c6;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: #495474;\n"
"    color: #f8f8f2;\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label"
                        " */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid #6272a4;\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: #5d6c99;\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
""
                        "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: #6272a4;\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid #bd93f9;\n"
"}\n"
"#titleRightInfo{\n"
"    color: #f8f8f2;\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: #bd93f9; border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: #ff79c6; border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: #495474; }\n"
"#themeSettingsTopDetail { background-color: #6272a4; }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: #495474 }\n"
"#bottomBar QLabel { font-size: 11px; color: #f8f8f2; padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS"
                        " */\n"
"#contentSettings .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"    color: #f8f8f2;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: #5d6c99;\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* LOGIN AREA */\n"
"#loginArea QPushButton {\n"
"	border: 2px solid #495474;\n"
"	border-radius: 5px;	\n"
"	background-color: #495474;\n"
"    color: #f8f8f2;\n"
"}\n"
"#loginArea QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"#loginArea QPushButton:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"#loginArea .QLabel{color: #f8f8f2; }\n"
"#loginArea .QRadioButton{color: #f8f8f2; }\n"
"/* //////////////////////////////////////////"
                        "///////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: #9faeda;\n"
"    outline: none;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: #9faeda;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: #9faeda;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"    color: #f8f8f2;\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: #6272a4;\n"
"	max-width: 30px;\n"
"	border: none;\n"
"	border-style: none;\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: #6272a4;\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid #6272a4;\n"
"	background-color: #6272a4;\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    color: #f8f8f2;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid #6272a4;\n"
"}\n"
"\n"
"/* /////////////////"
                        "////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"    color: #f8f8f2;\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit"
                        ":hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #6272a4;\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: #6272a4;\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: #6272a4;\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
""
                        "    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background-color: #6272a4;\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: #6272a4;\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: #6272a4;\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-posit"
                        "ion: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid #6272a4;\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: #6272a4;\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(119, 136, 187);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid #6272a4;\n"
"	width: 15p"
                        "x;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: #6272a4;\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(119, 136, 187);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid #bd93f9;\n"
"	border: 3px solid #bd93f9;	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: #6272a4;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #6272a4;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"    color: #f8f8f2;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid #7284b9;\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: #6272a4;\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-posit"
                        "ion: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: #6272a4;\n"
"	padding: 10px;\n"
"	selection-background-color: #6272a4;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: #6272a4;\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: #6272a4;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10"
                        "px;\n"
"    margin: 0px;\n"
"	background-color: #6272a4;\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: #6272a4;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"#pagesContainer QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"    border: 2px solid #ff79c6;\n"
"    color: #ff79c6;\n"
"}\n"
"#pagesContainer QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: #6272a4;\n"
"}\n"
"#pagesContainer QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249)"
                        ";\n"
"	background-color: #586796;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid #6272a4;\n"
"	border-radius: 5px;	\n"
"	background-color: #6272a4;\n"
"    color: #f8f8f2;\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: #546391;\n"
"	border: 2px solid #ff79c6;\n"
"}\n"
"\n"
"#pagesContainer QPushButton:disabled {\n"
"	color: rgb(120,120,120);\n"
"	background-color: rgb(191,191,191);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(240, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftLogo = QLabel(self.topLogoInfo)
        self.titleLeftLogo.setObjectName(u"titleLeftLogo")
        self.titleLeftLogo.setGeometry(QRect(10, 4, 42, 42))
        self.titleLeftLogo.setMinimumSize(QSize(42, 42))
        self.titleLeftLogo.setPixmap(QPixmap(u":/images/images/images/app_icon.png"))
        self.titleLeftLogo.setScaledContents(True)
        self.frame = QFrame(self.topLogoInfo)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(65, 4, 171, 41))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.titleLeftApp = QLabel(self.frame)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setFont(font)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_21.addWidget(self.titleLeftApp)

        self.titleLeftDescription = QLabel(self.frame)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font1 = QFont()
        font1.setFamilies([u"Source Han Sans SC"])
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftDescription.setFont(font1)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_21.addWidget(self.titleLeftDescription)


        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_order = QPushButton(self.topMenu)
        self.btn_order.setObjectName(u"btn_order")
        sizePolicy.setHeightForWidth(self.btn_order.sizePolicy().hasHeightForWidth())
        self.btn_order.setSizePolicy(sizePolicy)
        self.btn_order.setMinimumSize(QSize(0, 45))
        self.btn_order.setFont(font)
        self.btn_order.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_order.setLayoutDirection(Qt.LeftToRight)
        self.btn_order.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-clipboard.png);")

        self.verticalLayout_8.addWidget(self.btn_order)

        self.btn_message = QPushButton(self.topMenu)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chat-bubble.png)")

        self.verticalLayout_8.addWidget(self.btn_message)

        self.btn_trader_backstage = QPushButton(self.topMenu)
        self.btn_trader_backstage.setObjectName(u"btn_trader_backstage")
        sizePolicy.setHeightForWidth(self.btn_trader_backstage.sizePolicy().hasHeightForWidth())
        self.btn_trader_backstage.setSizePolicy(sizePolicy)
        self.btn_trader_backstage.setMinimumSize(QSize(0, 45))
        self.btn_trader_backstage.setFont(font)
        self.btn_trader_backstage.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_trader_backstage.setLayoutDirection(Qt.LeftToRight)
        self.btn_trader_backstage.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_8.addWidget(self.btn_trader_backstage)

        self.btn_admin_backstage = QPushButton(self.topMenu)
        self.btn_admin_backstage.setObjectName(u"btn_admin_backstage")
        sizePolicy.setHeightForWidth(self.btn_admin_backstage.sizePolicy().hasHeightForWidth())
        self.btn_admin_backstage.setSizePolicy(sizePolicy)
        self.btn_admin_backstage.setMinimumSize(QSize(0, 45))
        self.btn_admin_backstage.setFont(font)
        self.btn_admin_backstage.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_admin_backstage.setLayoutDirection(Qt.LeftToRight)
        self.btn_admin_backstage.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-door.png);")

        self.verticalLayout_8.addWidget(self.btn_admin_backstage)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-gamepad.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-coffee.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setAutoFillBackground(False)
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.accountTopBtn = QPushButton(self.rightButtons)
        self.accountTopBtn.setObjectName(u"accountTopBtn")
        self.accountTopBtn.setMinimumSize(QSize(28, 28))
        self.accountTopBtn.setMaximumSize(QSize(28, 28))
        self.accountTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.accountTopBtn.setIcon(icon1)
        self.accountTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.accountTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font2 = QFont()
        font2.setFamilies([u"Source Han Sans SC"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font2)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.table_canteen = QTableWidget(self.home)
        if (self.table_canteen.columnCount() < 3):
            self.table_canteen.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_canteen.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_canteen.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_canteen.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.table_canteen.rowCount() < 4):
            self.table_canteen.setRowCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_canteen.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_canteen.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_canteen.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_canteen.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_canteen.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_canteen.setItem(0, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_canteen.setItem(0, 2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_canteen.setItem(1, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_canteen.setItem(1, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_canteen.setItem(1, 2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_canteen.setItem(2, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_canteen.setItem(2, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_canteen.setItem(2, 2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_canteen.setItem(3, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_canteen.setItem(3, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_canteen.setItem(3, 2, __qtablewidgetitem18)
        self.table_canteen.setObjectName(u"table_canteen")
        self.table_canteen.setGeometry(QRect(10, 300, 791, 281))
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.table_canteen.sizePolicy().hasHeightForWidth())
        self.table_canteen.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(51, 51, 51, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush3 = QBrush(QColor(51, 51, 51, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.table_canteen.setPalette(palette)
        self.table_canteen.setFrameShape(QFrame.NoFrame)
        self.table_canteen.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table_canteen.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_canteen.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_canteen.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_canteen.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_canteen.setShowGrid(True)
        self.table_canteen.setGridStyle(Qt.SolidLine)
        self.table_canteen.setSortingEnabled(False)
        self.table_canteen.setRowCount(4)
        self.table_canteen.horizontalHeader().setVisible(True)
        self.table_canteen.horizontalHeader().setCascadingSectionResizes(True)
        self.table_canteen.horizontalHeader().setDefaultSectionSize(200)
        self.table_canteen.horizontalHeader().setStretchLastSection(True)
        self.table_canteen.verticalHeader().setVisible(False)
        self.table_canteen.verticalHeader().setCascadingSectionResizes(False)
        self.table_canteen.verticalHeader().setHighlightSections(False)
        self.table_canteen.verticalHeader().setStretchLastSection(False)
        self.label_2 = QLabel(self.home)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 270, 341, 41))
        self.label_7 = QLabel(self.home)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(-10, 0, 461, 271))
        self.label_7.setPixmap(QPixmap(u":/images/images/images/large_logo.png"))
        self.label_7.setScaledContents(True)
        self.label_11 = QLabel(self.home)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(470, 80, 224, 94))
        font3 = QFont()
        font3.setFamilies([u"Source Han Sans"])
        font3.setPointSize(20)
        font3.setBold(False)
        font3.setItalic(False)
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"font: 20pt \"Source Han Sans\";")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setWordWrap(False)
        self.stackedWidget.addWidget(self.home)
        self.canteen_page = QWidget()
        self.canteen_page.setObjectName(u"canteen_page")
        self.lbl_canteen_image = QLabel(self.canteen_page)
        self.lbl_canteen_image.setObjectName(u"lbl_canteen_image")
        self.lbl_canteen_image.setGeometry(QRect(0, 0, 420, 315))
        self.lbl_canteen_image.setMinimumSize(QSize(420, 315))
        self.lbl_canteen_image.setStyleSheet(u"")
        self.lbl_canteen_image.setPixmap(QPixmap(u":/images/images/images/large_logo.png"))
        self.lbl_canteen_image.setScaledContents(True)
        self.lbl_canteen_introduction = QLabel(self.canteen_page)
        self.lbl_canteen_introduction.setObjectName(u"lbl_canteen_introduction")
        self.lbl_canteen_introduction.setGeometry(QRect(440, 80, 361, 221))
        self.lbl_canteen_introduction.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lbl_canteen_introduction.setWordWrap(True)
        self.lbl_canteen_name = QLabel(self.canteen_page)
        self.lbl_canteen_name.setObjectName(u"lbl_canteen_name")
        self.lbl_canteen_name.setGeometry(QRect(440, 0, 321, 41))
        font4 = QFont()
        font4.setFamilies([u"Source Han Sans"])
        font4.setPointSize(24)
        font4.setBold(False)
        font4.setItalic(False)
        self.lbl_canteen_name.setFont(font4)
        self.lbl_canteen_name.setStyleSheet(u"font: 24pt \"Source Han Sans\";")
        self.lbl_canteen_contractor = QLabel(self.canteen_page)
        self.lbl_canteen_contractor.setObjectName(u"lbl_canteen_contractor")
        self.lbl_canteen_contractor.setGeometry(QRect(440, 40, 321, 21))
        self.table_canteen_orders = QTableWidget(self.canteen_page)
        if (self.table_canteen_orders.columnCount() < 2):
            self.table_canteen_orders.setColumnCount(2)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_canteen_orders.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_canteen_orders.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        if (self.table_canteen_orders.rowCount() < 9):
            self.table_canteen_orders.setRowCount(9)
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font5);
        self.table_canteen_orders.setVerticalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_canteen_orders.setVerticalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_canteen_orders.setVerticalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_canteen_orders.setItem(0, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_canteen_orders.setItem(0, 1, __qtablewidgetitem25)
        self.table_canteen_orders.setObjectName(u"table_canteen_orders")
        self.table_canteen_orders.setGeometry(QRect(400, 360, 281, 231))
        sizePolicy3.setHeightForWidth(self.table_canteen_orders.sizePolicy().hasHeightForWidth())
        self.table_canteen_orders.setSizePolicy(sizePolicy3)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush8 = QBrush(QColor(0, 0, 0, 255))
        brush8.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.table_canteen_orders.setPalette(palette1)
        self.table_canteen_orders.setFrameShape(QFrame.NoFrame)
        self.table_canteen_orders.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_canteen_orders.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_canteen_orders.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_canteen_orders.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_canteen_orders.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_canteen_orders.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_canteen_orders.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_canteen_orders.setShowGrid(True)
        self.table_canteen_orders.setGridStyle(Qt.SolidLine)
        self.table_canteen_orders.setSortingEnabled(False)
        self.table_canteen_orders.setRowCount(9)
        self.table_canteen_orders.setColumnCount(2)
        self.table_canteen_orders.horizontalHeader().setVisible(True)
        self.table_canteen_orders.horizontalHeader().setCascadingSectionResizes(True)
        self.table_canteen_orders.horizontalHeader().setDefaultSectionSize(120)
        self.table_canteen_orders.horizontalHeader().setHighlightSections(False)
        self.table_canteen_orders.horizontalHeader().setStretchLastSection(True)
        self.table_canteen_orders.verticalHeader().setVisible(False)
        self.table_canteen_orders.verticalHeader().setCascadingSectionResizes(False)
        self.table_canteen_orders.verticalHeader().setHighlightSections(False)
        self.table_canteen_orders.verticalHeader().setStretchLastSection(False)
        self.table_canteen_dish = QTableWidget(self.canteen_page)
        if (self.table_canteen_dish.columnCount() < 3):
            self.table_canteen_dish.setColumnCount(3)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table_canteen_dish.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.table_canteen_dish.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.table_canteen_dish.setHorizontalHeaderItem(2, __qtablewidgetitem28)
        if (self.table_canteen_dish.rowCount() < 9):
            self.table_canteen_dish.setRowCount(9)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font5);
        self.table_canteen_dish.setVerticalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.table_canteen_dish.setVerticalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.table_canteen_dish.setVerticalHeaderItem(2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.table_canteen_dish.setItem(0, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.table_canteen_dish.setItem(0, 1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.table_canteen_dish.setItem(0, 2, __qtablewidgetitem34)
        self.table_canteen_dish.setObjectName(u"table_canteen_dish")
        self.table_canteen_dish.setGeometry(QRect(0, 310, 401, 281))
        sizePolicy3.setHeightForWidth(self.table_canteen_dish.sizePolicy().hasHeightForWidth())
        self.table_canteen_dish.setSizePolicy(sizePolicy3)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 255))
        brush9.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush11 = QBrush(QColor(0, 0, 0, 255))
        brush11.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.table_canteen_dish.setPalette(palette2)
        self.table_canteen_dish.setFrameShape(QFrame.NoFrame)
        self.table_canteen_dish.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_canteen_dish.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_canteen_dish.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_canteen_dish.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_canteen_dish.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_canteen_dish.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_canteen_dish.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_canteen_dish.setShowGrid(True)
        self.table_canteen_dish.setGridStyle(Qt.SolidLine)
        self.table_canteen_dish.setSortingEnabled(False)
        self.table_canteen_dish.setRowCount(9)
        self.table_canteen_dish.setColumnCount(3)
        self.table_canteen_dish.horizontalHeader().setVisible(True)
        self.table_canteen_dish.horizontalHeader().setCascadingSectionResizes(True)
        self.table_canteen_dish.horizontalHeader().setDefaultSectionSize(120)
        self.table_canteen_dish.horizontalHeader().setHighlightSections(False)
        self.table_canteen_dish.horizontalHeader().setStretchLastSection(True)
        self.table_canteen_dish.verticalHeader().setVisible(False)
        self.table_canteen_dish.verticalHeader().setCascadingSectionResizes(False)
        self.table_canteen_dish.verticalHeader().setHighlightSections(False)
        self.table_canteen_dish.verticalHeader().setStretchLastSection(False)
        self.btn_canteen_clear = QPushButton(self.canteen_page)
        self.btn_canteen_clear.setObjectName(u"btn_canteen_clear")
        self.btn_canteen_clear.setGeometry(QRect(690, 400, 91, 41))
        self.btn_canteen_clear.setMinimumSize(QSize(0, 0))
        self.btn_canteen_clear.setFont(font)
        self.btn_canteen_clear.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_canteen_clear.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_canteen_clear.setIcon(icon4)
        self.btn_canteen_submit = QPushButton(self.canteen_page)
        self.btn_canteen_submit.setObjectName(u"btn_canteen_submit")
        self.btn_canteen_submit.setGeometry(QRect(690, 480, 91, 41))
        self.btn_canteen_submit.setMinimumSize(QSize(0, 0))
        self.btn_canteen_submit.setFont(font)
        self.btn_canteen_submit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_canteen_submit.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-cart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_canteen_submit.setIcon(icon5)
        self.horizontalLayoutWidget = QWidget(self.canteen_page)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(690, 320, 111, 41))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.lbl_canteen_cost = QLabel(self.horizontalLayoutWidget)
        self.lbl_canteen_cost.setObjectName(u"lbl_canteen_cost")

        self.horizontalLayout_7.addWidget(self.lbl_canteen_cost)

        self.edit_canteen_address = QLineEdit(self.canteen_page)
        self.edit_canteen_address.setObjectName(u"edit_canteen_address")
        self.edit_canteen_address.setGeometry(QRect(410, 320, 261, 41))
        self.edit_canteen_address.setMinimumSize(QSize(0, 30))
        self.edit_canteen_address.setStyleSheet(u"")
        self.stackedWidget.addWidget(self.canteen_page)
        self.order_page = QWidget()
        self.order_page.setObjectName(u"order_page")
        self.table_order_orders = QTableWidget(self.order_page)
        if (self.table_order_orders.columnCount() < 6):
            self.table_order_orders.setColumnCount(6)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.table_order_orders.setHorizontalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.table_order_orders.setHorizontalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.table_order_orders.setHorizontalHeaderItem(2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.table_order_orders.setHorizontalHeaderItem(3, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.table_order_orders.setHorizontalHeaderItem(4, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.table_order_orders.setHorizontalHeaderItem(5, __qtablewidgetitem40)
        if (self.table_order_orders.rowCount() < 8):
            self.table_order_orders.setRowCount(8)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.table_order_orders.setVerticalHeaderItem(0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.table_order_orders.setItem(0, 0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.table_order_orders.setItem(0, 1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.table_order_orders.setItem(0, 2, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.table_order_orders.setItem(0, 3, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.table_order_orders.setItem(0, 4, __qtablewidgetitem46)
        self.table_order_orders.setObjectName(u"table_order_orders")
        self.table_order_orders.setGeometry(QRect(10, 50, 781, 301))
        sizePolicy3.setHeightForWidth(self.table_order_orders.sizePolicy().hasHeightForWidth())
        self.table_order_orders.setSizePolicy(sizePolicy3)
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush12 = QBrush(QColor(0, 0, 0, 255))
        brush12.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush13 = QBrush(QColor(0, 0, 0, 255))
        brush13.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush14 = QBrush(QColor(0, 0, 0, 255))
        brush14.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.table_order_orders.setPalette(palette3)
        self.table_order_orders.setFrameShape(QFrame.NoFrame)
        self.table_order_orders.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_order_orders.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_order_orders.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_order_orders.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_order_orders.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_order_orders.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_order_orders.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_order_orders.setShowGrid(True)
        self.table_order_orders.setGridStyle(Qt.SolidLine)
        self.table_order_orders.setSortingEnabled(False)
        self.table_order_orders.setRowCount(8)
        self.table_order_orders.setColumnCount(6)
        self.table_order_orders.horizontalHeader().setVisible(True)
        self.table_order_orders.horizontalHeader().setCascadingSectionResizes(True)
        self.table_order_orders.horizontalHeader().setDefaultSectionSize(120)
        self.table_order_orders.horizontalHeader().setHighlightSections(False)
        self.table_order_orders.horizontalHeader().setStretchLastSection(True)
        self.table_order_orders.verticalHeader().setVisible(False)
        self.table_order_orders.verticalHeader().setCascadingSectionResizes(False)
        self.table_order_orders.verticalHeader().setHighlightSections(False)
        self.table_order_orders.verticalHeader().setStretchLastSection(False)
        self.combo_order_filter = QComboBox(self.order_page)
        self.combo_order_filter.addItem("")
        self.combo_order_filter.addItem("")
        self.combo_order_filter.addItem("")
        self.combo_order_filter.addItem("")
        self.combo_order_filter.addItem("")
        self.combo_order_filter.setObjectName(u"combo_order_filter")
        self.combo_order_filter.setGeometry(QRect(20, 10, 121, 40))
        self.combo_order_filter.setFont(font)
        self.combo_order_filter.setAutoFillBackground(False)
        self.combo_order_filter.setStyleSheet(u"")
        self.combo_order_filter.setIconSize(QSize(16, 16))
        self.combo_order_filter.setFrame(True)
        self.edit_comment = QPlainTextEdit(self.order_page)
        self.edit_comment.setObjectName(u"edit_comment")
        self.edit_comment.setGeometry(QRect(270, 360, 341, 221))
        self.edit_comment.setMinimumSize(QSize(0, 0))
        self.edit_comment.setStyleSheet(u"")
        self.horizontalLayoutWidget_2 = QWidget(self.order_page)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 360, 241, 41))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_8.addWidget(self.label_3)

        self.slider_rating = QSlider(self.horizontalLayoutWidget_2)
        self.slider_rating.setObjectName(u"slider_rating")
        self.slider_rating.setMinimum(0)
        self.slider_rating.setMaximum(8)
        self.slider_rating.setValue(8)
        self.slider_rating.setSliderPosition(8)
        self.slider_rating.setOrientation(Qt.Horizontal)

        self.horizontalLayout_8.addWidget(self.slider_rating)

        self.lable_rating = QLabel(self.horizontalLayoutWidget_2)
        self.lable_rating.setObjectName(u"lable_rating")

        self.horizontalLayout_8.addWidget(self.lable_rating)

        self.btn_order_comment = QPushButton(self.order_page)
        self.btn_order_comment.setObjectName(u"btn_order_comment")
        self.btn_order_comment.setGeometry(QRect(20, 420, 121, 41))
        self.btn_order_comment.setMinimumSize(QSize(0, 0))
        self.btn_order_comment.setFont(font)
        self.btn_order_comment.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_order_comment.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-comment-bubble.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_order_comment.setIcon(icon6)
        self.stackedWidget.addWidget(self.order_page)
        self.trader_backstage = QWidget()
        self.trader_backstage.setObjectName(u"trader_backstage")
        self.trader_backstage.setStyleSheet(u"")
        self.table_trader_orders = QTableWidget(self.trader_backstage)
        if (self.table_trader_orders.columnCount() < 6):
            self.table_trader_orders.setColumnCount(6)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.table_trader_orders.setHorizontalHeaderItem(0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.table_trader_orders.setHorizontalHeaderItem(1, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.table_trader_orders.setHorizontalHeaderItem(2, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.table_trader_orders.setHorizontalHeaderItem(3, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.table_trader_orders.setHorizontalHeaderItem(4, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.table_trader_orders.setHorizontalHeaderItem(5, __qtablewidgetitem52)
        if (self.table_trader_orders.rowCount() < 8):
            self.table_trader_orders.setRowCount(8)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.table_trader_orders.setVerticalHeaderItem(0, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.table_trader_orders.setItem(0, 0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.table_trader_orders.setItem(0, 1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.table_trader_orders.setItem(0, 2, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.table_trader_orders.setItem(0, 3, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.table_trader_orders.setItem(0, 4, __qtablewidgetitem58)
        self.table_trader_orders.setObjectName(u"table_trader_orders")
        self.table_trader_orders.setGeometry(QRect(0, 40, 781, 301))
        sizePolicy3.setHeightForWidth(self.table_trader_orders.sizePolicy().hasHeightForWidth())
        self.table_trader_orders.setSizePolicy(sizePolicy3)
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush15 = QBrush(QColor(0, 0, 0, 255))
        brush15.setStyle(Qt.NoBrush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush16 = QBrush(QColor(0, 0, 0, 255))
        brush16.setStyle(Qt.NoBrush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush17 = QBrush(QColor(0, 0, 0, 255))
        brush17.setStyle(Qt.NoBrush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.table_trader_orders.setPalette(palette4)
        self.table_trader_orders.setFrameShape(QFrame.NoFrame)
        self.table_trader_orders.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_trader_orders.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_trader_orders.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_trader_orders.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_trader_orders.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_trader_orders.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_trader_orders.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_trader_orders.setShowGrid(True)
        self.table_trader_orders.setGridStyle(Qt.SolidLine)
        self.table_trader_orders.setSortingEnabled(False)
        self.table_trader_orders.setRowCount(8)
        self.table_trader_orders.setColumnCount(6)
        self.table_trader_orders.horizontalHeader().setVisible(True)
        self.table_trader_orders.horizontalHeader().setCascadingSectionResizes(True)
        self.table_trader_orders.horizontalHeader().setDefaultSectionSize(120)
        self.table_trader_orders.horizontalHeader().setHighlightSections(False)
        self.table_trader_orders.horizontalHeader().setStretchLastSection(True)
        self.table_trader_orders.verticalHeader().setVisible(False)
        self.table_trader_orders.verticalHeader().setCascadingSectionResizes(False)
        self.table_trader_orders.verticalHeader().setHighlightSections(False)
        self.table_trader_orders.verticalHeader().setStretchLastSection(False)
        self.combo_trader_filter = QComboBox(self.trader_backstage)
        self.combo_trader_filter.addItem("")
        self.combo_trader_filter.addItem("")
        self.combo_trader_filter.addItem("")
        self.combo_trader_filter.addItem("")
        self.combo_trader_filter.addItem("")
        self.combo_trader_filter.setObjectName(u"combo_trader_filter")
        self.combo_trader_filter.setGeometry(QRect(10, 0, 121, 40))
        self.combo_trader_filter.setFont(font)
        self.combo_trader_filter.setAutoFillBackground(False)
        self.combo_trader_filter.setStyleSheet(u"")
        self.combo_trader_filter.setIconSize(QSize(16, 16))
        self.combo_trader_filter.setFrame(True)
        self.btn_trader_take = QPushButton(self.trader_backstage)
        self.btn_trader_take.setObjectName(u"btn_trader_take")
        self.btn_trader_take.setEnabled(False)
        self.btn_trader_take.setGeometry(QRect(300, 350, 121, 41))
        self.btn_trader_take.setMinimumSize(QSize(0, 0))
        self.btn_trader_take.setFont(font)
        self.btn_trader_take.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_trader_take.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_trader_take.setIcon(icon7)
        self.btn_trader_serve = QPushButton(self.trader_backstage)
        self.btn_trader_serve.setObjectName(u"btn_trader_serve")
        self.btn_trader_serve.setEnabled(False)
        self.btn_trader_serve.setGeometry(QRect(460, 350, 121, 41))
        self.btn_trader_serve.setMinimumSize(QSize(0, 0))
        self.btn_trader_serve.setFont(font)
        self.btn_trader_serve.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_trader_serve.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-truck.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_trader_serve.setIcon(icon8)
        self.label_trader_info1 = QLabel(self.trader_backstage)
        self.label_trader_info1.setObjectName(u"label_trader_info1")
        self.label_trader_info1.setGeometry(QRect(10, 340, 281, 241))
        self.label_trader_info1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_trader_info1.setWordWrap(False)
        self.label_trader_info2 = QLabel(self.trader_backstage)
        self.label_trader_info2.setObjectName(u"label_trader_info2")
        self.label_trader_info2.setGeometry(QRect(300, 410, 311, 171))
        self.label_trader_info2.setFont(font)
        self.label_trader_info2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_trader_info2.setWordWrap(True)
        self.stackedWidget.addWidget(self.trader_backstage)
        self.table_trader_orders.raise_()
        self.combo_trader_filter.raise_()
        self.label_trader_info1.raise_()
        self.label_trader_info2.raise_()
        self.btn_trader_take.raise_()
        self.btn_trader_serve.raise_()
        self.admin_backstage = QWidget()
        self.admin_backstage.setObjectName(u"admin_backstage")
        self.label_5 = QLabel(self.admin_backstage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(230, 270, 301, 41))
        self.stackedWidget.addWidget(self.admin_backstage)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon9)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon10)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem62)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setFont(font5);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem82)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush18 = QBrush(QColor(0, 0, 0, 255))
        brush18.setStyle(Qt.NoBrush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush18)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush19 = QBrush(QColor(0, 0, 0, 255))
        brush19.setStyle(Qt.NoBrush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush19)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush20 = QBrush(QColor(0, 0, 0, 255))
        brush20.setStyle(Qt.NoBrush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.tableWidget.setPalette(palette5)
        self.tableWidget.setStyleSheet(u"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.loginArea = QFrame(self.extraRightBox)
        self.loginArea.setObjectName(u"loginArea")
        self.loginArea.setEnabled(True)
        self.loginArea.setMinimumSize(QSize(0, 0))
        self.loginArea.setSizeIncrement(QSize(0, 0))
        self.loginArea.setFrameShape(QFrame.NoFrame)
        self.loginArea.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.loginArea)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_password = QLabel(self.loginArea)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_password, 1, 0, 1, 1)

        self.lineEdit_user_name = QLineEdit(self.loginArea)
        self.lineEdit_user_name.setObjectName(u"lineEdit_user_name")
        self.lineEdit_user_name.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit_user_name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_user_name.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lineEdit_user_name.setClearButtonEnabled(False)

        self.gridLayout_4.addWidget(self.lineEdit_user_name, 0, 1, 1, 1)

        self.label_usertype = QLabel(self.loginArea)
        self.label_usertype.setObjectName(u"label_usertype")
        self.label_usertype.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_usertype, 2, 0, 1, 1)

        self.frame_2 = QFrame(self.loginArea)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_2)
        self.verticalLayout_24.setSpacing(6)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.radio_user = QRadioButton(self.frame_2)
        self.radio_user.setObjectName(u"radio_user")

        self.verticalLayout_24.addWidget(self.radio_user)

        self.radio_admin = QRadioButton(self.frame_2)
        self.radio_admin.setObjectName(u"radio_admin")

        self.verticalLayout_24.addWidget(self.radio_admin)

        self.radio_trader = QRadioButton(self.frame_2)
        self.radio_trader.setObjectName(u"radio_trader")

        self.verticalLayout_24.addWidget(self.radio_trader)


        self.gridLayout_4.addWidget(self.frame_2, 2, 1, 1, 1, Qt.AlignTop)

        self.lineEdit_password = QLineEdit(self.loginArea)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setMaxLength(16)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.gridLayout_4.addWidget(self.lineEdit_password, 1, 1, 1, 1)

        self.label_user_name = QLabel(self.loginArea)
        self.label_user_name.setObjectName(u"label_user_name")
        self.label_user_name.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_user_name, 0, 0, 1, 1)


        self.verticalLayout_22.addLayout(self.gridLayout_4)

        self.frame_3 = QFrame(self.loginArea)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton {\n"
"	border-radius: 5px;	\n"
"	text-align: center;\n"
"	padding-left: 0px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_register = QPushButton(self.frame_3)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setMinimumSize(QSize(30, 30))
        self.btn_register.setFont(font)
        self.btn_register.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_register.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_register.setIconSize(QSize(0, 0))

        self.horizontalLayout_6.addWidget(self.btn_register)

        self.btn_login = QPushButton(self.frame_3)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(30, 30))
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_login.setIconSize(QSize(16, 16))

        self.horizontalLayout_6.addWidget(self.btn_login)


        self.verticalLayout_22.addWidget(self.frame_3, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.loginArea, 0, Qt.AlignTop)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setEnabled(True)
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_logined_user = QPushButton(self.topMenus)
        self.btn_logined_user.setObjectName(u"btn_logined_user")
        sizePolicy.setHeightForWidth(self.btn_logined_user.sizePolicy().hasHeightForWidth())
        self.btn_logined_user.setSizePolicy(sizePolicy)
        self.btn_logined_user.setMinimumSize(QSize(0, 64))
        self.btn_logined_user.setFont(font)
        self.btn_logined_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logined_user.setLayoutDirection(Qt.LeftToRight)
        self.btn_logined_user.setStyleSheet(u"background-image: url(:/images/images/images/UserAvatar_default.png);")

        self.verticalLayout_14.addWidget(self.btn_logined_user)

        self.btn_profile = QPushButton(self.topMenus)
        self.btn_profile.setObjectName(u"btn_profile")
        sizePolicy.setHeightForWidth(self.btn_profile.sizePolicy().hasHeightForWidth())
        self.btn_profile.setSizePolicy(sizePolicy)
        self.btn_profile.setMinimumSize(QSize(0, 45))
        self.btn_profile.setFont(font)
        self.btn_profile.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_profile.setLayoutDirection(Qt.LeftToRight)
        self.btn_profile.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-settings.png);")

        self.verticalLayout_14.addWidget(self.btn_profile)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font6 = QFont()
        font6.setFamilies([u"Source Han Sans SC"])
        font6.setBold(False)
        font6.setItalic(False)
        self.creditsLabel.setFont(font6)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.combo_trader_filter.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftLogo.setText("")
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"\u54c8\u5c14\u6ee8\u5de5\u4e1a\u5927\u5b66\uff08\u6df1\u5733\uff09", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"\u89c4\u683c\u4e25\u683c\uff0c\u529f\u592b\u5230\u5bb6", None))
        self.toggleButton.setText("")
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
        self.btn_order.setText(QCoreApplication.translate("MainWindow", u"\u8ba2\u5355", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"\u6d88\u606f", None))
        self.btn_trader_backstage.setText(QCoreApplication.translate("MainWindow", u"\u5546\u5bb6\u540e\u53f0", None))
        self.btn_admin_backstage.setText(QCoreApplication.translate("MainWindow", u"\u98df\u5802\u540e\u53f0", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Source Han Sans SC'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; color:#ffffff;\">An interface created using Python and PySide (support for PyQt),"
                        " and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt; color:#ffff"
                        "ff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"\u6821\u56ed\u98df\u5802\u5916\u9001\u70b9\u9910\u7cfb\u7edf", None))
#if QT_CONFIG(tooltip)
        self.accountTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u8d26\u6237", None))
#endif // QT_CONFIG(tooltip)
        self.accountTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        ___qtablewidgetitem = self.table_canteen.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u98df\u5802", None));
        ___qtablewidgetitem1 = self.table_canteen.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u7efc\u5408\u8bc4\u5206", None));
        ___qtablewidgetitem2 = self.table_canteen.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u70ed\u5ea6", None));
        ___qtablewidgetitem3 = self.table_canteen.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.table_canteen.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem5 = self.table_canteen.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem6 = self.table_canteen.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"4", None));

        __sortingEnabled = self.table_canteen.isSortingEnabled()
        self.table_canteen.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.table_canteen.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u8377\u56ed\u4e00\u98df\u5802", None));
        ___qtablewidgetitem8 = self.table_canteen.item(0, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"4.3", None));
        ___qtablewidgetitem9 = self.table_canteen.item(0, 2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"163", None));
        ___qtablewidgetitem10 = self.table_canteen.item(1, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u8354\u56ed\u4e00\u98df\u5802", None));
        ___qtablewidgetitem11 = self.table_canteen.item(1, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"4.0", None));
        ___qtablewidgetitem12 = self.table_canteen.item(1, 2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"184", None));
        ___qtablewidgetitem13 = self.table_canteen.item(2, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"We-Space\u5496\u5561\u5427", None));
        ___qtablewidgetitem14 = self.table_canteen.item(2, 1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"3.8", None));
        ___qtablewidgetitem15 = self.table_canteen.item(2, 2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"87", None));
        ___qtablewidgetitem16 = self.table_canteen.item(3, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u8354\u56ed\u4e8c\u98df\u5802", None));
        ___qtablewidgetitem17 = self.table_canteen.item(3, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"2.9", None));
        ___qtablewidgetitem18 = self.table_canteen.item(3, 2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"112", None));
        self.table_canteen.setSortingEnabled(__sortingEnabled)

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4eca\u65e5\u98df\u5802\u6392\u884c\u699c\uff0c\u70b9\u51fb\u8fdb\u5165\u70b9\u9910", None))
        self.label_7.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u6b22\u8fce\u4f7f\u7528\uff01\n"
"\u8bf7\u5148\u767b\u5f55\u518d\u70b9\u9910", None))
        self.lbl_canteen_image.setText("")
        self.lbl_canteen_introduction.setText(QCoreApplication.translate("MainWindow", u"\uff08\u6d4b\u8bd5\u7248\uff09\u8377\u56ed\u4e00\u98df\u5802\u8bbe\u4e00\u5c42\u3001\u4e8c\u5c42\u5c31\u9910\u533a\uff0c\u53ef\u63d0\u4f9b\u7ea61200\u4eba\u540c\u65f6\u5c31\u9910\u3002\u4e00\u5c42\u8bbe\u6709\u5f00\u996d\u4e86\uff08\u5927\u4f17\u9910\uff09\u3001\u519c\u5bb6\u74e6\u7f50\u3001\u571f\u9e21\u7c73\u7ebf\u7b49\u6863\u53e3;\u4e8c\u5c42\u8bbe\u6709\u6aac\u5927\u67b7\u3001\u9ebb\u8fa3\u9999\u9505\u3001\u81ea\u52a9\u9910\u3001\u4e2d\u9910\u5bb4\u5e2d\u7b49\u4f17\u591a\u98ce\u5473\u7a97\u53e3\uff0c\u8fd8\u8bbe\u6709\u591a\u529f\u80fd\u4f1a\u8bae\u5385\uff0c\u4e3a\u6709\u9700\u8981\u7684\u540c\u5b66\u548c\u8001\u5e08\u514d\u8d39\u63d0\u4f9b\u4f1a\u8bae\u6f14\u8bb2\u573a\u5730\u53ca\u8bbe\u5907(\u51ed\u5b66\u751f\u8bc1\u767b\u8bb0\u9884\u5b9a)\n"
"\u5730\u5740\uff1a\u6e05\u534e\u56ed\u533a\u5b66\u751f\u751f\u6d3b\u533a\n"
"\u8425\u4e1a\u65f6\u95f4\uff1a7\uff1a00\u201413\uff1a30 \uff1b16\uff1a00\u201419\uff1a30\n"
"\u670d\u52a1\u7535\u8bdd\uff1a17620424865", None))
        self.lbl_canteen_name.setText(QCoreApplication.translate("MainWindow", u"\u98df\u5802\u540d\u5b57", None))
        self.lbl_canteen_contractor.setText(QCoreApplication.translate("MainWindow", u"\u516c\u53f8\u516c\u53f8\u516c\u53f8\u516c\u53f8\u516c\u53f8\u516c\u53f8\u516c\u53f8\u516c\u53f8", None))
        ___qtablewidgetitem19 = self.table_canteen_orders.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u52a0\u8d2d\u83dc\u54c1", None));
        ___qtablewidgetitem20 = self.table_canteen_orders.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None));
        ___qtablewidgetitem21 = self.table_canteen_orders.verticalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem22 = self.table_canteen_orders.verticalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem23 = self.table_canteen_orders.verticalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled1 = self.table_canteen_orders.isSortingEnabled()
        self.table_canteen_orders.setSortingEnabled(False)
        self.table_canteen_orders.setSortingEnabled(__sortingEnabled1)

        ___qtablewidgetitem24 = self.table_canteen_dish.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u5546\u94fa", None));
        ___qtablewidgetitem25 = self.table_canteen_dish.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u83dc\u54c1", None));
        ___qtablewidgetitem26 = self.table_canteen_dish.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None));
        ___qtablewidgetitem27 = self.table_canteen_dish.verticalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem28 = self.table_canteen_dish.verticalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem29 = self.table_canteen_dish.verticalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled2 = self.table_canteen_dish.isSortingEnabled()
        self.table_canteen_dish.setSortingEnabled(False)
        self.table_canteen_dish.setSortingEnabled(__sortingEnabled2)

        self.btn_canteen_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.btn_canteen_submit.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u5355", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u603b\u4ef7\uff1a\uffe5", None))
        self.lbl_canteen_cost.setText(QCoreApplication.translate("MainWindow", u"\u603b\u4ef7", None))
        self.edit_canteen_address.setText("")
        self.edit_canteen_address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u9001\u9910\u5730\u5740", None))
        ___qtablewidgetitem30 = self.table_order_orders.horizontalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u5355\u53f7", None));
        ___qtablewidgetitem31 = self.table_order_orders.horizontalHeaderItem(1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"\u5546\u94fa", None));
        ___qtablewidgetitem32 = self.table_order_orders.horizontalHeaderItem(2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\u83dc\u54c1", None));
        ___qtablewidgetitem33 = self.table_order_orders.horizontalHeaderItem(3)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\u603b\u4ef7", None));
        ___qtablewidgetitem34 = self.table_order_orders.horizontalHeaderItem(4)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u5355\u65f6\u95f4", None));
        ___qtablewidgetitem35 = self.table_order_orders.horizontalHeaderItem(5)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"\u8ba2\u5355\u72b6\u6001", None));
        ___qtablewidgetitem36 = self.table_order_orders.verticalHeaderItem(0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled3 = self.table_order_orders.isSortingEnabled()
        self.table_order_orders.setSortingEnabled(False)
        ___qtablewidgetitem37 = self.table_order_orders.item(0, 0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem38 = self.table_order_orders.item(0, 1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u996d\u4e86", None));
        ___qtablewidgetitem39 = self.table_order_orders.item(0, 2)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"\u814a\u80a0\u7092\u82b1\u83dc\uff0c\u9999\u828b\u7ca5", None));
        ___qtablewidgetitem40 = self.table_order_orders.item(0, 3)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"30", None));
        ___qtablewidgetitem41 = self.table_order_orders.item(0, 4)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"2022-12-25 21:51:32", None));
        self.table_order_orders.setSortingEnabled(__sortingEnabled3)

        self.combo_order_filter.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6240\u6709\u8ba2\u5355", None))
        self.combo_order_filter.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5df2\u4e0b\u5355", None))
        self.combo_order_filter.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5df2\u63a5\u5355", None))
        self.combo_order_filter.setItemText(3, QCoreApplication.translate("MainWindow", u"\u5df2\u9001\u8fbe", None))
        self.combo_order_filter.setItemText(4, QCoreApplication.translate("MainWindow", u"\u5df2\u8bc4\u4ef7", None))

        self.edit_comment.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5728\u8fd9\u91cc\u5199\u4e0b\u8bc4\u8bba", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8bc4\u4ef7\uff1a", None))
        self.lable_rating.setText(QCoreApplication.translate("MainWindow", u"\uff1f\u5206", None))
        self.btn_order_comment.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u5e03\u8bc4\u4ef7", None))
        ___qtablewidgetitem42 = self.table_trader_orders.horizontalHeaderItem(0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"\u5355\u53f7", None));
        ___qtablewidgetitem43 = self.table_trader_orders.horizontalHeaderItem(1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"\u5546\u94fa", None));
        ___qtablewidgetitem44 = self.table_trader_orders.horizontalHeaderItem(2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"\u83dc\u54c1", None));
        ___qtablewidgetitem45 = self.table_trader_orders.horizontalHeaderItem(3)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"\u603b\u4ef7", None));
        ___qtablewidgetitem46 = self.table_trader_orders.horizontalHeaderItem(4)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u5355\u65f6\u95f4", None));
        ___qtablewidgetitem47 = self.table_trader_orders.horizontalHeaderItem(5)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"\u8ba2\u5355\u72b6\u6001", None));
        ___qtablewidgetitem48 = self.table_trader_orders.verticalHeaderItem(0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled4 = self.table_trader_orders.isSortingEnabled()
        self.table_trader_orders.setSortingEnabled(False)
        self.table_trader_orders.setSortingEnabled(__sortingEnabled4)

        self.combo_trader_filter.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6240\u6709\u8ba2\u5355", None))
        self.combo_trader_filter.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5df2\u4e0b\u5355", None))
        self.combo_trader_filter.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5df2\u63a5\u5355", None))
        self.combo_trader_filter.setItemText(3, QCoreApplication.translate("MainWindow", u"\u5df2\u9001\u8fbe", None))
        self.combo_trader_filter.setItemText(4, QCoreApplication.translate("MainWindow", u"\u5df2\u8bc4\u4ef7", None))

        self.btn_trader_take.setText(QCoreApplication.translate("MainWindow", u"\u63a5\u5355", None))
        self.btn_trader_serve.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u9001\u8fbe", None))
        self.label_trader_info1.setText(QCoreApplication.translate("MainWindow", u"\u8ba2\u5355\u8be6\u60c5\n"
"\u5355\u53f7\uff1a10086\n"
"\u5546\u94fa\uff1a\u67d0\u67d0\u67d0\n"
"\u83dc\u54c1\uff1a\u67d0\u67d0\u67d0\u67d0\uff0c\u67d0\u67d0\u67d0\u67d0\uff0c\u67d0\u67d0\u67d0\u67d0\n"
"\u603b\u4ef7\uff1a88\n"
"\u914d\u9001\u5730\u5740\uff1a\u67d0\u67d0\u67d0\u67d0\u67d0\u67d0\u67d0\u67d0\n"
"\u8ba2\u5355\u72b6\u6001\uff1a\u5df2\u63a5\u5355\n"
"\u4e0b\u5355\u65f6\u95f4\uff1a2022-12-25 21:51:32\n"
"\u63a5\u5355\u65f6\u95f4\uff1a2022-12-25 21:51:32\n"
"\u9001\u8fbe\u65f6\u95f4\uff1a2022-12-25 21:51:32\n"
"", None))
        self.label_trader_info2.setText(QCoreApplication.translate("MainWindow", u"\u8bc4\u5206\uff1a4\n"
"\u8bc4\u8bba\uff1a\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\u8bc4\u8bba\n"
"", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u98df\u5802\u540e\u53f0", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem49 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem50 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem51 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem52 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem53 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem54 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem55 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem56 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem57 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem58 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem59 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem60 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem61 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem62 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem63 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem64 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem65 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem66 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem67 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem68 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled5 = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem69 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem70 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem71 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem72 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled5)

        self.label_password.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.lineEdit_user_name.setText("")
        self.lineEdit_user_name.setPlaceholderText("")
        self.label_usertype.setText(QCoreApplication.translate("MainWindow", u"\u7c7b\u578b", None))
        self.radio_user.setText(QCoreApplication.translate("MainWindow", u"\u666e\u901a\u7528\u6237", None))
        self.radio_admin.setText(QCoreApplication.translate("MainWindow", u"\u98df\u5802\u7ba1\u7406\u5458", None))
        self.radio_trader.setText(QCoreApplication.translate("MainWindow", u"\u5546\u5bb6", None))
        self.lineEdit_password.setText("")
        self.label_user_name.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None))
        self.btn_register.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.btn_logined_user.setText(QCoreApplication.translate("MainWindow", u"account_name\n"
"type", None))
        self.btn_profile.setText(QCoreApplication.translate("MainWindow", u"\u4e2a\u4eba\u4fe1\u606f", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u767b\u5f55", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"by linkfqy, HITsz", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

