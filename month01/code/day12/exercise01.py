commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}


class Commodity:
    def __init__(self, id=0, amount=0):
        self.id = id
        self.name = commodity_info[self.id]["name"]
        self.amount = amount
        self.price = commodity_info[self.id]["price"]

    @property
    def calculate(self):
        return self.price * self.amount


class BuyingController:

    __list_order = []

    @staticmethod
    def display_commodity():
        for key, value in commodity_info.items():
            print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))

    def choose(self):
        self.display_commodity()
        id = int(input("输入商品编号:"))
        if id in commodity_info:
            amount = int(input("输入购买数量"))
            commodity = Commodity(id, amount)
            BuyingController.__list_order.append(commodity)
            print("加入购物车成功")
        else:
            print("商品不存在")

    @staticmethod
    def get_list_order():
        return BuyingController.__list_order


class PayingController:

    def __init__(self):
        self.__list_order = BuyingController().get_list_order()

    def print_order(self):
        for item in self.__list_order:
            print("商品代号", item.id, "商品名称", item.name, "商品单价", item.price,
                  "商品总价", item.calculate)

    def calculate_total_money(self):
        total_money = 0
        for item in self.__list_order:
            total_money += item.calculate
        return total_money

    def paying(self):
        money = int(input("商品总价为%d,请输入金额:" % self.calculate_total_money()))
        if money >= self.calculate_total_money():
            change = money - self.calculate_total_money()
            print("支付成功,找回%d元" % change)
            self.__list_order.clear()
        else:
            print("金额不足")


class ShoppingView:
    def main(self):
        while True:
            item = input("1键购买,2键结算,3键退出")
            if item == "1":
                self.__buy()
            elif item == "2":
                self.__pay()
            elif item == "3":
                exit()
            else:
                print("输入有误")

    def __buy(self):
        buyer = BuyingController()
        buyer.choose()

    def __pay(self):
        settle = PayingController()
        settle.print_order()
        settle.paying()


shopping = ShoppingView()
shopping.main()
