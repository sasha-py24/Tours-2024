$('#saveTour').click(function(){
    $.ajax('/create-tour', {
        'type': 'POST',
        'async': true,
        'dataType': 'json',
        'data': {
            'name': $('#tourName').val(),
            'date': $('#tourCity').val(),
            'days': $('#tourDays').val(),
            'price': $('#tourPrice').val(),
            'data': $('#tourDate').val()
                },

            'success': function(response){


//               let tours =  document.getElementById(`tour${response.tour_id}`);
//               let newTask = ` <tr>
//                                    <td>${$('#taskName').val()}</td>
//                                    <td>${$('#taskDeadLine').val()}</td>
//                                    <td>${$('#taskPriority').val()}</td>
//                                    <td><p class="text-danger">Not Done</p></td>
//                               </tr>`

               tasks.innerHTML += `<h4>${$(`#tourName`).val()}</h4>`;
                $('#tourName').val(),
                $('#tourCity').val(),
                $('#tourDays').val(),
                $('#tourPrice').val(),
                $('#tourDate').val()
        }
    });
});















//        'success': function(response){
//                let toursDiv = document.getElementById('tours');                                    //записуємо окрему змінну дів і викликаємо: -->
//                toursDiv.innerHTML = `<h3>${$('#tourName').val()}</h3>` + toursDiv.innerHTML;       //він дорівнює новому туру і вст назву в середину і додоємо код HTML щоб додався на початок -->
//                $('#tourName').val('');                                                             //очистка форми//
//                let tourModal = new bootstrap.Modal('#tourModal');                                  //викликаємо hide і закриваємо вікно
//                tourModal.hide();
//                 }
//     })
//});

