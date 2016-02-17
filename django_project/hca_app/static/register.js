$('#registerBtn').on('click', function(){
//    $.ajax({
//        url: '/api_register',
//
//    })
    console.log($('#registerForm').serialize());
    $.post('/api/v1/register', $('#registerForm').serialize())
});