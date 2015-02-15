function getArticleText(abs_url, id) {
    if ($('.read-more:eq(' + id + ')').html() === "Read More") {
        //if ($('#news-content-' + id + '.news-text').html() === "") {
        console.log("Ajaxing");
        $.ajax({
                url: "/newstext" + abs_url,
            })
            .done(function(data) {
                $('#news-content-' + id + ' .news-text').html("");
                $('#news-content-' + id + ' .news-teaser').hide();
                $('#news-content-' + id + ' .news-text').append(data).slideDown("slow");
                //$('#news-content-' + id + ' .news-text').show('slow');
                $('.read-more:eq(' + id + ')').html("Read Less");
            });
        //} else {
        //    $('#news-content-' + id + ' .news-teaser').show();
        //        $('#news-content-' + id + ' .news-text').hide();
        //        $('.read-more:eq(' + id + ')').html("Read More");
        //    }
    } else {
        $('#news-content-' + id + ' .news-text').slideUp('slow', function() {
            $('#news-content-' + id + ' .news-teaser').show('fast');
        });
        $('.read-more:eq(' + id + ')').html("Read More");
    }
}
