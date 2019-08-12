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

// 定义一个基于列表页的业务逻辑
var lst={
    template: function(t,u,p1,p2){
        var _html = "";
        _html += '<div class="item">';
        _html += '<div class="title">';
        _html += '<h3>'+t+'</h3>';
        _html += '</div>';
        _html += '<div class="con">';
        _html += '<div class="cleft">';
        _html += '<img src="'+u+'" alt="">';
        _html += '</div>';
        _html += '<div class="cright">';
        _html += '<p class="ptop">'+p1+'</p>';
        _html += '<p class="pbottom">'+p2+'</p>';
        _html += '</div>';
        _html += '</div></div>';
        return _html;
    }
}
// 使用数组保存数据
var arrData = [
    {
        t: "Python语言优势",
        u: "imgs/d.jpg",
        p1: "本文探讨了Python语言在AI领域的优势和运用。谁会成为AI 和大数据时代的第一开发语言？",
        p2: "皮皮下 学无止境 2019-8-23 3457已阅读 99",
    },
    {
        t: "Java语言优势",
        u: "imgs/c.jpg",
        p1: "本文探讨了JAVA语言在AI领域的优势和运用。谁会成为AI 和大数据时代的第一开发语言？",
        p2: "皮皮下 学无止境 2019-8-23 3457已阅读 99",
    },
    {
        t: "C++语言优势",
        u: "imgs/e.jpg",
        p1: "本文探讨了C++语言在AI领域的优势和运用。谁会成为AI 和大数据时代的第一开发语言？",
        p2: "皮皮下 学无止境 2019-8-23 3457已阅读 99",
    }
]
// 使用流程
// 1.遍历数组，获取每一项元素对象
// 2.将获取的元素对象填充到模板中
// 3.向页面元素追加模板
for (var i=0;i<arrData.length;i++){
    var _HTML = lst.template(arrData[i].t,
                             arrData[i].u,
                             arrData[i].p1,
                             arrData[i].p2);
    $(".lst").prepend(_HTML);
}

// 定义一个基于图片页的业务逻辑对象
var pics={
    template: function(u,n,t){
        _html = "";
        _html += '<div class="item">';
        _html += '<div class="imgs">';
        _html += '<img src="'+u+'" alt="">';
        _html += '<div class="tip">喜欢 | '+n+'</div>';
        _html += '</div>';
        _html += '<div class="title">';
        _html += '<h3>'+t+'</h3>';
        _html += '</div>';
        _html += '</div>';
        return _html;
    }
}
// 使用数组保存数据
var arrPics = [
    {
        t: "Python基础学习总结(一)",
        u: "imgs/toppic02.jpg",
        n: "199",
    },
    {
        t: "Sublime text3不能正常使用",
        u: "imgs/toppic01.jpg",
        n: "199",
    },
    {
        t: "Python学习网址及笔记",
        u: "imgs/banner01.jpg",
        n: "199",
    }
]
// 使用流程
// 1.遍历数组，获取每一项元素对象
// 2.将获取的元素对象填充到模板中
// 3.向页面元素追加模板
for (var j=0;j<arrPics.length;j++){
    var _HTML = pics.template(arrPics[j].u,
                             arrPics[j].n,
                             arrPics[j].t,);
    $("#pics").append(_HTML);
}
