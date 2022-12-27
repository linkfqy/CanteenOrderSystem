/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2022/12/27 18:40:01                          */
/*==============================================================*/


/*==============================================================*/
/* Table: Canteen                                               */
/*==============================================================*/
create table Canteen
(
   canteen_id           int not null auto_increment,
   admin_id             int not null,
   name                 varchar(16) not null,
   contractor           varchar(32) not null,
   image                varchar(256),
   introduction         varchar(512),
   primary key (canteen_id)
);

/*==============================================================*/
/* Table: CanteenAdmin                                          */
/*==============================================================*/
create table CanteenAdmin
(
   admin_id             int not null auto_increment,
   name                 varchar(16) not null,
   password             varchar(256) not null,
   primary key (admin_id)
);

/*==============================================================*/
/* Index: CanteenAdmin_name                                     */
/*==============================================================*/
create unique index CanteenAdmin_name on CanteenAdmin
(
   name
);

/*==============================================================*/
/* Table: Order_Dish                                            */
/*==============================================================*/
create table Order_Dish
(
   order_id             int not null,
   dish_id              int not null,
   primary key (order_id, dish_id)
);

/*==============================================================*/
/* Table: Orders                                                */
/*==============================================================*/
create table Orders
(
   order_id             int not null auto_increment,
   stall_id             int not null,
   user_id              int not null,
   cost                 decimal(5,2) not null,
   address              varchar(256) not null,
   status               int not null,
   ordered_time         timestamp not null,
   took_time            timestamp,
   served_time          timestamp,
   primary key (order_id)
);

/*==============================================================*/
/* Table: Stall                                                 */
/*==============================================================*/
create table Stall
(
   stall_id             int not null auto_increment,
   trader_id            int not null,
   canteen_id           int not null,
   name                 varchar(16) not null,
   primary key (stall_id)
);

/*==============================================================*/
/* Table: Trader                                                */
/*==============================================================*/
create table Trader
(
   trader_id            int not null auto_increment,
   name                 varchar(16) not null,
   password             varchar(256) not null,
   primary key (trader_id)
);

/*==============================================================*/
/* Index: Trader_name                                           */
/*==============================================================*/
create unique index Trader_name on Trader
(
   name
);

/*==============================================================*/
/* Table: User                                                  */
/*==============================================================*/
create table User
(
   user_id              int not null auto_increment,
   name                 varchar(16) not null,
   password             varchar(256) not null,
   primary key (user_id)
);

/*==============================================================*/
/* Index: User_name                                             */
/*==============================================================*/
create unique index User_name on User
(
   name
);

/*==============================================================*/
/* Table: comment                                               */
/*==============================================================*/
create table comment
(
   comment_id           int not null auto_increment,
   order_id             int not null,
   user_id              int not null,
   rating               int not null,
   content              varchar(512) not null,
   primary key (comment_id)
);

/*==============================================================*/
/* Table: dish                                                  */
/*==============================================================*/
create table dish
(
   dish_id              int not null auto_increment,
   stall_id             int not null,
   name                 varchar(16) not null,
   price                decimal(5,2) not null,
   image                varchar(256),
   primary key (dish_id)
);

alter table Canteen add constraint FK_Admin_Canteen foreign key (admin_id)
      references CanteenAdmin (admin_id) on delete restrict on update restrict;

alter table Order_Dish add constraint FK_Order_Dish foreign key (order_id)
      references Orders (order_id) on delete restrict on update restrict;

alter table Order_Dish add constraint FK_Order_Dish2 foreign key (dish_id)
      references dish (dish_id) on delete restrict on update restrict;

alter table Orders add constraint FK_Ordering foreign key (user_id)
      references User (user_id) on delete restrict on update restrict;

alter table Orders add constraint FK_Stall_Order foreign key (stall_id)
      references Stall (stall_id) on delete restrict on update restrict;

alter table Stall add constraint FK_Canteen_Stall foreign key (canteen_id)
      references Canteen (canteen_id) on delete restrict on update restrict;

alter table Stall add constraint FK_Trader_Stall foreign key (trader_id)
      references Trader (trader_id) on delete restrict on update restrict;

alter table comment add constraint FK_Order_Comment foreign key (order_id)
      references Orders (order_id) on delete restrict on update restrict;

alter table comment add constraint FK_commenting foreign key (user_id)
      references User (user_id) on delete restrict on update restrict;

alter table dish add constraint FK_Stall_Dish foreign key (stall_id)
      references Stall (stall_id) on delete restrict on update restrict;


create trigger Orders_BEFORE_INSERT before insert on Orders
	for each row set new.ordered_time = NOW();

