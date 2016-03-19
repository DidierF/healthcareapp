$('#button-id-savebtn').on('click', function(){
    $.ajax({
        url: '/api/v1/patients/',
        method: 'post',
        data: $('#patientForm').serialize(),
//        beforeSend: function(jqXHR){
//            jqXHR.setRequestHeader('X-CSRFToken',$('input[name="csrfmiddlewaretoken"]').val());
//        }
    })
    .done(function(data, textStatus, jqXHR) {
//        TODO: return patient id to redirect to its edition page
        console.log(data);
        console.log(textStatus);
        console.log(jqXHR);
        switch(jqXHR.status){
            case 201:
                window.location.href = '/patients/'
                break;
            case 400:
                break;
        }
    });
});


$( "#id_date_of_birth" ).datepicker({
    dateFormat: "yy-mm-dd",
    minDate: "-100Y",
    changeMonth: true,
    changeYear: true
});