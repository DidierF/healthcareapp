$('#button-id-loginbtn').on('click', function(){
    $.ajax({
        url: '/api/v1/login',
        method: 'post',
        data: $('#loginForm').serialize()
    })
    .done(function( data, textStatus, jqXHR ) {
        console.log(jqXHR);
        switch(jqXHR.status){
            case 200:
                var next = getUrlParameter('next');
                if (next){
                    window.location.href = next;
                } else {
                    window.location.href = '/dashboard/';
                }
                break;
            case 401:
                break;
        }
    });
});

$(document).ready(function() {
    $('#loginForm').formValidation({
        framework: 'bootstrap',
        icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            id_username: {
                validators: {
                    notEmpty: {
                        message: 'The username is required'
                    },
                    stringLength: {
                        min: 6,
                        max: 30,
                        message: 'The username must be more than 6 and less than 30 characters long'
                    },
                    regexp: {
                        regexp: /^[a-zA-Z0-9_]+$/,
                        message: 'The username can only consist of alphabetical, number and underscore'
                    }
                }
            },
            password: {
                validators: {
                    notEmpty: {
                        message: 'The password is required'
                    }
                }
            }
        }
    });
});