# MySQL-Day03笔记
## 存储引擎
* 定义
  处理表的处理器
  
* 基本操作  
  1、查看所有存储引擎
  ```
  mysql> show engines;
  ```
  2、查看已有表的存储引擎
  ```
  mysql> show create table 表名;
  ```
  3、创建表指定  
  ```
  create table 表名 (...) 
  engine=MyISAM,
  charset=utf8,
  auto_increment=10000;
  ```  
  4、已有表指定  
  ```
  alter table 表名 engine=InnoDB;
  ```
  
## 常用存储引擎及特点
* InnoDB  
  1、支持行级锁  
  2、支持外键、事务、事务回滚  
  3、表字段和索引同存储在一个文件中  
    * 1、表名.frm :表结构  
    * 2、表名.ibd : 表记录及索引文件  
    
* MyISAM  
  1、支持表级锁  
  2、表字段和索引分开存储  
  * 1、表名.frm :表结构  
  * 2、表名.MYI : 索引文件(my index)  
  * 3、表名.MYD : 表记录(my data) 
   
* MEMORY  
  1、表记录存储在内存中,效率高  
  2、服务或主机重启,表记录清除  
  
* 如何选择存储引擎  
  1、执行查操作多的表用 具体问题具体分析(实在不行用 InnoDB)  
  key_buffer 在内存中缓存索引，64M 内存，M:存索引，In:存索引+数据  
  
  2、执行写操作多的表用 InnoDB  
  
  3、临时表 : MEMORY  
  
## MySQL的用户账户管理

* 开启MySQL远程连接

  更改配置文件,重启服务!
  * 1、sudo su
  * 2、cd /etc/mysql/mysql.conf.d
  * 3、cp mysqld.cnf mysqld.cnf.bak
  * 4、vi mysqld.cnf #找到44行左右,加 # 注释
    bind-address = 127.0.0.1  
    [mysqld]  
    character_set_server = utf8
  * 5、保存退出
  * 6、service mysql restart
  
* 添加授权用户
  > 1、用root用户登录mysql  
    mysql -uroot -p123456
    
  > 2、授权  
    grant 权限列表 on 库.表 to "用户名"@"%"
    identified by "密码" with grant option;
    
  > 3、刷新权限  
    flush privileges;
      
  > 权限列表:  
    all privileges 、select 、insert ... ...
    库.表 : *.* 代表所有库的所有表

* 示例  
  1、添加授权用户work,密码123,对所有库的所有表有所有权限 
  ``` 
  mysql>grant all privileges on *.* to
  'work'@'%' identified by '123' with grant option;
  mysql>flush privileges;
  ```
  
## 事务和事务回滚

* 事务定义  
  一件事从开始发生到结束的过程
* 作用  
  确保数据的一致性、准确性、有效性
* 事务操作  
  > 1、开启事务  
    mysql>begin; # 方法1  
    mysql>start transaction; # 方法2
    
  > 2、开始执行事务中的1条或者n条SQL命令
  
  > 3、终止事务  
    mysql>commit; # 事务中SQL命令都执行成功,提交到数据库,结束!
    mysql>rollback; # 有SQL命令执行失败,回滚到初始状态,结束!
    
## 事务四大特性(ACID)

* 1、原子性(atomicity)  
> 一个事务必须视为一个不可分割的最小工作单元,整个事务中
的所有操作要么全部提交成功,要么全部失败回滚,对于一个
事务来说,不可能只执行其中的一部分操作

* 2、一致性(consistency)
> 数据库总是从一个一致性的状态转换到另一个一致性的状态

* 3、隔离性(isolation)
> 一个事务所做的修改在最终提交以前,对其他事务是不可见的

* 4、持久性(durability)
> 一旦事务提交,则其所做的修改就会永久保存到数据库中。此
时即使系统崩溃,修改的数据也不会丢失

* 注意
> 1、事务只针对于表记录操作(增删改)有效,对于库和表的操作无效

> 2、事务一旦提交结束,对数据库中数据的更改是永久性的

* 注：在系统日志中查看 mysql 启动日志
> cd /var/log  
  cat /var/log/syslog |grep 'MySQL'|more +
  
  
## E-R模型(Entry-Relationship)
* 定义  
  E-R模型即 实体-关系 数据模型,用于数据库设计  
  用简单的图(E-R图)反映了现实世界中存在的事物或数据以及

* 他们之间的关系：实体、属性、关系  
  > 实体
  >> 1、描述客观事物的概念(表)  
     2、表示方法 :矩形框  
     3、示例 :一个人、一本书、一杯咖啡、一个学生
   
  > 属性  
  >> 1、实体具有的某种特性(表里的字段)  
     2、表示方法 :椭圆形  
     3、示例  
       学生属性 :学号、姓名、年龄、性别、专业 ...  
       感受属性 :悲伤、喜悦、刺激、愤怒 ...
       
* ==关系(重要)==  

  > 1、实体之间的联系
  
  > 2、一对一关联(1:1) :老公对老婆  
    A中的一个实体,B中只能有一个实体与其发生关联  
    B中的一个实体,A中只能有一个实体与其发生关联
    
  > 3、一对多关联(1:n) :父亲对孩子  
    A中的一个实体,B中有多个实体与其发生关联  
    B中的一个实体,A中只能有一个与其发生关联
    
  > 4、多对多关联(m:n) :兄弟姐妹对兄弟姐妹、学生对课程  
    A中的一个实体,B中有多个实体与其发生关联  
    B中的一个实体,A中有多个实体与其发生关联  
    
## ER图的绘制
矩形框代表实体,菱形框代表关系,椭圆形代表属性
![img](/home/tarena/m1905/month03/MySQL_senior/day03/timg.jpeg)

## 关系映射实现(重要)
* 1:1 实现 -->   
  主外键关联,外键字段添加唯一索引
  ```
  表t1 : id int primary key,
  1
  表t2 : t2_id int unique,
  foreign key(t2_id) references t1(id)
  1
  ```
* 1:n 实现 -->   
  主外键关联
  ```
  表t1 : id int primary key,
  1
  表t2 : t2_id int,
  foreign key(t2_id) references t1(id)
  1
  1
  ```
* m:n 实现 (借助中间表):
  ```
  t1 : t1_id
  t2 : t2_id
  ```

## MySQL调优

* 存储引擎优化
1、读操作多:MyISAM
2、写操作多:InnoDB

* 索引优化
  
