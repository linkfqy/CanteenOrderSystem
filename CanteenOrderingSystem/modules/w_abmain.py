from abc import abstractmethod

from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Signal
from . import Ui_MainWindow

class AbstractMainWindow(QMainWindow, Ui_MainWindow):
    # 用户登录状态信号，用于动态显示控件以及业务逻辑
    loginStatusSignal = Signal(int)
    userId = None
    userType = ''
    canteenSelectSignal = Signal(int)
    ordered_dishes = []
    dictOrderStatus = {1:"已下单",2:"已接单",3:"已送达",4:"已评价"}

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def launch(self):
        pass