from sstack import SStack

"""
    逆波兰式表达
    1 1 + 5 * 9 + 0 - 5 * 
"""

stack = SStack()
while True:
    str_input = input(":").split(" ")
    for i in str_input:
        try:
            number = float(i)
            stack.push(i)
        except Exception:
            x = stack.pop()
            y = stack.pop()
            z = str(eval(y + i + x))
            print(z)
            stack.push(z)
