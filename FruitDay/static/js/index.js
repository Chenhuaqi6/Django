 function check_login() {
     $.get('/check_login/',function (data) {
            var html = ''
            if(data.loginStatus == 0){
                html += '<a href="/login">[登录]</a>'
                html += '<a href="/register">[注册有惊喜]</a>'

            }else{
                html += "欢迎:"+data.uname + ' '
                html += "<a href='/logout'>退出</a>"
            }
            //将html显示在指定的位置处
        $("#login").html(html)
     },'json')
 }

/*
* 加载所有的商品类型以及商品信息
* */
function loadgoods() {
   $.get('/type_goods',function (data) {
       var html = ''
       //循环遍历data中的数据
       $.each(data,function (i,obj) {

         html += "<div class='goodsType'>"

           //拼顶部标题
           //先将obj.type的值获取出来并转换成js对象
           var jsonType = JSON.parse(obj.type)

           html += "<p class ='goodsTitle'>"
           html += "<img src='/"+jsonType.picture+"'>"
           html += "<a href='#'>更多</a>"
           html += "</p>"

           //拼商品展示
          html += "<ul>"
           var jsonGoods = JSON.parse(obj.goods)
           $.each(jsonGoods,function (j,good) {
            html += "<li ";
               if((j+1) % 5 == 0){
                html += "class ='no-margin'"
               }
            html += ">"
               html +="<div>"
                    html += "<img src='/"+good.fields.picture+"'>"
               html +="</div>"
               html += "<a href='#'>"
                    html += "<img src='/static/images/cart.png'>"
               html += "</a>"
               html += "<p>"+good.fields.title+"</p>"
               html += "<span>"
                    html += "&yen;"+good.fields.price+"/"
                    html += good.fields.spec
               html += "</span>"
            html += "</li>"
           })

          html += "</ul>"
        html += "</div>"
       })
       $("#main").html(html)
   },'json')
}

$(function(){
    //调用加载商品类型和商品的方法
    loadgoods()

    //调用检查用户信息的方法 - check_login
    check_login()

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




/*
1.获取图片数组
2.开启定时器,切换下标取图片,控制隐藏与显示

*/ 
/*window.onload = function (){
    var imgIndex = 0;
    //#banner img
    var imgs = document.getElementById('banner').children;
    setInterval(function (){
        //display:none/block
        imgIndex++;
        //数组越界判断
        //隐藏图片
        //指定下标图片显示
        imgs[imgIndex].style.display = block;

    },1000);

};
*/


