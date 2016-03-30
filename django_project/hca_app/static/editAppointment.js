var url = '/api/v1/appointments/'+$('#appointmentId').val();

$('#button-id-savebtn').on('click', function(){
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

$( "#id_date" ).datepicker({
    dateFormat: "yy-mm-dd",
    minDate: "-100Y",
    changeMonth: true,
    changeYear: true
});

$('#emailOpt').on('click', function(){
    $('#emailDiv').toggle();
});

$('#sendBtn').on('click', function(){
    $.ajax({
        url: '/api/v1/mail/appointments',
        method: 'post',
        data: 'email=' + $('#email').val() + '&appointment=' + $('#appointmentId').val(),
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