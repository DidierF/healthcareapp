$('#registerBtn').on('click', function(){
    console.log($('#registerForm').serialize());
    $.post('/api/v1/register', $('#registerForm').serialize())
});