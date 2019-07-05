#### 客户端流程

* 代码实现：tcp_client.py
		  
1.创建套接字  
* 注意:只有相同类型的套接字才能进行通信
			
2.请求连接

```
sockfd.connect(server_addr)
功能：连接服务器
参数：元组  服务器地址
```

3.收发消息
* 注意： 防止两端都阻塞，recv send要配合

4.关闭套接字

#### tcp 套接字数据传输特点

* tcp连接中当一端退出，另一端如果阻塞在recv，此时recv会立即返回一个空字串。

* tcp连接中如果一端已经不存在，仍然试图通过send发送则会产生BrokenPipeError

* 一个监听套接字可以同时连接多个客户端，也能够重复被连接

#### 网络收发缓冲区

1. 网络缓冲区有效的协调了消息的收发速度
2. send和recv实际是向缓冲区发送接收消息，当缓冲区不为空recv就不会阻塞。
	
#### tcp粘包

	  
>原因：tcp以字节流方式传输，没有消息边界。多次发送的消息被一次接收，此时就会形成粘包。

>影响：如果每次发送内容是一个独立的含义，需要接收端独立解析此时粘包会有影响。

>处理方法
>>1. 人为的添加消息边界
>>2. 控制发送速度

### UDP套接字编程

#### 服务端流程


代码实现：udpserver.py
	  
1. 创建数据报套接字
```
sockfd = socket(AF_INET,SOCK_DGRAM)
```
2. 绑定地址

```
sockfd.bind(addr)
```

3. 消息收发

```	    
data,addr = sockfd.recvfrom(buffersize)
功能： 接收UDP消息
参数： 每次最多接收多少字节
返回值： data  接收到的内容
	addr  消息发送方地址

n = sockfd.sendto(data,addr)
功能： 发送UDP消息
参数： data  发送的内容 bytes格式
	addr  目标地址
返回值：发送的字节数
```

4. 关闭套接字
```
sockfd.close()
```

#### 客户端流程

代码实现：udpclient.py

1.创建套接字  
2.收发消息  
3.关闭套接字  

---------------
### 总结 ：tcp套接字和udp套接字编程区别
> 1. 流式套接字是以字节流方式传输数据，数据报套接字以数据报形式传输
> 2. tcp套接字会有粘包，udp套接字有消息边界不会粘包
> 3. tcp套接字保证消息的完整性，udp套接字则不能
> 4. tcp套接字依赖listen accept建立连接才能收发消息，udp套接字则不需要
> 5. tcp套接字使用send，recv收发消息，udp套接字使用sendto，recvfrom
---------------------

## socket套接字属性
```
1. sockfd.type  套接字类型

2. sockfd.family 套接字地址类型

3. sockfd.getsockname() 获取套接字绑定地址

4. sockfd.fileno() 获取套接字的文件描述符

5. sockfd.getpeername() 获取连接套接字客户端地址

6. sockfd.setsockopt(level,option,value)
    功能：设置套接字选项
    参数： level  选项类别   SOL_SOCKET
          option 具体选项内容
          value  选项值

7. sockfd.getsockopt(level,option) 
		功能 ： 获取套接字选项值
```

### UDP套接字广播
代码实现：day3/broadcast_recv.py
代码实现：day3/broadcast_recv.py

* 广播定义 ： 一端发送多点接收
    
* 广播地址 ： 每个网络的最大地址为发送广播的地址，向该地址发送，则网段内所有主机都能接收。

### TCP套接字之HTTP传输

#### HTTP协议 （超文本传输协议）

1.用途: 网页获取，数据的传输

2.特点  
 * 应用层协议，传输层使用tcp传输
 * 简单，灵活，很多语言都有HTTP专门接口
 * 无状态，协议不记录传输内容
 * http1.1 支持持久连接，丰富了请求类型

3.网页请求过程
```
1.客户端（浏览器）通过tcp传输，发送http请求给服务端
2.服务端接收到http请求后进行解析
3.服务端处理请求内容，组织响应内容
4.服务端将响应内容以http响应格式发送给浏览器
5.浏览器接收到响应内容，解析展示
```

#### HTTP请求（request）

代码实现：day3/http_test.py  
代码实现：day3/http_server.py

* 请求行 ： 具体的请求类别和请求内容

```
GET         /        HTTP/1.1
请求类别   请求内容     协议版本


请求类别：每个请求类别表示要做不同的事情 
	
GET : 获取网络资源
POST ：提交一定的信息，得到反馈
HEAD ： 只获取网络资源的响应头
PUT ： 更新服务器资源
DELETE ： 删除服务器资源
CONNECT
TRACE ： 测试
OPTIONS ： 获取服务器性能信息
```

* 请求头：对请求的进一步解释和描述, 以 key:value 形式
```
Accept-Encoding: gzip
```
* 空行
* 请求体: 请求参数或者提交内容

#### http响应（response）

1. 响应格式：响应行，响应头，空行，响应体

* 响应行 ： 反馈基本的响应情况

```	    
HTTP/1.1     200       OK
版本信息    响应码   附加信息
```

响应码 ： 
```
1xx  提示信息，表示请求被接收
2xx  响应成功
3xx  响应需要进一步操作，重定向
4xx  客户端错误
5xx  服务器错误
```
* 响应头：对响应内容的描述
```		    
Content-Type: text/html
```

* 响应体：响应的主体内容信息