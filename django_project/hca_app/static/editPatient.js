var url = '/api/v1/patients/'+$('#patientId').val();

$('#saveBtn').on('click', function(){
    $.ajax({
        url: url,
        method: 'put',
        data: $('#patientForm').serialize(),
        beforeSend: function(jqXHR){
            jqXHR.setRequestHeader('X-CSRFToken',$('input[name=csrfmiddlewaretoken]').val());
        }
    })
    .done(function(data, textStatus, jqXHR) {
        switch(jqXHR.status){
            case 200:
                console.log('Patient Saved');
                break;
            case 404:
                console.log('Patient was not found.');
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
                alert('Patient Deleted');
                window.location.href = '/patient'
                break;
            case 404:
                console.log('Patient was not found.');
                break;
        }
    });
});