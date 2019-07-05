## struct模块的使用

代码实现：struct_server.py   
代码实现：struct_client.py

1. 原理： 将一组简单数据进行打包，转换为bytes格式发送。或者将一组bytes格式数据，进行解析。

2. 接口使用

```
Struct(fmt)
功能: 生成结构化对象
参数：fmt  定制的数据结构

st.pack(v1,v2,v3....)
功能: 将一组数据按照指定格式打包转换为bytes
参数：要打包的数据
返回值： bytes字节串

st.unpack(bytes_data)
功能： 将bytes字节串按照指定的格式解析
参数： 要解析的字节串
返回值： 解析后的内容

struct.pack(fmt,v1,v2,v3...)
struct.unpack(fmt,bytes_data)

说明： 可以使用struct模块直接调用pack unpack。此时这两函数第一个参数传入fmt。其他用法功能相同
```


