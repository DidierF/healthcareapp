$('#button-id-savebtn').on('click', function(){
    $.ajax({
        url: '/api/v1/prescriptions/',
        method: 'post',
        data: $('#prescriptionForm').serialize()
    })
    .done(function(data, textStatus, jqXHR) {
//        TODO: return appointment id to redirect to its edition page
        console.log(data);
        console.log(textStatus);
        console.log(jqXHR);
        switch(jqXHR.status){
            case 201:
//                window.location.href = '/appointments/'
                history.go(-1);
                break;
            case 400:
                break;
        }
    });
});