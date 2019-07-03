"""
    seek.py
    1.每次open打开文件，文件偏移量在开头
    2.以 a 的方式打开，文件偏移量在末尾
    3.读写操作共用一个文件偏移量
"""

with open("buffer.txt", "rb+") as f:
    print("文件偏移量", f.tell())
    f.write(b"c")
    print("文件偏移量", f.tell())
    f.seek(-1, 2)
    print("文件偏移量", f.tell())
    print(f.read(1).decode())
    print("文件偏移量", f.tell())
