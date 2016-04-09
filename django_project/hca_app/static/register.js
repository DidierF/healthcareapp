$('#button-id-savebtn').on('click', function(){
    console.log('register');
    $.ajax({
        url: '/api/v1/doctors/',
        method: 'post',
        data: $('#doctorForm').serialize()
    })
    .done(function( data, textStatus, jqXHR ) {
        console.log(data);
        console.log(textStatus);
        console.log(jqXHR);
    });
});