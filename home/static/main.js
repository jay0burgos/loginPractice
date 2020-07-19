$('form').submit(function(event){
    event.preventDefault();
    var form = $(this);//get data from the event, through $(this)
    $.ajax({
        url: '/create',
        method: 'POST',
        data: form.serialize()
    }).done(function(response){
        $('tbody').html(response)
    })
})

$(document).ready(function(){
    $.ajax({
        url:'/fetch',
        method: 'GET'
    }).done(function(response){
        $('tbody').html(response)
    })
})