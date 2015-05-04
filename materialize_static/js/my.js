$(document).ready(function() {
    //if ($(".brick").css("width") != "100%") {
    var wall = new freewall("#freewall");
    wall.reset({
        selector: '.brick',
        animate: true,
        cellW: function(width) {
            var cellWidth = width / 2;
            return cellWidth - 20;
        },
        cellH: 'auto',
        onResize: function() {
            wall.fitWidth();
        }
    });

    wall.container.find('.brick img').load(function() {
        wall.fitWidth();
    });
    console.log("running");
    //}
});
