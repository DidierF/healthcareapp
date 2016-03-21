$('#addForm').on('click', function(){
    $('#chooseForm').toggle();

});
$('#selectBtn').on('click', function(){
    console.log($('#selectForm').val());
    window.location.href = '/medic_forms/' + $('#selectForm').val() +
                            '/?p=' + $('#patient_id').val();
});