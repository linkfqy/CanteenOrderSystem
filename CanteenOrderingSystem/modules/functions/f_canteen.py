from modules import AbstractMainWindow, DbUtil
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from PySide6.QtGui import QPixmap


class CanteenFunctions(AbstractMainWindow):
    dishes = []
    cost = 0

    def freshCanteen(self, canteenId):
        db = DbUtil.getInstance()
        canInfo = db.queryAll('canteen', 'canteen_id', canteenId)
        if len(canInfo) != 1:
            print('CANTEEN: ????')
            return
        canInfo = canInfo[0]
        self.lbl_canteen_name.setText(canInfo['name'])
        self.lbl_canteen_contractor.setText(canInfo['contractor'])
        self.lbl_canteen_introduction.setText(canInfo['introduction'])
        self.lbl_canteen_image.setPixmap(QPixmap(canInfo['image']))

        self.dishes = db.getDish(canteenId)
        table = self.table_canteen_dish
        table.setRowCount(len(self.dishes))
        for i, dish in enumerate(self.dishes):
            table.setItem(i, 0, QTableWidgetItem(dish['stall_name']))
            table.setItem(i, 1, QTableWidgetItem(dish['dish_name']))
            table.setItem(i, 2, QTableWidgetItem(str(dish['price'])))

        self.ordered_dishes=[]
        CanteenFunctions.freshTableOrder(self)

    def widgetInit(self, canteenId):
        CanteenFunctions.freshCanteen(self,canteenId)

    @classmethod
    def allConnect(cls, self: AbstractMainWindow):
        self.table_canteen_dish.cellClicked.connect(
            lambda x, y: cls.tableDishClicked(self, x, y))
        self.table_canteen_orders.cellClicked.connect(
            lambda x, y: cls.tableOrderClicked(self, x, y))
        self.btn_canteen_clear.clicked.connect(
            lambda: cls.btnClearClicked(self))
        self.btn_canteen_submit.clicked.connect(
            lambda: cls.btnSubmitClicked(self))

    def tableDishClicked(self, row, col):
        '''点击菜品，加入购物车'''
        dish = self.dishes[row]
        self.ordered_dishes.append(dish)
        CanteenFunctions.freshTableOrder(self)

    def tableOrderClicked(self, row, col):
        '''点击购物车中菜品，删除此菜品'''
        self.ordered_dishes.pop(row)
        CanteenFunctions.freshTableOrder(self)

    def btnClearClicked(self):
        '''清空购物车'''
        self.ordered_dishes.clear()
        CanteenFunctions.freshTableOrder(self)

    def btnSubmitClicked(self):
        '''先验证已填写地址，且所有菜来自同一商铺，再提交订单'''
        address=self.edit_canteen_address.text()
        if address=='':
            QMessageBox.warning(self, '下单失败', '未填写地址', QMessageBox.Ok)
            return

        stall_id = self.ordered_dishes[0]['stall_id']
        dish_ids = []
        for dish in self.ordered_dishes:
            if dish['stall_id']!=stall_id:
                QMessageBox.warning(self, '下单失败', '所有菜品必须来自同一商铺', QMessageBox.Ok)
                return
            dish_ids.append(dish['dish_id'])
        db = DbUtil.getInstance()
        db.addOrder(stall_id, self.userId, dish_ids, self.cost, address)
        QMessageBox.information(self, '成功下单', '成功下单，请前往订单页面查看', QMessageBox.Ok)

    def freshTableOrder(self):
        table = self.table_canteen_orders
        table.setRowCount(len(self.ordered_dishes))
        self.cost = 0
        for i, dish in enumerate(self.ordered_dishes):
            table.setItem(i, 0, QTableWidgetItem(dish['dish_name']))
            table.setItem(i, 1, QTableWidgetItem(str(dish['price'])))
            self.cost += dish['price']
        self.lbl_canteen_cost.setText(str(self.cost))
