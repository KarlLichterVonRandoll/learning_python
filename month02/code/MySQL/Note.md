## 数据库概述

### 数据存储阶段 

(1) 人工管理阶段

缺点 ： 数据无法共享,不能单独保持,数据存储量有限

(2) 文件管理阶段 （.txt  .doc  .xls）
    
优点 ： 数据可以长期保存,可以存储大量的数据,使用简单

缺点 ： 数据一致性差,数据查找修改不方便,数据冗余度可能比较大

(3) 数据库管理阶段

优点 ： 数据组织结构化降低了冗余度,提高了增删改查的效率,容易扩展,方便程序调用，做自动化处理

缺点 ： 需要使用sql 或者 其他特定的语句，相对比较复杂

### 数据库应用

>融机构、游戏网站、购物网站、论坛网站 ... ... 

### 基础概念

>数据 ： 能够输入到计算机中并被识别处理的信息集合

>数据结构 ： 研究一个数据集合中数据之间关系的

>数据库 ： 按照数据结构，存储管理数据的仓库。数据库是在数据库管理系统管理和控制下，在一定介质上的数据集合。

>数据库管理系统 ： 管理数据库的软件，用于建立和维护数据库

>数据库系统 ： 由数据库和数据库管理系统，开发工具等组成的集合 


### 数据库分类和常见数据库

* 关系型数据库和非关系型数据库
      
>关系型 ： 采用关系模型（二维表）来组织数据结构的数据库 

>非关系型 ： 不采用关系模型组织数据结构的数据库

* 开源数据库和非开源数据库

> 开源 ： MySQL、SQLite、MongoDB

> 非开源 ： Oracle、DB2、SQL_Server

* 常见的关系型数据库
  
> MySQL、Oracle、SQL_Server、DB2 SQLite  


### 认识关系型数据库和MySQL

1.数据库结构 （图库结构）

>数据元素 --> 记录 -->数据表 --> 数据库

2.数据库概念解析

>数据表 ： 存放数据的表格 

>字段 ： 每个列，用来表示该列数据的含义

>记录 ： 每个行，表示一组完整的数据

3.MySQL特点

* 是开源数据库，使用C和C++编写 
* 能够工作在众多不同的平台上
* 提供了用于C、C++、Python、Java、Perl、PHP、Ruby众多语言的API
* 存储结构优良，运行速度快
* 功能全面丰富

4.MySQL安装

>Ubuntu安装MySQL服务
>>安装服务端: sudo apt-get install mysql-server
>>安装客户端: sudo apt-get install mysql-client
>>> 配置文件：/etc/mysql
>>> 命令集： /usr/bin
>>> 数据库存储目录 ：/var/lib/mysql

>Windows安装MySQL
>>下载MySQL安装包(windows)  https://dev.mysql.com/downloads/mysql/
  mysql-installer***5.7.***.msi
>>安装教程去安装

5.启动和连接MySQL服务

>服务端启动
>>查看MySQL状态: sudo /etc/init.d/mysql status
>>启动服务：sudo /etc/init.d/mysql start | stop | restart

>客户端连接
>>命令格式 
>>>mysql -h主机地址 -u用户名 -p密码
>>>mysql -hlocalhost -uroot -p123456
>>>本地连接可省略 -h 选项: mysql -uroot -p123456

>关闭连接
>> ctrl-D
>> exit