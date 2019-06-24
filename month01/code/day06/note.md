# day06
### 列表推导式
* 使用简易方法,将可迭代对象转换为列表。
* 语法：  
变量 = [表达式 for 变量 in 可迭代对象]  
变量 = [表达式 for 变量 in 可迭代对象 if 条件]
```
# 将列表 list01 中每个元素 +1 后存入 list02
list01 = [4,55,66,7,3,6,5]
list02 = []
# for item in list01:
#     list02.append(item+1)
# 等同于
# list02 = [item + 1 for item in list01]

# 将list01 中大于 10 的元素 +1 后存入 list02
list02 = [item + 1 for item in list01 if item > 10] 
```

### 列表扩容
* 1.列表都会预留空间  
  2.当预留空间不足时，会创建新列表(更大的空间)  
  3.将原有的数据拷贝到新列表中  
  4.替换引用

## 元组 tuple
* 1.由一系列变量组成的不可变序列容器。  
  2.不可变是指一但创建，不可以再添加/删除/修改元素。
  
* 创建元组
```
tuple01 = ()  # 空
tuple01 = tuple([1,2,3])  # 列表 -> 元组
list01 = list(tuple01)  # 元组 -> 列表
tuple01 = (1,2,3)  # 具有默认值
```
* 如果元组只有一个元素,在构建时需要加逗号
```
tuple02 = (100)  # type(tuple02) == "int"
tuple02 = (100,)  # type(tuple02) == "tuple"
```
* 获取元素（索引、切片）
```
tuple03 = (1, 2, 3)
a = tuple03[1]  # str
b = tuple03[-2:]  # tuple
# 可以直接将元组赋值给多个变量
a, b, c = tuple03
print(a,b,c)  # 1 2 3
```
* 遍历元素
```
# 正向
for item in tuple03:
    print(item)
# 反向
for i in range(len(tuple03)-1,-1,-1):
    print(tuple03[i])

```

## 字典
* 1.由一系列键值对组成的可变映射容器  
  2.映射：一对一的对应关系，且每条记录无序 
  3.键必须惟一且不可变(字符串/数字/元组)，值没有限制
* 字典中键的位置根据哈希算法确定。
* 所有容器中字典的查找是最快的，但缺点是占用空间(内存)大，利用空间换取时间(CPU)。
#### 1.创建字典
```
# 空字典
dict01 = {}
dict01 = dict()
# 默认值
dict01 = {”zwj“:100, ”zm“:80, ”zzr“:90}
dict01 = dict([('a',1),('b',2)]) # {'a': 1, 'b': 2}
```
#### 2.查找元素(根据key查找value)
```
print(dict01["a"])
# 如果key不存在，查找时会报错
```
#### 3.修改元素(key存在)
```
dict01["a"] = 3
```
#### 4.添加元素(key不存在)
```
dict01["c"] = 9
```
#### 5.删除元素
```
del dict01["a"]
```
#### 6.遍历
```
for key in dict01:   # 拿到所有的键
    print(key)
for value in dict01.values():  # 拿到所有值
    print(value)
for k,v in dict01.items():  # 拿到所有的键和值
    print(k,v)
```

  