## 1.实验介绍
* 用 50 行 Python 代码完成图片转字符画小工具。学习 Linux 命令行操作，Python 基础，pillow 库的使用，argparse 库的使用。

## 2.实验原理
* 字符画是一系列字符的组合，我们可以把字符看作是比较大块的像素，一个字符能表现一种颜色（为了简化可以这么理解），字符的种类越多，可以表现的颜色也越多，图片也会更有层次感。
问题来了，我们是要转换一张彩色的图片，这么多的颜色，要怎么对应到单色的字符画上去？这里就要介绍灰度值的概念了。

> 灰度值：指黑白图像中点的颜色深度，范围一般从0到255，白色为255，黑色为0，故黑白图片也称灰度图像。

* 另外一个概念是 RGB 色彩：

> RGB色彩模式是工业界的一种颜色标准，是通过对红(R)、绿(G)、蓝(B)三个颜色通道的变化以及它们相互之间的叠加来得到各式各样的颜色的，
  RGB即是代表红、绿、蓝三个通道的颜色，这个标准几乎包括了人类视力所能感知的所有颜色，是目前运用最广的颜色系统之一。

* 我们可以使用灰度值公式将像素的 RGB 值映射到灰度值（这个公式并不是一个真实的算法，而是简化的 sRGB IEC61966-2.1 公式，真实的公式更复杂一些，不过在我们的这个应用场景下并没有必要）
```
gray ＝ 0.2126 * r + 0.7152 * g + 0.0722 * b
```
  我们可以创建一个不重复的字符列表，灰度值小（暗）的用列表开头的符号，灰度值大（亮）的用列表末尾的符号。
  
## 3. 实验步骤

### 1.导入必要的模块
```
from PIL import Image
import argparse
```

### 2.argparse 模块使用
* argparse 是一个命令行解析参数，它要运行在命令行下。

* 代码实现 test01.py

1.构建命令行输入参数处理对象
```
parser = argparse.ArgumentParser()
```

2.添加描述信息，当输入 python3 test01.py --help  就会出现
```
parser.description = "叫我出来干哈"
```

3.添加位置参数
```
parser.add_argument('partA', help="这是参数A")
parser.add_argument('partB', help="这是参数B")

# 使用
python3 test01.py 5 6
```

4.可选参数
```
parser.add_argument('--partC', help="这是参数C")
parser.add_argument('--partD', help="这是参数D")
# 使用
python3 test01.py --partC 7 --partD 8
```
5.为参数指定值
```
parser.add_argument('--verbose', help="increase output verbosity", action="store_true")
```
指定一个新关键字 action，指定值为"store_true"，这意味着，指定后使用 if args.verbose，就会返回真。没有指明它意味着False。
当你指定其他值时，它就会报错。

6.短选项
```
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
                    
>> python3 test01.py -v
verbosity turned on
>> python3 test01.py --help
usage: test01.py [-h] [-v]

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  increase output verbosity          
```

7.增加参数限制
```
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
                    help="increase output verbosity")
```
通过增加 choices 关键字指定参数 verbosity 的值只能为 0,1,2


8.解析并获取参数
```
args = parser.parse_args()
```

9.使用参数
```
print(args.echo)
```

10.在命令行不确定是否输入某个参数时, 采用以下形式输入
```
python3 test01.py --echo 5
```

### 3.实现 RGB 值转字符的函数
首先将 RGB 值转为灰度值，然后使用灰度值映射到字符列表中的某个字符。


### 4.处理图片
1.首先使用 PIL 的 Image.open 打开图片文件，获得对象 im  

2.使用 PIL 库的 im.resize() 调整图片大小对应到输出的字符画的宽度和高度，注意这个函数第二个参数使用 Image.NEAREST，表示输出低质量的图片。

3.遍历提取图片中每行的像素的 RGB 值，调用 getchar 转成对应的字符

4.将所有的像素对应的字符拼接在一起成为一个字符串 txt

5.打印输出字符串 txt

6.如果执行时配置了输出文件，将打开文件将 txt 输出到文件，如果没有，则默认输出到 output.txt 文件


