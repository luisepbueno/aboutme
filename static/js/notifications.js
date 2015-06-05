/* notifications every 10 seconds */
var notification_delay = 10000;

$(document).ready(function() {
    /* hide all notification icons */
    $(".notification-icon").hide();
    
    /* get notifications for the first time */
    //getNotifications();
    
    /* schedule notification */
    //setTimeout(getNotifications(), notification_delay);
});

function getNotifications() {
    var jqxhr = $.getJSON("/jsonui/notifications", function(data) {
        
    });
    jqxhr.done(function(data) {
        for (key in data) {
            var value=data[key];
            setNotification(
                $(".menu-item#"+key),
                $(".notification-icon#"+key),
                value);
        }
    });
        /*.fail(function() {
            // do nothing in case o failure
        })*/
    
    /* schedule again */
    //setTimeout(getNotifications(), notification_delay);
}

function setNotification(menu_item, notif, count) {

    if(count==0) {
        notif.hide();
        return;
    }

    new_top = menu_item.offset().top;
    new_left = menu_item.offset().left + menu_item.width() /*- notif.width()*/;

    notif.html(count);
    notif.offset({top: new_top, left: new_left});
    notif.show();
}