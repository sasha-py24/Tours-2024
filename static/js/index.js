$('#saveTour').click(function(){
  $.ajax('/create-tour', {
        'type': 'POST',
        'async': true,
        'dataType': 'json',
        'data':{
            'name': $('#tourName').val(),
        },

        'success': function(responce){
        //                <!-- записуємо окрему змінну дів і викликаємо: -->
                let tourDiv = document.getElementById('tours');
        //                <!--він дорівнює новому туру і вст назву в середину і додоємо код HTML щоб додався на початок -->
                tourDiv.innerHTML = `<h3>${$('#tourName').val()}</h3>` + tourDiv.innerHTML;
                $('#tourName').val('');//очистка форми

                let tourModal = new bootstrap.Modal('#tourModal', options);
                tourModal.hide();
//                викликаємо hide і закриваємо вікно

        }
  })
});







