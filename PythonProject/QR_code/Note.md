## 实验介绍
### 实验内容
* 通过调用 MyQR 接口来实现个人所需二维码，并可以设置二维码大小，是否在现有
  图片基础上生成，是否生成动态二维码。

### 实验环境
* Python 3.6.7
* MyQR

## 实验步骤

### 1.生成普通二维码
```
from MyQR import myqr
myqr.run("https://www.baidu.com")
```
会默认生成二维码图片 qrcode.png, 扫描二维码进入百度主页

#### myqr.run() 函数里的参数
```
run(words, version=1, level='H', picture=None, colorized=False, 
    contrast=1.0, brightness=1.0, save_name=None, save_dir=os.getcwd()):

参数            含义               详细
words       二维码指向链接  str,输入链接或句子作为参数
version     边长          int,控制边长,范围1-40,默认边长取决于输入信息长度和默认纠错等级
level       纠错等级       str,控制纠错水平，范围是L、M、Q、H，从左到右依次升高，默认为'H'
picture     结合图片       str，将QR二维码图像与一张同目录下的图片相结合，产生一张黑白图片
colorized   颜色          bool，使产生的图片由黑白变为彩色的
contrast    对比度        float，调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0
brightness  亮度          float，调节图片的亮度，其余用法和取值与 contrast 相同
save_name   输出文件名     str，默认输出文件名是"qrcode.png"
save_dir    存储位置       str，默认存储位置是当前目录
```


  