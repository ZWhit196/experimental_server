var ajaxobj = null, callback = null, errorback = null, showncol = null;


function SetAjaxArgs(o, c, e) { ajaxobj = o; callback = c; errorback = e; }

function NullAjaxArgs() { ajaxobj = null; callback = null; errorback = null; }

function AjaxCall() {
    $.ajax({
        url: window.location,
        method: 'POST',
        data: JSON.stringify( ajaxobj ),
        contentType: 'application/json'
    }).done(function(dt) {
        callback(dt);
        NullAjaxArgs();
    }).fail(function(e) {
        console.log("Failed processing", e.status, e.responseJSON.Message);
        alert("Data Request Error:  "+String(e.status)+"\n"+e.responseJSON.Message);
        errorback();
        NullAjaxArgs();
    });
}

function isInArray(target, array) {
    if( array.indexOf(target)>-1 ) return true;
    return false; 
}

function ToggleLoader(id, l_id) {
    if (!l_id) l_id = ".loader";
    if (typeof id == "object" && id.length > 0) for (var i=0; i<id.length; i++) $( id[i] ).find(l_id).toggle();
    else if (typeof id == "string") $(id).find(l_id).toggle();
}

function copyToClipboard(element) {
    var $temp = $("<input>");
    $("body").append($temp);
    $temp.val($(element).text()).select();
    document.execCommand("copy");
    $temp.remove();
}

function togglePassField(el) {
    // Toggle readability of password field given, switch between hidden text and readable text.
    if ( $( el ).prop("type") == "password" ) {
        $( el ).prop("type", "text");
        $( el ).prop("placeholder", "password");
    } else {
        $( el ).prop("type", "password");
        $( el ).prop("placeholder", "********");
    }
}