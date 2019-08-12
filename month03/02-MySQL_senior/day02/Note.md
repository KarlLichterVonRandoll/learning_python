# MySQL高级-Day02笔记

## 外键（foreign key）

* 定义

  让当前表字段的值在另一个表的范围内选择

* 语法
  ```mysql
  foreign key(参考字段名)
  references 主表(被参考字段名)
  on delete 级联动作
  on update 级联动作
  ```

* 使用规则

  1.主表、从表字段数据类型要一致  
  2.主表被参考字段 ：KEY的一种，一般为主键
  ```sql
  mysql> create table slave (
    -> stu_id int,
    -> name varchar(20),
    -> money decimal(6,2),
    -> foreign key(stu_id) references master(id)
    -> on delete cascade
    -> on update cascade) charset=utf8;
  ```

* 示例

  表1. 缴费信息表(财务)

  ```mysql
  id   姓名     班级     缴费金额
  1   唐伯虎   AID1903     300
  2   点秋香   AID1903     300
  3   祝枝山   AID1903     300
  ```

  表2. 学生信息表(班主任) -- 做外键关联

  ```mysql
  stu_id   姓名   缴费金额
    1     唐伯虎    300
    2     点秋香    300
  ```
  
* **删除外键**

  ```mysql
  alter table 表名 drop foreign key 外键名;
  ​外键名 ：show create table 表名;
  ```

* **级联动作**

  ```mysql
  cascade
  ​数据级联删除、更新(参考字段)
  restrict(默认)
  ​从表有相关联记录,不允许主表操作
  set null
  ​主表删除、更新,从表相关联记录字段值为NULL
  ```

* **已有表添加外键**

  ```mysql
  alter table 表名 add foreign key(参考字段) 
  references 主表(被参考字段) 
  on delete 级联动作 
  on update 级联动作;
  ```
  
## 嵌套查询(子查询)

* 定义

  把内层的查询结果作为外层的查询条件

* 语法格式

  ```mysql
  select ... from 表名 where 条件(select ....);
  ```

* 示例

  ```mysql
  1、把攻击值小于平均攻击值的英雄名字和攻击值显示出来
  
  2、找出每个国家攻击力最高的英雄的名字和攻击值(子查询)
  ```
  
## 多表查询

* 笛卡尔积  
  ```
  select 字段名列表 from 表名列表; 
  ```
  
* 多表查询
  ```  
  select 字段名列表 from 表名列表 where 条件;
  ```
  eg ： 显示 省 市 县 详细信息
  ```
  select province.pname,city.cname,county.coname
  from province, city, county
  where city.cp_id = province.pid 
  and county.copid = city.cid;
  ```
  
## 连接查询

* 内连接（结果同多表查询，显示匹配到的记录）
  ```
  select 字段名 from  表1 inner join 表2 on 条件 inner join 表3 on 条件;
  ```
  eg1 : 显示省市详细信息
  ```
  select province.pname,city.cname from province 
  inner join city 
  on province.pid = city.cp_id;
  ```
  eg2 : 显示 省 市 县 详细信息
  ```
  select province.pname,city.cname,county.coname from province 
  inner join city 
  on province.pid = city.cp_id 
  inner join county 
  on county.copid = city.cid;
  ```
  
* 左外连接  
  以 左表 为主显示查询结果
  ```
  select 字段名 from 表1 
  left join 表2 
  on 条件 
  left join 表3 
  on 条件;
  ```
  eg1 : 显示 省 市 详细信息（要求省全部显示）
  ```
  select province.pname,city.cname from province 
  left join city 
  on province.pid = city.cp_id;
  ```
 
* 右外连接  
  用法同左连接,以 右表 为主显示查询结果
  ```
  select 字段名 from 表1 
  right join 表2 
  on 条件 
  right join 表3 
  on 条件;
  ```

## 数据导入
==掌握大体步骤==

==source 文件名.sql==

* 作用

  把文件系统的内容导入到数据库中
  语法（方式一）
  ```
  load data infile "文件名"
  into table 表名
  fields terminated by "分隔符"
  lines terminated by "\n"
  ```
* 示例  
  scoretable.csv 文件导入到数据库 db2 的表

  1、将scoretable.csv放到数据库搜索路径中
  ```
   mysql>show variables like 'secure_file_priv';
         /var/lib/mysql-files/
   Linux: sudo cp /home/tarena/scoreTable.csv /var/lib/mysql-files/
  ```
  * 2、在数据库中创建对应的表
  ```
  create table scoretab(
  rank int,
  name varchar(20),
  score float(5,2),
  phone char(11),
  class char(7)
  )charset=utf8;
  ```
  * 3、执行数据导入语句
  ```
  load data infile '/var/lib/mysql-files/scoreTable.csv'
  into table scoretab
  fields terminated by ','
  lines terminated by '\n'
  ```
  * 4、练习
  添加id字段,要求主键自增长,显示宽度为3,位数不够用0填充
  ``````
  alter table scoretab add id int(3) zerofill primary key auto_increment first;
  * 语法（方式二）

  source 文件名.sql
  
## 数据导出

* 作用

  将数据库中表的记录保存到系统文件里

* 语法格式
  ```
  select ... from 表名
  into outfile "/var/lib/mysql-files/文件名"
  fields terminated by "分隔符"
  lines terminated by "分隔符";
  ```
* 练习

  1、把sanguo表中英雄的姓名、攻击值和国家三个字段导出来,放到 sanguo.csv中
 
  2、将mysql库下的user表中的 user、host两个字段的值导出到 user2.txt，将其存放在数据库目录下
 
* 注意

  1、导出的内容由SQL查询语句决定  
  
  2、执行导出命令时路径必须指定在对应的数据库目录下
  
## 表的复制
1、表能根据实际需求复制数据

2、复制表时不会把KEY属性复制过来

* 语法
  ```
  create table 表名 select 查询命令;
  ```
  
* 练习
  
  1、复制sanguo表的全部记录和字段,sanguo2
  ```
  create table sanguo2 select * from sanguo;
  ```
  2、复制sanguo表的 id,name,country 三个字段的前3条记录,sanguo4
  ```
  create table sanguo4 select id,name,country from sanguo limit 3;
  ```
  
* 注意

  复制表的时候不会把原有表的 KEY 属性复制过来

* 复制表结构  
  create table 表名 select 查询命令 where false;
  
## 锁（自动加锁和释放锁）

全程重点，理论和锁分类及特点

* 目的

  解决客户端并发访问的冲突问题

* 锁类型分类

  读锁(共享锁)：select 加读锁之后别人不能更改表记录,但可以进行查询  
  
  写锁(互斥锁、排他锁)：加写锁之后别人不能查、不能改  
  
* 锁粒度分类

  表级锁 ：myisam
  
  行级锁 ：innodb