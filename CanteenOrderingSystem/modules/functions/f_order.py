from modules import AbstractMainWindow, DbUtil
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem as QTWI


class OrderFunctions(AbstractMainWindow):
    def widgetInit(self):
        self.combo_order_filter.setCurrentIndex(0)
        self.slider_rating.setValue(self.slider_rating.maximum())
        self.edit_comment.setPlainText('')
        OrderFunctions.freshTableOrder(self)

    @classmethod
    def allConnect(cls, self: AbstractMainWindow):
        self.combo_order_filter.currentIndexChanged.connect(
            lambda: cls.filterChanged(self))
        self.slider_rating.valueChanged.connect(lambda: cls.freshRating(self))
        cls.freshRating(self)
        self.table_order_orders.itemClicked.connect(lambda: cls.freshBtnEnable(self))
        self.btn_order_comment.clicked.connect(lambda: cls.btnCommentClicked(self))

    def freshRating(self):
        self.rating = self.slider_rating.value()/(self.slider_rating.maximum() -
                                                  self.slider_rating.minimum())*4+1
        self.lable_rating.setText(f"{self.rating}分")

    def freshTableOrder(self, filter=0):
        db = DbUtil.getInstance()
        self.orders = db.getOrderByUser(self.userId, status=filter)
        table = self.table_order_orders
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
        id = self.combo_order_filter.currentIndex()
        OrderFunctions.freshTableOrder(self, id)

    def freshBtnEnable(self):
        row = self.table_order_orders.selectedItems()[0].row()
        order = self.orders[row]
        self.btn_order_comment.setEnabled(order['status'] == 3)

    def btnCommentClicked(self):
        row = self.table_order_orders.selectedItems()[0].row()
        order = self.orders[row]
        db = DbUtil.getInstance()
        db.addComment(order['order_id'], self.userId, self.rating,
                      self.edit_comment.toPlainText())
        QMessageBox.information(self,' ','已成功评价',QMessageBox.Ok)
        OrderFunctions.filterChanged(self)
        OrderFunctions.freshBtnEnable(self)
