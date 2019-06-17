a = input('输入第一个变量：')
b = input('输入第二个变量：')
print(id(a))
print(id(b))
temp = a
a = b
b = temp
print('第一个变量为 ' + a)
print('第二个变量为 ' + b)
print(id(a))
print(id(b))
