$('#submit-id-registerbtn').on('click', function(){
    $.ajax({
        url: '/api/v1/doctors/',
        method: 'post',
        data: $('#registerForm').serialize()
    })
    .done(function( data, textStatus, jqXHR ) {
        console.log(data);
        console.log(textStatus);
        console.log(jqXHR);
    });
});