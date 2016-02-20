$('#loginBtn').on('click', function(){
    $.ajax({
        url: '/api/v1/login',
        method: 'post',
        data: $('#loginForm').serialize()
    })
    .done(function( data, textStatus, jqXHR ) {
        console.log(data);
        console.log(textStatus);
        console.log(jqXHR);
    });
});