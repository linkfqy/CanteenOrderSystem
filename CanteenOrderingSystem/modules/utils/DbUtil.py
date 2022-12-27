import pymysql
from .Singleton import Singleton


class DbUtil(Singleton):
    '''数据库相关'''

    def __init__(self) -> None:
        pass

    def connect(self, host='127.0.0.1', port=3306, user='canteen_admin', pwd='canteen_admin',
                db='canteenorderingsystem', charset='utf8'):
        with open("./secrets/passwd.txt", "r") as f:
            user, pwd = f.read().splitlines()
        self._conn = pymysql.connect(
            host=host, port=port, user=user, passwd=pwd, db=db, charset=charset)
        self._cur = self._conn.cursor()
        self._dict_cur = self._conn.cursor(pymysql.cursors.DictCursor)
        print(f"MYSQL CONNECTED: {user}@{host}:{port}")
        return self

    # def commit(self):
    #     self._conn.commit()

    # def rollback(self):
    #     self._conn.rollback()

    @classmethod
    def getInstance(cls):
        '''返回单例并重新连接数据库'''
        if not hasattr(cls, '_instance'):
            cls._instance = DbUtil()
        return cls._instance.connect()

    def queryAll(self, table, column, equal_to):
        sql = f"select * from {table} where {column}='{equal_to}'"
        count = self._dict_cur.execute(sql)
        res = self._dict_cur.fetchall()
        return res

    def userExist(self, name, table='user'):
        '''用户存在检验'''
        sql = f'''
            select {table}_id from {table}
            where name='{name}'
            '''
        count = self._cur.execute(sql)
        return count != 0

    def loginVerify(self, table, name, password) -> dict:
        '''登录验证'''
        sql = f'''
            SELECT * FROM {table}
            WHERE name='{name}' and password='{password}'
            '''
        count = self._dict_cur.execute(sql)
        if count == 0:
            return None
        elif count != 1:
            return print("用户重名????")
        return self._dict_cur.fetchall()[0]

    def addUser(self, data):
        '''（含写入操作）'''
        sql = f'''
            insert into user (name, password)
            values (%s, %s)
            '''
        self._cur.execute(sql, data)
        self._conn.commit()

    def getDish(self, canteenId):
        sql = f'''
        SELECT S.stall_id stall_id, D.dish_id dish_id,trader_id, D.name dish_name, S.name stall_name, price
        FROM canteen C, stall S, dish D
        WHERE
            C.canteen_id='{canteenId}'
            and C.canteen_id=S.canteen_id
            and S.stall_id=D.stall_id
        '''
        count = self._dict_cur.execute(sql)
        res = self._dict_cur.fetchall()
        return res

    def addOrder(self, stall_id, user_id, dish_ids, cost, address):
        '''（含写入操作）'''
        sql_orders = f'''
        INSERT INTO orders
        VALUES (NULL,{stall_id},{user_id},{cost},'{address}',1,NULL,NULL,NULL);
        '''
        self._cur.execute(sql_orders)
        order_id = self._cur.lastrowid
        for dish_id in dish_ids:
            sql_order_dish = f"INSERT INTO order_dish VALUES ({order_id},{dish_id});"
            self._cur.execute(sql_order_dish)
        self._conn.commit()

    def getOrderByUser(self, user_id, status=0):
        '''
        status = 0 : 查询所有状态的订单
        status = others : 查询指定状态订单
        '''
        sql = f'''
        SELECT
            O.order_id order_id,
            S.name stall_name,
            GROUP_CONCAT(D.name SEPARATOR '，') dish_names,
            cost, ordered_time ,status
        FROM
            user U,
            orders O,
            order_dish OD,
            dish D,
            stall S
        WHERE
            U.user_id=O.user_id
            AND O.order_id=OD.order_id
            AND OD.dish_id=D.dish_id
            AND D.stall_id=S.stall_id
            AND U.user_id={user_id}
            {f"AND O.status={status}"if status else ""}
        GROUP BY O.order_id
        ORDER BY O.ordered_time DESC
        '''
        self._dict_cur.execute(sql)
        res = self._dict_cur.fetchall()
        return res

    def getOrderByTrader(self, trader_id, status=0):
        '''
        status = 0 : 查询所有状态的订单
        status = others : 查询指定状态订单
        '''
        sql = f'''
        SELECT 
            O.order_id order_id,
            S.name stall_name,
            GROUP_CONCAT(D.name SEPARATOR '，') dish_names,
            cost,
            address,
            status,
            ordered_time,
            took_time,
            served_time
        FROM
            trader T,
            stall S,
            orders O,
            order_dish OD,
            dish D 
        WHERE
            T.trader_id=S.trader_id
            AND S.stall_id=O.stall_id
            AND O.order_id=OD.order_id
            AND OD.dish_id=D.dish_id
            AND T.trader_id={trader_id}
            {f"AND O.status={status}"if status else ""}
        GROUP BY O.order_id
        ORDER BY O.ordered_time DESC
        '''
        self._dict_cur.execute(sql)
        res = self._dict_cur.fetchall()
        return res

    def takeOrder(self, order_id):
        sql = f'''
        UPDATE orders
        SET status=2, took_time=NOW()
        WHERE order_id={order_id}
        '''
        self._cur.execute(sql)
        self._conn.commit()

    def serveOrder(self, order_id):
        sql = f'''
        UPDATE orders
        SET status=3, served_time=NOW()
        WHERE order_id={order_id}
        '''
        self._cur.execute(sql)
        self._conn.commit()

    def addComment(self, order_id, user_id, rating, content):
        '''添加评论并修改订单状态'''
        sql = f'''
        INSERT INTO comment
        VALUES (NULL,{order_id},{user_id},{rating},'{content}')
        '''
        self._cur.execute(sql)
        self._cur.execute(f"UPDATE orders SET status=4 WHERE order_id={order_id}")
        self._conn.commit()
