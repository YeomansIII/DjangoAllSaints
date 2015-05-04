$(document).ready(function() {
/*
    var clickEvent = false;
    var id;
    $('#myCarousel').carousel({
        interval: 4000
    }).on('click', '.list-group li', function() {
        clickEvent = true;
        $('.list-group li').removeClass('active');
        $(this).addClass('active');
    }).on('slid.bs.carousel', function(e) {
        if (!clickEvent) {
            var count = $('.list-group-item').length-1;
            var current = $('.list-group li.active');
            var next=current.next();
            id = parseInt(current.data('slide-to'));
            current.removeClass('active')
            console.log("count: "+count+"  id:: "+id+"  array: "+$('.list-group-item').get(1));
            if (count == id) {
                $('.list-group-item').first().addClass('active');
            } else {
                id++;
                next.addClass('active');
            }
        }
        clickEvent = false;
    });*/
})

function canvas_size() {
    var offset = $('#quicklinks').offset();
    $('#home-background').css('height', offset.top);
}

$(window).load(function() {
    var boxheight = $('#myCarousel .carousel-inner').innerHeight();
    var itemlength = $('#myCarousel .item').length;
    var triggerheight = Math.round(boxheight / 5);
    $('#myCarousel .list-group-item').outerHeight(triggerheight);

    canvas_size();
});

$(window).resize( function() {
    canvas_size();
});
