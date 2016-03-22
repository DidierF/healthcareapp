$('#button-id-savebtn').on('click', function(){
    $.ajax({
        url: '/api/v1/ophthalmology/',
        method: 'post',
        data: $('#ophthalmologyForm').serialize()
    })
    .done(function( data, textStatus, jqXHR ) {
        console.log(data);
        console.log(textStatus);
        console.log(jqXHR);
    });
});