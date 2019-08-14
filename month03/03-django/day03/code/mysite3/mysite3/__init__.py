# file: mysite3/__init__.py

import pymysql

# 让 Django 用 pymysql 对 mysql 进行操作
pymysql.install_as_MySQLdb()
