"""
    buffer.py
    * 缓冲刷新条件
      1.缓冲区满了
      2.行缓冲时自动刷新
      3.程序运行结束或文件关闭，自动刷新
      4.调用flush函数
"""

f = open("buffer.txt", "w", 1)  # 1 表示行缓冲

while True:
    data = input(":")
    if not data:
        break
    f.write(data + "\n")  # 每次输入加 \n 都会自动缓冲
    # f.flush()

f.close()
