var url = '/api/v1/doctors/'+$('#doctorId').val();

$('#saveBtn').on('click', function(){
    $.ajax({
        url: url,
        method: 'put',
        data: $('#doctorForm').serialize(),
        beforeSend: function(jqXHR){
            jqXHR.setRequestHeader('X-CSRFToken',$('input[name=csrfmiddlewaretoken]').val());
        }
    })
    .done(function(data, textStatus, jqXHR) {
        switch(jqXHR.status){
            case 200:
                console.log('Doctor Saved');
                break;
            case 404:
                console.log('Doctor was not found.');
                break;
        }
    });
});

$('#deleteBtn').on('click', function(){
    $.ajax({
        url: url,
        method: 'delete',
        beforeSend: function(jqXHR){
            jqXHR.setRequestHeader('X-CSRFToken',$('input[name=csrfmiddlewaretoken]').val());
        }
    })
    .done(function(data, textStatus, jqXHR) {
        switch(jqXHR.status){
            case 204:
                console.log('Doctor Deleted');
                window.location.href = '/doctors'
                break;
            case 404:
                console.log('Doctor was not found.');
                break;
        }
    });
});