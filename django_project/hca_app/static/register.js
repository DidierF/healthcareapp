$('#registerBtn').on('click', function(){
    $.ajax({
        url: '/api/v1/register',
        method: 'post',
        data: $('#registerForm').serialize()
    })
    .done(function( data, textStatus, jqXHR ) {
        console.log(data);
        console.log(textStatus);
        console.log(jqXHR);
    });
});