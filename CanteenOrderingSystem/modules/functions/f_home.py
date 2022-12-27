from modules import AbstractMainWindow, DbUtil
from . import CanteenFunctions
from PySide6.QtWidgets import QMessageBox

class HomeFunctions(AbstractMainWindow):
    '''主界面相关'''

    def widgetInit(self):
        '''相关部件状态初始化'''
        self.table_canteen.setHorizontalHeaderLabels(['食堂','综合评分','热度',''])
    
    @classmethod
    def allConnect(cls,self: AbstractMainWindow):
        self.table_canteen.cellClicked.connect(lambda x,y:cls.tableCanteenClicked(self,x,y))
        self.canteenSelectSignal.connect(lambda x:CanteenFunctions.freshCanteen(self,x))

    def tableCanteenClicked(self, row, col):
        if self.userType!='User':
            QMessageBox.warning(self,'警告','只有登录为普通用户才可以点餐',QMessageBox.Ok)
            return
        self.stackedWidget.setCurrentWidget(self.canteen_page)
        self.canteenSelectSignal.emit([4,1,3,2][row])
        