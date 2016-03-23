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

$('#deleteBtn').on('click', function(){
    $.ajax({
        url: '/api/v1/ophthalmology/' + $('#form_id').val(),
        method: 'delete',
        beforeSend: function(jqXHR){
            jqXHR.setRequestHeader('X-CSRFToken',$('input[name=csrfmiddlewaretoken]').val());
        }
    })
    .done(function(data, textStatus, jqXHR) {
        switch(jqXHR.status){
            case 204:
                console.log('Ophth form deleted');
//                window.location.href = '/'
                history.go(-1);
                break;
            case 404:
                console.log('Ophth form  was not found.');
                break;
        }
    });
});