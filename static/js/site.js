$(document).ready(function($) {
    $("header").find('.logo').click(function() {
        window.location.href = "/";
    });
    
    $("#flashes").find("span.ui-icon").click(function() {
        $(this).parent().remove();
    });
});