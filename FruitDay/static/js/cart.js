$(function(){

    //下拉菜单 添加点击事件,传值显示
    $('.select li').each(function (){
        $(this).click(function (){
            
            $('.currentAddress').html($(this).html());
        });
    });

    //图片轮播
    var imgIndex = 0;
    var timerId = setInterval(autoplay,1000);
    function autoplay(){
        //隐藏所有图片
        $('#banner img').each(function (){
            $(this).css('display','none');

        });
        //下标操作
        // if(++imgIndex){

        // }
        imgIndex = ++imgIndex == $('#banner img').length ? 0 :imgIndex;
        //显示
        $('#banner img').eq(imgIndex).css('display','block');

        //切换索引:修改背景色为灰色
        $('#banner li').each(function (){
            $(this).css('background','gray');

        });
        //图片下标对应的元素,背景色改为红色
        $('#banner li').eq(imgIndex).css('background','red');

        

   
    };
    
//鼠标移入移出操作定时器
$('#banner').bind('mouseover',function (){

    //鼠标移入,停止定时器
    clearInterval(timerId);
})

$('#banner').mouseout(function(){
    //鼠标移处,重启定时器
    timerId = setInterval(autoplay,1000)
})
    
});


$(function(){
    countItem();
    //1.全选和取消全选
    var isChecked = false;
    $("#checkAll").click(function (){
        isChecked = !isChecked;
        if(isChecked){
        //获取商品信息中的按钮,更改选中状态
        $("[name=check]").prop("checked","true");
            
        }else{
            //取消全选
            $("[name=check]").removeAttr("checked")
        }
        countItem();
    })
    //2.反选-商品选择状态改变全选按钮
    $("[name=check]").change(function(){
        //onclick  监听按钮状态改变
        //商品按钮 如果全选中,修改全选按钮
        //只要有一个商品按钮未被选中,全选也不能选中
        //未被选中的按钮数量 ==0 ->全选

        //input:checked 表示被选中的按钮
        //size() 获取元素的数量 等价于 length

        if($("[name=check]").not("input:checked").size() == 0){
            //全选
            $("#checkAll").prop("checked","true");
            isChecked = true;
        }else{
            // $("#checkAll").prop("checked","false");
            $("#checkAll").removeAttr("checked");

            isChecked = false;
        }
        countItem()
    });
    //3.数量加减
    $(".add").click(function (){
        //取前一个兄弟元素的文本内容
        var value = Number($(this).prev().val());
        //
        $(this).prev().val(++value);
        //价格联动
        //取单价
        var priceStr = $(this).parent().prev().html(); //$188
        //数值字符串
        var price = Number(priceStr.substring(1));
        //小计
        $(this).parent().next().html("<b>&yen;"+value*price + "</b>")
        countItem()
    });
    $(".minus").click(function (){
        //取后一个兄弟元素
        var value = Number($(this).next().val());
        //value > 1 才能做减法
        if(value > 1){
        $(this).next().val(--value);
        }
        var priceStr = $(this).parent().prev().html(); //$188
        //数值字符串
        var price = Number(priceStr.substring(1));
        //小计
        $(this).parent().next().html("<b>&yen;"+value*price + "</b>")
        countItem()
    });
    //输入数量,价格联动
    $(".count input").blur(function(){
        //输入数量,失去焦点时价格联动
        var value = Number($(this).val());
         //取单价
         var priceStr = $(this).parent().prev().html(); //$188
         //数值字符串
         var price = Number(priceStr.substring(1));
         //小计
         $(this).parent().next().html("<b>&yen;"+value*price + "</b>")
         countItem()

    })
    //4. 移除
    $(".g-item .action").click(function (){
        //点击哪个商品栏,移除当前信息
        $(this).parent().remove();
        countItem()
    })

    //5.总价格和总数量
    function countItem(){
        var sum = 0;
        var sumPrice = 0;
        //1.获取被选中的商品
        $("[name=check]:checked").each(function (){
            //每取依次运行一次,获取当前商品的数量和小计
            //.g-item --> .count .sum
            sum += Number($(this).parents(".g-item").find(".count input").val());
            var priceStr = $(this).parents(".g-item").find(".sum b").html();
            var price = Number(priceStr.substring(1));
            sumPrice += price
        })
        //2.显示在工具栏
        $(".submit-count span").html(sum);
        $(".submit-price span").html("&yen;"+sumPrice)
    }
})






