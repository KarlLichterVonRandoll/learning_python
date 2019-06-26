def give_money(money):
    print("支付宝到账 %d 元" % money)

    def child_buy(target, price):
        nonlocal money
        if money >= price:
            money -= price
            print("孩子花了%d元，购买了%s，还剩%d元" % (price, target, money))
        else:
            print("钱不够")

    return child_buy


result = give_money(100000000)
result('手机', 8000)
result('跑车', 500000)
result('别墅', 2000000)

