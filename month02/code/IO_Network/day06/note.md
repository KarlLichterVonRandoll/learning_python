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

***代码示例：day2/stick_send.py,stick_recv.py***
	  
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