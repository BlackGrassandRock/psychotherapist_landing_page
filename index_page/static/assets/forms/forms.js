$(document).ready(function(){
    if ($('#success').length) {
        setTimeout(function(){
            $('#success').fadeOut('slow');
        }, 3000);
    }
});