$(document).ready(function () {
    let sidebarMenuItem = $('.sidebar-menu-item');
    let sidebarGroupTitle = $('.sidebar-group-title');
    let sidebarSingleItem = $('.sidebar-single-item');
    let menuItems = $('.menu-items');

    sidebarMenuItem.click(function () {
        sidebarMenuItem.removeClass('active');
        sidebarGroupTitle.removeClass('active');
        sidebarSingleItem.removeClass('active');
        $(this).addClass('active');
        $(this).parent().prev('.sidebar-group-title').addClass('active');
    });

    sidebarSingleItem.click(function () {
        sidebarMenuItem.removeClass('active');
        sidebarGroupTitle.removeClass('active');
        sidebarSingleItem.removeClass('active');
        $(this).addClass('active');
    });

    function hideMenuItems() {
        menuItems.collapse('hide');
    }

    let collapsedSidebar = false;
    $('#sidebar-toggle').click(function () {
        collapsedSidebar = !collapsedSidebar;
        $(this).toggleClass('rotate');
        $('#sidebar-menu, #brand').toggleClass('collapsed-sidebar');
        if (collapsedSidebar===true){
            $(document).on('click', hideMenuItems)
        }else{
            $(document).off('click', hideMenuItems)
        }
    });
});

