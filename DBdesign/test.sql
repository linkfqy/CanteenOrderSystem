SELECT * FROM user;
INSERT INTO user VALUES (1, 'a', '0a68f9f3cec8b3bae1682a71370bf8fb');
INSERT INTO user VALUES (2, 'b', '0a68f9f3cec8b3bae1682a71370bf8fb');
INSERT INTO user VALUES (3, 'c', '0a68f9f3cec8b3bae1682a71370bf8fb');


SELECT * FROM canteenadmin;
INSERT INTO canteenadmin VALUES (1, 'a', '0a68f9f3cec8b3bae1682a71370bf8fb');
INSERT INTO canteenadmin VALUES (2, 'b', '0a68f9f3cec8b3bae1682a71370bf8fb');
INSERT INTO canteenadmin VALUES (3, 'c', '0a68f9f3cec8b3bae1682a71370bf8fb');

SELECT * FROM trader;
INSERT INTO trader VALUES (1, 'a', '0a68f9f3cec8b3bae1682a71370bf8fb');
INSERT INTO trader VALUES (2, 'b', '0a68f9f3cec8b3bae1682a71370bf8fb');
INSERT INTO trader VALUES (3, 'c', '0a68f9f3cec8b3bae1682a71370bf8fb');


SELECT * FROM canteen;
INSERT INTO canteen VALUES (
        1,
        1,
        '荔园一食堂',
        '广州寅源餐饮服务有限公司',
        './images/canteens/liyuan1.png',
        '荔园一食堂设一层、二层就餐区，可提供约1800人就餐。一层设东北炖菜，U包包，烤肉拌饭，五谷鱼粉，小米米，麻辣香锅，大众餐，二层设自助称重和铁板炒饭及包房服务。
地址：哈工大园区学生生活区
营业时间：早餐7：00-9：00 ；中餐11:00-13:00；晚餐17:00-19:00
服务电话：13660176091'
    );
INSERT INTO canteen VALUES (
        2,
        1,
        '荔园二食堂',
        '深圳市都市嘉餐饮管理服务有限公司',
        './images/canteens/liyuan2.png',
        '荔园二食堂设一、二、三层就餐区，可提供约800人就餐。 一楼设奶茶店、鸡公煲、煲仔饭、咖喱饭、焖天下、重庆小面、巴蜀风味； 二楼设东北菜； 三楼设湘菜、粤菜、小炒、面食及包房服务。'
    );
INSERT INTO canteen VALUES (
        3,
        2,
        'We-Space咖啡吧',
        '深圳论语文化传播有限公司',
        './images/canteens/wespace.jpg',
        '大学论语咖啡吧设在深圳大学城图书馆We-Space内，提供咖啡饮品，糕点以及文具用品等服务。 We-Space,又称微空间，阅览空间，是深圳大学城图书馆为大学城师生以及社会读者打造的特色多彩图书馆之一，内有藏书18000册。 '
    );
INSERT INTO canteen VALUES (
        4,
        3,
        '荷园一食堂',
        '重庆快乐食间餐饮管理有限责任公司',
        './images/canteens/heyuan1.jpg',
        '荷园一食堂设一层、二层就餐区，可提供约1200人同时就餐。一层设有开饭了（大众餐）、农家瓦罐、土鸡米线等档口;二层设有檬大枷、麻辣香锅、自助餐、中餐宴席等众多风味窗口，还设有多功能会议厅，为有需要的同学和老师免费提供会议演讲场地及设备(凭学生证登记预定)
地址：清华园区学生生活区
营业时间：7：00—13：30 ；16：00—19：30
服务电话：17620424865+牛肉饭、煎饼侠、陈记面点、机器人蒸菜、土鸡米线、东北水饺、豆浆记忆、清真拉面等档口;二层设有檬大枷、冒泡(麻辣烫)、麻辣香锅、拌菜、自助餐、中餐宴席等众多风味窗口，还设有多功能会议厅，为有需要的同学和老师免费提供会议演讲场地及设备(凭学生证登记预定)'
    );

SELECT * FROM stall;
INSERT INTO stall VALUES (1,1,1,'大众自选');
INSERT INTO stall VALUES (2,1,1,'东北菜');
INSERT INTO stall VALUES (3,1,1,'猪肚鸡');
INSERT INTO stall VALUES (4,1,1,'麻辣烫');
INSERT INTO stall VALUES (5,1,2,'猪脚饭');
INSERT INTO stall VALUES (6,1,2,'大众自选');
INSERT INTO stall VALUES (7,1,3,'卡布奇诺');
INSERT INTO stall VALUES (8,1,4,'瓦罐汤');
INSERT INTO stall VALUES (9,1,4,'开饭了');
INSERT INTO stall VALUES (10,1,4,'土鸡米线');
INSERT INTO stall VALUES (11,1,4,'豆浆记忆');
INSERT INTO stall VALUES (12,1,4,'清真拉面');

SELECT * FROM dish;
INSERT INTO dish VALUES (1,1,'番茄炒蛋',5,NULL);
INSERT INTO dish VALUES (2,1,'大鸡排',8,NULL);
INSERT INTO dish VALUES (3,1,'红烧牛肉',10,NULL);
INSERT INTO dish VALUES (4,1,'烫青菜',4,NULL);
INSERT INTO dish VALUES (5,1,'鸭腿',10,NULL);
INSERT INTO dish VALUES (6,3,'招牌猪肚鸡',18,NULL);
INSERT INTO dish VALUES (7,7,'卡布奇诺',20,NULL);
INSERT INTO dish VALUES (8,7,'摩卡',21,NULL);
INSERT INTO dish VALUES (9,9,'萝卜牛腩',7,NULL);
INSERT INTO dish VALUES (10,9,'香芋粥',1,NULL);
INSERT INTO dish VALUES (11,9,'香煎带鱼',9,NULL);
INSERT INTO dish VALUES (12,9,'腊肠炒花菜',4,NULL);
INSERT INTO dish VALUES (13,10,'招牌米线',15,NULL);
INSERT INTO dish VALUES (14,10,'清汤米线',13,NULL);
INSERT INTO dish VALUES (15,11,'豆浆',5,NULL);
INSERT INTO dish VALUES (16,12,'拉面',10,NULL);
