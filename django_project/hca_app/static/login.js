$('#loginBtn').on('click', function(){
    $.ajax({
        url: '/api/v1/login',
        method: 'post',
        data: $('#loginForm').serialize()
    })
    .done(function( data, textStatus, jqXHR ) {
        console.log(jqXHR);
        switch(jqXHR.status){
            case 200:
                var next = getUrlParameter('next');
                if (next){
                    window.location.href = next;
                } else {
                    window.location.href = '/dashboard/'
                }
                break;
            case 401:
                break;
        }
    });
});