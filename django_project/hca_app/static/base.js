var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = decodeURIComponent(window.location.search.substring(1)),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : sParameterName[1];
        }
    }
};

$('#logout').on('click', function(){
    $.ajax({
        url: '/api/v1/logout',
        method: 'post',
        beforeSend: function(jqXHR){
            jqXHR.setRequestHeader('X-CSRFToken',$('#logoutToken').val());
        }
    }).done(function(){
        window.location.href = '/';
    });
});