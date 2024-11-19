$('#saveTour').click(function(){
    $.ajax('/create-tour', {
        'type': 'POST',
        'async': true,
        'dataType': 'json',
        'data': {
            'name': $('#tourName').val(),
                },
        'success': function(response){
                let toursDiv = document.getElementById('tours');        //записуємо окрему змінну дів і викликаємо: -->
                toursDiv.innerHTML = `<h3>${$('#tourName').val()}</h3>` + toursDiv.innerHTML;       //він дорівнює новому туру і вст назву в середину і додоємо код HTML щоб додався на початок -->
                $('#tourName').val('');      //очистка форми//
                let tourModal = new bootstrap.Modal('#tourModal');     //викликаємо hide і закриваємо вікно
                tourModal.hide();
                 }
     })
});

