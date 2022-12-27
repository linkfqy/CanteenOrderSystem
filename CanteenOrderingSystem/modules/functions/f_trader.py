from modules import AbstractMainWindow, DbUtil
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem as QTWI


class TraderBackstageFunctions(AbstractMainWindow):
    def widgetInit(self):
        self.combo_trader_filter.setCurrentIndex(0)
        TraderBackstageFunctions.freshTableOrder(self)
        self.label_trader_info1.setText("选择订单以查看详情")
        self.label_trader_info2.setText("")
        TraderBackstageFunctions.freshBtnEnable(self, 3)

    @classmethod
    def allConnect(cls, self: AbstractMainWindow):
        self.combo_trader_filter.currentIndexChanged.connect(
            lambda: cls.filterChanged(self))
        self.table_trader_orders.cellClicked.connect(
            lambda x, y: cls.tableOrderClicked(self, x, y))
        self.btn_trader_take.clicked.connect(lambda: cls.btnTakeClicked(self))
        self.btn_trader_serve.clicked.connect(lambda: cls.btnServeClicked(self))

    def freshTableOrder(self, filter=0):
        db = DbUtil.getInstance()
        self.orders = db.getOrderByTrader(self.userId, filter)
        table = self.table_trader_orders
        table.setRowCount(len(self.orders))
        for i, order in enumerate(self.orders):
            table.setItem(i, 0, QTWI(str(order['order_id'])))
            table.setItem(i, 1, QTWI(order['stall_name']))
            table.setItem(i, 2, QTWI(order['dish_names']))
            table.setItem(i, 3, QTWI(str(order['cost'])))
            table.setItem(i, 4, QTWI(str(order['ordered_time'])))
            table.setItem(i, 5, QTWI(self.dictOrderStatus[order['status']]))
        table.resizeColumnsToContents()

    def filterChanged(self):
        id = self.combo_trader_filter.currentIndex()
        TraderBackstageFunctions.freshTableOrder(self, id)

    def freshBtnEnable(self, status):
        if status == 1:
            self.btn_trader_take.setEnabled(True)
            self.btn_trader_serve.setEnabled(False)
        elif status == 2:
            self.btn_trader_take.setEnabled(False)
            self.btn_trader_serve.setEnabled(True)
        elif status == 3:
            self.btn_trader_take.setEnabled(False)
            self.btn_trader_serve.setEnabled(False)

    def tableOrderClicked(self, row, col):
        order = self.orders[row]
        status = order['status']
        self.label_trader_info1.setText(
            f"订单详情\n"
            f"单号：{order['order_id']}\n"
            f"商铺：{order['stall_name']}\n"
            f"菜品：{order['dish_names']}\n"
            f"总价：{order['cost']}\n"
            f"配送地址：{order['address']}\n"
            f"订单状态：{self.dictOrderStatus[status]}\n"
            f"下单时间：{order['ordered_time']}\n"
            f"接单时间：{order['took_time']}\n"
            f"送达时间：{order['served_time']}\n"
        )

        TraderBackstageFunctions.freshBtnEnable(self, status)

        db = DbUtil.getInstance()
        comment = db.queryAll('comment', 'order_id', order['order_id'])
        if len(comment) > 1:
            print("COMMENT: MORE THAN 1")
            return
        elif len(comment) == 0:
            self.label_trader_info2.setText("暂无评论")
            return
        comment = comment[0]
        self.label_trader_info2.setText(
            f"评分：{comment['rating']}\n"
            f"评论：{comment['content']}\n"
        )

    def btnTakeClicked(self):
        '''更新数据库状态，刷新控件信息'''
        row = self.table_trader_orders.selectedItems()[0].row()
        order = self.orders[row]
        db=DbUtil.getInstance()
        db.takeOrder(order['order_id'])
        # 刷新表格
        TraderBackstageFunctions.filterChanged(self)
        # 刷新详情和按钮状态
        TraderBackstageFunctions.tableOrderClicked(self,row,0)

    def btnServeClicked(self):
        '''更新数据库状态，刷新控件信息'''
        row = self.table_trader_orders.selectedItems()[0].row()
        order = self.orders[row]
        db=DbUtil.getInstance()
        db.serveOrder(order['order_id'])
        # 刷新表格
        TraderBackstageFunctions.filterChanged(self)
        # 刷新详情和按钮状态
        TraderBackstageFunctions.tableOrderClicked(self,row,0)
