var url = '/api/v1/prescriptions/'+$('#prescriptionId').val();

$('#button-id-savebtn').on('click', function(){
    $.ajax({
        url: url,
        method: 'put',
        data: $('#prescriptionForm').serialize()
    })
    .done(function(data, textStatus, jqXHR) {
        switch(jqXHR.status){
            case 200:
                console.log('Prescription Saved');
                break;
            case 404:
                console.log('Prescription was not found.');
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
                alert('Prescription Deleted');
                window.location.href = '/prescriptions'
                break;
            case 404:
                console.log('Prescription was not found.');
                break;
        }
    });
});