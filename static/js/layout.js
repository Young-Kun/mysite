$('.sidebar-menu-item').click(function () {
    $('.sidebar-group-title').removeClass('active');
    $('.sidebar-menu-item').removeClass('active');
    $(this).addClass('active');
});

$('.sidebar-group-title').click(function () {
    $('.sidebar-group-title').removeClass('active');
    $('.sidebar-menu-item').removeClass('active');
    $(this).addClass('active');
});