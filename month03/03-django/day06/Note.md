# session 会话控制

### 什么是session
session又名会话控制，是在服务器上开辟一段空间用于保留浏览器和服务器交互时的重要数据。
  
##### session的起源  
* http 协议是无状态的：每次请求都是一次新的请求，不会记得之前通信的状态
* 实现状态保持的方式：在客户端或服务器端存储与会话有关的数据
* 推荐使用 session 方式，所有数据存储在服务器端

##### 实现方式
* 使用 session 需要在浏览器客户端启动 cookie，且用在 cookie 中存储 sessionid
* 每个客户端都可以在服务器端有一个独立的 Session
* 注意：不同的请求者之间不会共享这个数据，与请求者一一对应

##### Django启用Session
在 settings.py 文件中
向 INSTALLED_APPS 列表中添加：
```python
INSTALLED_APPS = [
# 启用 sessions 应用
    'django.contrib.sessions',
]
```
向 MIDDLEWARE_CLASSES 列表中添加：
```python
MIDDLEWARE = [
# 启用 Session 中间件
    'django.contrib.sessions.middleware.SessionMiddleware',
]
```

### session的基本操作
session 对象是一个类似于字典的 SessionStore 类型的对象，可以用类似于字典的方式进行操作  
session 只能够存储能够序列化的数据,如字典，列表等。

**1. 保存 session 的值到服务器**
`request.session['KEY'] = VALUE`

**2. 获取session的值**
`VALUE = request.session['KEY']`
`VALUE = request.session.get('KEY', 缺省值)`

**3. 删除session的值**
`del request.session['KEY']`

**4. 在 settings.py 中有关 session 的设置**
1.SESSION_COOKIE_AGE
作用: 指定 sessionid 在cookies中的保存时长(默认是2周)，如下:
`SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2`

2.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
设置只要浏览器关闭时,session就失效(默认为False)

**5. session 缺省配置**
  模块 `import django.conf.global_settings`

注: 当使用 session 时需要迁移数据库,否则会出现错误
```shell
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```