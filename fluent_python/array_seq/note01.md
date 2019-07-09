## 内置序列类型
### 容器序列
* list、tuple 和 collections.deque 这些序列能存放不同类型的数据。
### 扁平序列
* str、bytes、bytearray、memoryview 和 array.array,这类序列只能容纳一种类型。

容器序列存放的是它们所包含的任意类型的对象的引用,而扁平序列里存放的是值而不是引用。
换句话说,扁平序列其实是一段连续的内存空间。
由此可见扁平序列其实更加紧凑,但是它里面只能存放诸如字符、字节和数值这种基础类型。

### 可变序列
* list、bytearray、array.array、collections.deque 和 memoryview。
### 不可变序列
* tuple、str 和 bytes。


### 元组不仅仅是不可变的列表
* 元组其实是对数据的记录:  
元组中的每个元素都存放了记录中一个字段的数据,外加这个字段的位置。正是这个位置信息给数据赋予了意义。

### 具名元组 collections.nametuple
* collections.nametuple 是一个工厂函数，它可以用来构建一个带字段名的元组和一个有名字的类。
* 代码实现 namedtuple.py