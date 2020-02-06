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

    function showMenuItems() {
        $(this).parent().children('.menu-items').collapse('show');
    }

    function hideMenuItems() {
        $(this).parent().children('.menu-items').collapse('hide');
    }

    let collapsedSidebar = false;
    $('#sidebar-toggle').click(function () {
        collapsedSidebar = !collapsedSidebar;
        $(this).toggleClass('rotate');
        $('#sidebar-menu, #brand').toggleClass('collapsed-sidebar');

        // if (collapsedSidebar === true) {
        //     sidebarGroupTitle.hover(showMenuItems, hideMenuItems);
        //
        //     menuItems.on('mouseenter', showMenuItems);
        //     menuItems.on('mouseleave', hideMenuItems);
        // } else {
        //     sidebarGroupTitle.off('mouseenter', showMenuItems);
        //     sidebarGroupTitle.off('mouseleave', hideMenuItems);
        //
        //     menuItems.off('mouseenter', showMenuItems);
        //     menuItems.off('mouseleave', hideMenuItems);
        // }
    });
});

