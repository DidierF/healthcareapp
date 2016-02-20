$('#registerBtn').on('click', function(){
    $.post('/api/v1/register', $('#registerForm').serialize())
});