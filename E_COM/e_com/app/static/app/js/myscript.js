$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('.plus-cart').click(function(){
    var id = $(this).attr('pid').toString();
    var element = $('#quantity');
    $.ajax({
        type:'GET',
        url:'/pluscart',
        data:{
            product_id : id
        },
        success:function(data){
            element.text(data.quantity); //$('#quantity').text(data.quantity); is steade of element.
            $('#total_amount').text(data.total_amount);
            $('#temp_amount').text(data.temp_amount);
        }
    })
})

$('.minus-cart').click(function(){
    var id = $(this).attr('pid').toString();
    var element = $('#quantity');
    $.ajax({
        type:'GET',
        url:'/minuscart',
        data:{
            product_id : id
        },
        success:function(data){
            element.text(data.quantity); //$('#quantity').text(data.quantity); is steade of element.
            $('#total_amount').text(data.total_amount);
            $('#temp_amount').text(data.temp_amount);
        }
    })
})


$('.remove-cart').click(function(){
    var id = $(this).attr('pid').toString();
    var item = this
    console.log(id);
    $.ajax({
        type:'GET',
        url:'/removecart',
        data:{
            product_id : id
        },
        success:function(data){
            $('#temp_amount').text(data.temp_amount);
            $('#total_amount').text(data.total_amount);
            item.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})



