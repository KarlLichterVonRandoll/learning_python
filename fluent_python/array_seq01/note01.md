## 内置序列类型

### 容器序列
* list、tuple 和 collections.deque 这些序列能存放不同类型的数据。

### 扁平序列
* str、bytes、bytearray、memoryview 和 array.array,这类序列只能容纳一种类型。

> 容器序列存放的是它们所包含的任意类型的对象的引用,而扁平序列里存放的是值而不是引用。
  换句话说,扁平序列其实是一段连续的内存空间。
  由此可见扁平序列其实更加紧凑,但是它里面只能存放诸如字符、字节和数值这种基础类型。

### 可变序列
* list, bytearray, array.array, collections.deque 和 memoryview。

### 不可变序列
* tuple, str 和 bytes。

## 元组
### 元组不仅仅是不可变的列表
* 元组其实是对数据的记录: 元组中的每个元素都存放了记录中一个字段的数据,外加这个字段的位置。
  正是这个位置信息给数据赋予了意义。

### 具名元组 collections.nametuple
* collections.nametuple 是一个工厂函数，它可以用来构建一个带字段名的元组和一个有名字的类。
* 代码实现 namedtuple.py
```
1. 创建具名元组需要两个参数，一个是类名，另一个是类的各个字段的名字。
   后者可以是由数个字符串组成的可迭代对象,或者是由空格分隔开的字段名组成的字符串。
   
2. 存放在对应字段里的数据要以一串参数的形式传入到构造函数中
   (注意,元组的构造函数却只接受单一的可迭代对象)。
   
3. 可以通过字段名或者位置来获取一个字段的信息。
```
* 具名元组的一些专有属性  
  如：_fields 类属性、类方法_make(iterable) 和实例方法 _asdict()。
  代码实现 namedtuple.py
```
_fields 属性是一个包含这个类所有字段名称的元组。

用 _make() 通过接受一个可迭代对象来生成这个类的一个实例,
它的作用跟 City(*delhi_data) 是一样的。

_asdict() 把具名元组以 collections.OrderedDict 的形式返
回,我们可以利用它来把元组里的信息友好地呈现出来。
```

### 作为不可变列表的元组
* 除了跟增减元素相关的方法之外,元组支持列表的其他所有方法。
还有一个例外,元组没有 __reversed__ 方法,但是这个方法只是个优化而已,
reversed(my_tuple)这个用法在没有 __reversed__ 的情况下也是合法的。

## 切片
> 在 Python 里,像列表(list)、元组(tuple)和字符串(str)这类序列类型都支持切片操作

### 对对象进行切片
* 我们可以用 s[a:b:c] 的形式对 s 在 a 和 b 之间以 c 为间隔取值，
  c 的值还可以为负,负值意味着反向取值。 
* a:b:c 这种用法只能作为索引或者下标用在 [] 中来返回一个切片对象:  
  slice(a, b, c)。  
  对 seq[start:stop:step] 进行求值的时候,Python 会调用 seq.__getitem__(slice(start, stop, step))。

### 给切片进行赋值
```
>> l = list(range(10))
>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>> l[2:5] = [20, 30]
>> l
[0, 1, 20, 30, 5, 6, 7, 8, 9]
>> l[2:5] = 100
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: can only assign an iterable
>> l[2:5] = [100]
[0, 1, 100, 6, 7, 8, 9]
```