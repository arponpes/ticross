$(".iconEdit").on('click', function () {


  

    
    var target = $(this).data('target')
    $('#' + target).addClass('editMode')
    
});

$(".iconSave").on('click', function () {
    var target = $(this).data('target')
    $('#' + target).removeClass('editMode')

    var newName = $(this).parent().children('.newName').val()
    $(this).parent().children('.title').text(newName)
    $.ajax({
        type: "PATCH",
        url: '/api/projects/'+target+'/',
        data: { project_name: newName },
        success: function (response) {
            
        }

    });
});

