// 针对 login 页面定义一个对象
var log={
    dt: "2019-8-5",
    enddt: "2019-9-5",
    updatedt: "2019-8-5",
    author: "ddkj"
}
// 有对象派生业务逻辑
log.submit={
    check: function(v){
        var _v = (v=="")?true:false;
        return _v;
    },
    autohide: function(obj){
        setTimeout(function(){
            obj.hide();
        }, 2000)
    }
}
// 获取元素对象并保存在变量中
var $form = $("form");

var $btn = $(".btn>input");

// 定义一个验证内容是否为空的函数
function checkvalue(){
    var $username = $("#username");
    var $password = $("#password");
    var $err1 = $("#err1");
    var $err2 = $("#err2");
    // 当用户名和密码都不为空时
    if ($username.val()!=""&&$password.val()!=""){
        // 直接提交
        console.log("err");
        return true;
    }else{
        // 如果用户名为空
        if ($username.val()==""){
            // 提示用户名错误显示
            $err1.show();
            // 两秒后自动隐藏
            log.submit.autohide($err1);
            // 阻止提交
            return false;
        }else{
            // 提示密码错误显示
            $err2.show();
            // 两秒后自动隐藏
            log.submit.autohide($err2);
            // 组织提交
            return false;
        }

    }
}
// 绑定按钮的单机事件
