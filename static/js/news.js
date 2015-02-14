function getArticleText(abs_url, id) {
  $.ajax({
      url: "/newstext/"+abs_url,
    })
    .done(function(data) {
        $('.news-content').html(data);
    });
}
