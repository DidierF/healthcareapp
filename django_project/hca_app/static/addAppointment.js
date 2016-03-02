$('#saveBtn').on('click', function(){
    $.ajax({
        url: '/api/v1/appointments/',
        method: 'post',
        data: $('#appointmentForm').serialize()
    })
    .done(function(data, textStatus, jqXHR) {
//        TODO: return appointment id to redirect to its edition page
        console.log(data);
        console.log(textStatus);
        console.log(jqXHR);
        switch(jqXHR.status){
            case 201:
                window.location.href = '/appointments/'
                break;
            case 400:
                break;
        }
    });
});