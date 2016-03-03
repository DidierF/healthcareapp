var url = '/api/v1/appointments/'+$('#appointmentId').val();

$('#saveBtn').on('click', function(){
    $.ajax({
        url: url,
        method: 'put',
        data: $('#appointmentForm').serialize(),
        beforeSend: function(jqXHR){
            jqXHR.setRequestHeader('X-CSRFToken',$('input[name=csrfmiddlewaretoken]').val());
        }
    })
    .done(function(data, textStatus, jqXHR) {
        switch(jqXHR.status){
            case 200:
                console.log('Appointment Saved');
                break;
            case 404:
                console.log('Appointment was not found.');
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
                alert('Appointment Deleted');
                window.location.href = '/appointments'
                break;
            case 404:
                console.log('Appointment was not found.');
                break;
        }
    });
});