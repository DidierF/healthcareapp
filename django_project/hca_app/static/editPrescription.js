var url = '/api/v1/prescriptions/'+$('#prescriptionId').val();

$('#button-id-savebtn').on('click', function(){
    $.ajax({
        url: url,
        method: 'put',
        data: $('#prescriptionForm').serialize(),
        beforeSend: function(jqXHR){
            jqXHR.setRequestHeader('X-CSRFToken',$('input[name=csrfmiddlewaretoken]').val());
        }
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

$('#emailOpt').on('click', function(){
    $('#emailDiv').toggle();
});

$('#sendBtn').on('click', function(){
    $.ajax({
        url: '/api/v1/mail/prescriptions',
        method: 'post',
        data: 'email=' + $('#email').val() + '&prescription=' + $('#prescriptionId').val(),
        beforeSend: function(jqXHR){
            jqXHR.setRequestHeader('X-CSRFToken',$('input[name=csrfmiddlewaretoken]').val());
        }
    })
    .done(function(data, textStatus, jqXHR) {
        switch(jqXHR.status){
            case 200:
                alert('Email sent.');
                break;
        }
    })
    .fail(function(jqXHR, textStatus, errorThrown){
        if(jqXHR.status == 400){
            alert('There was an error sending the email.\nPlease try again.');
        }
    });
});