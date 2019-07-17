## 1. 实验简介

#### 1.实验知识点
* python 基础知识
* 状态机的概念

#### 2.实验环境
* python 3.6


## 2. 实验内容
* 用 python 实现 2048 游戏
* 需要导入的模块
```
import random
import os
```

### 2.1 主逻辑
#### 1.用户行为:  
所有的有效输入都可以转换为"上，下，左，右，游戏重置，退出"这六种行为，用 actions 表示
```
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
```
有效输入键是最常见的 W（上），A（左），S（下），D（右），R（重置），Q（退出），  
这里要考虑到大写键开启的情况，获得有效键值列表：
```
letter_codes = [ord(ch) for ch in "WASDRQwasdqr"]
```
将输入与行为进行关联
```
actions_dict = dict(zip(letter_codes, actions * 2))
```

#### 2.状态机
* 将 2048 游戏分解为几种状态的转换:  
  包括 Init, Win, Game, Gameover, Exit.

* state 存储当前状态， state_actions 这个词典变量作为状态转换的规则，它的 key 是状态，value 是返回下一个状态的函数：
```
Init: init()
    Game
Game: game()
    Game
    Win
    GameOver
    Exit
Win: lambda: not_game('Win')
    Init
    Exit
Gameover: lambda: not_game('Gameover')
    Init
    Exit
Exit: 退出循环
状态机会不断循环，直到达到 Exit 终结状态结束程序。
```

### 2.2 用户输入处理

### 2.3 矩阵转置和矩阵逆转
* 使用这两个操作会大大减少代码量

### 2.4 创建棋盘
* 初始化棋盘的参数，可以指定棋盘的高和宽以及游戏胜利条件，默认是最经典的 4x4～2048。

### 2.5 棋盘操作

### 

