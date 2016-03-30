$('#button-id-savebtn').on('click', function(){
    var customData = [];

    $.each($('.customField'), function(index, value){
        customData.push({'title':$(this).find(".title").val(), 'content':$(this).find(".content").val()});
    });
    if($('#form_id').length){
        $.ajax({
            url: '/api/v1/ophthalmology/' + $('#form_id').val(),
            method: 'put',
            data: $('#ophthalmologyForm').serialize() + '&customData=' + JSON.stringify(customData),
            beforeSend: function(jqXHR){
                jqXHR.setRequestHeader('X-CSRFToken',$('input[name=csrfmiddlewaretoken]').val());
            }
        })
        .done(function( data, textStatus, jqXHR ) {
//            console.log(data);
//            console.log(textStatus);
//            console.log(jqXHR);
        });
    } else {
        $.ajax({
            url: '/api/v1/ophthalmology/',
            method: 'post',
            data: $('#ophthalmologyForm').serialize() + '&customData=' + JSON.stringify(customData)
        })
        .done(function( data, textStatus, jqXHR ) {
            console.log(data);
            console.log(textStatus);
            console.log(jqXHR);
        });
    }
});

$('#deleteBtn').on('click', function(){
    $.ajax({
        url: '/api/v1/ophthalmology/' + $('#form_id').val(),
        method: 'delete',
        beforeSend: function(jqXHR){
            jqXHR.setRequestHeader('X-CSRFToken',$('input[name=csrfmiddlewaretoken]').val());
        }
    })
    .done(function(data, textStatus, jqXHR) {
        switch(jqXHR.status){
            case 204:
                console.log('Ophth form deleted');
                history.go(-1);
                break;
            case 404:
                console.log('Ophth form  was not found.');
                break;
        }
    });
});

$('#id_date').datepicker({
    dateFormat: "yy-mm-dd",
    minDate: "-100Y",
    changeMonth: true,
    changeYear: true
});

$('#addFieldBtn').on('click', function(){
    $('#button-id-savebtn').parent().parent().before(
        '<div class="customField form-group">' +
            '<label class="control-label">Title</label>' +
            '<input class="title textinput textInput form-control" type="text"/>' +

            '<label class="control-label">Content</label>' +
            '<input class="content textinput textInput form-control" type="text"/>' +
        '</div>'
    );
});