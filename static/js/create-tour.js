$('#saveTour').click(function(){
    $.ajax('/create-tour', {
        'type': 'POST',
        'async': true,
        'dataType': 'json',
        'data': {
            'name': $('#tourName').val(),
            'city': $('#tourCity').val(),
            'days': $('#tourDays').val(),
            'price': $('#tourPrice').val(),
            'date': $('#tourDate').val()
                },

        'success': function(response){
                var addTour = `
                                    <td>${response.name}</td>
                                    <td>${response.city}</td>
                                    <td>${response.days}</td>
                                    <td>${response.price}</td>
                                    <td>${response.date}</td>
                                    <td>
                                        <p class="text-success">Done</p>
                                    </td>`

                document.getElementById(`tour${response.id}`).innerHTML = addTour

        }






//            'success': function(response){
//
//               let tours =  document.getElementById(`tourCard${response.tour_id}`);
//               let newTour = `
//                                <tr>
//                                    <td>${$('#tourName').val()}</td>
//                                    <td>${$('#tourCity').val()}</td>
//                                    <td>${$('#tourDays').val()}</td>
//                                    <td>${$('#tourPrice').val()}</td>
//                                    <td>${$('#tourDate').val()}</td>
//                                </tr>`
//
//            toursDiv.innerHTML = `<h3>${$('#tourName').val()}</h3>` + toursDiv.innerHTML;
//            toursDiv.innerHTML = `<h3>${$('#tourCity').val()}</h3>` + toursDiv.innerHTML;
//            toursDiv.innerHTML = `<h3>${$('#tourDays').val()}</h3>` + toursDiv.innerHTML;
//            toursDiv.innerHTML = `<h3>${$('#tourPrice').val()}</h3>`+ toursDiv.innerHTML;
//            toursDiv.innerHTML = `<h3>${$('#tourDate').val()}</h3>` + toursDiv.innerHTML;
//                $('#tourName').val(''),
//                $('#tourCity').val(''),
//                $('#tourDays').val(''),
//                $('#tourPrice').val(''),
//                $('#tourDate').val('')
//        }
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

//            toursDiv.innerHTML = `<h3>${$('#tourName').val()}</h3>` + toursDiv.innerHTML;
//            toursDiv.innerHTML = `<h3>${$('#tourCity').val()}</h3>` + toursDiv.innerHTML;
//            toursDiv.innerHTML = `<h3>${$('#tourDays').val()}</h3>` + toursDiv.innerHTML;
//            toursDiv.innerHTML = `<h3>${$('#tourPrice').val()}</h3>`+ toursDiv.innerHTML;
//            toursDiv.innerHTML = `<h3>${$('#tourDate').val()}</h3>` + toursDiv.innerHTML;
//                $('#tourName').val(''),
//                $('#tourCity').val(''),
//                $('#tourDays').val(''),
//                $('#tourPrice').val(''),
//                $('#tourDate').val('')
