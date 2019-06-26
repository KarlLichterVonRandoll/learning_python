def verify_permission(func):
    def wrapper(*args, **kwargs):
        print("验证权限")
        func(*args, **kwargs)

    return wrapper


@verify_permission
def enter_background(login_id, pwd):
    if login_id == "wang" and pwd == 123456:
        print("进入后台")
    else:
        print("登录失败")


@verify_permission
def delete_order(id):
    print("删除订单%d" % id)


enter_background("wang",123456)
delete_order(101)


