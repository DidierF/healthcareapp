$('#saveBtn').on('click', function(){
    $.ajax({
        url: '/api/v1/patients/',
        method: 'post',
        data: $('#patientForm').serialize()
    })
    .done(function(data, textStatus, jqXHR) {
//        TODO: return patient id to redirect to its edition page
        console.log(data);
        console.log(textStatus);
        console.log(jqXHR);
        switch(jqXHR.status){
            case 201:
                window.location.href = '/patient/'
                break;
            case 400:
                break;
        }
    });
});