    //asynchronous updating of the user table
$('form').submit(function(event){ //grabs form, and executes at clicking submit from the form
    event.preventDefault();
    var form = $(this);//gets data from the event, through $(this)
    $.ajax({
        url: '/create', //goes through this url to reach the views function to create a new user
        method: 'POST', //type of method
        data: form.serialize() //assigns the data from the created variable to be used
    }).done(function(response){ //after getting a response from the server, loads in the response onto the table
        $('tbody').html(response)
    })
})

$(document).ready(function(){ //used to attach the table body to the table through ajax
    $.ajax({ 
        url:'/fetch', //gets the pathway that leads to the views function that retrieves the data and html form
        method: 'GET'
    }).done(function(response){
        $('tbody').html(response) //assigns the response to the table
    })
})