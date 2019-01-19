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


