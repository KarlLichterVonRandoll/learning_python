commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}


# 选择商品
def choose_commodity():
    display_commodity()
    create_order()
    print("添加到购物车。")


# 生成订单
def create_order():
    while True:
        cid = int(input("请输入商品编号："))
        if cid in commodity_info:
            break
        else:
            print("该商品不存在")
    count = int(input("请输入购买数量："))
    shopping_cart.append({"cid": cid, "count": count})


# 打印商品信息
def display_commodity():
    for key, value in commodity_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))


# 结算
def payment_commodity():
    amount_of_money = 0
    amount_of_money = generate_bill(amount_of_money)
    pay_bill(amount_of_money)


# 支付账单
def pay_bill(amount_of_money):
    while True:
        money_input = float(input("总价%d元，请输入金额：" % amount_of_money))
        if money_input >= amount_of_money:
            print("购买成功，找回：%d元。" % (money_input - amount_of_money))
            shopping_cart.clear()
            break
        else:
            print("金额不足.")


# 生成账单,计算总价
def generate_bill(amount_of_money):
    for item in shopping_cart:
        commodity = commodity_info[item["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (commodity["name"], commodity["price"], item["count"]))
        amount_of_money += commodity["price"] * item["count"]
    return amount_of_money


# 购物
def shopping():
    while True:
        item = input("1键购买，2键结算，3键退出。")
        if item == "1":
            choose_commodity()
        elif item == "2":
            payment_commodity()
        elif item == "3":
            print("谢谢惠顾")
            break


if __name__ == "__main__":
    shopping_cart = []
    shopping()
