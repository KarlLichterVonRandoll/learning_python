"""
    空洞文件
"""

with open("hole.txt", "wb") as f:
    f.write(b"start----\n")
    f.seek(1024*1024, 2) # 预先设置存储空间
    f.write(b"end---")
