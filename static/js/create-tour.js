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
                                    <li>${response.name}</li>
                                    <li>${response.city}</li>
                                    <li>${response.days}</li>
                                    <li>${response.price}</li>
                                    <li>${response.date}</li>
                                    `

                document.getElementById(`tourCard${response.id}`).innerHTML = addTour

        }

//                                `
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

