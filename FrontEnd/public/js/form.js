$(function() {

    $('#submit').on('click', function(){
        event.preventDefault();
        var value = $("#stext").val();
        //alert(value);
        console.log(value)
        var requestConfig = {
            method: "POST",
            url: 'http://127.0.0.1:5000/',
            contentType: 'application/json',
            data : {text : value}
          };
        $.ajax({
            type: "POST",
            url: 'http://127.0.0.1:5000/', 
            contentType: 'application/json', 
            data : JSON.stringify({text : value}) ,                                                   
            success: function(data) {
                $('#links').empty()
                console.log("In success"+ data.data);
                //alert("In success" + data.data)
                $('#result-container').removeClass('hidden');
                for(var i=0; i<data.data.length; i++){
                    $('#links').append($('<div></div>').append($('<a></a>')
                                                                            .text(data.data[i])
                                                                            .attr("href",data.data[i])))
                }

            },
            error: function(error){
                console.log(error)
                //alert(error)
                $('#result-container').addClass('hidden');
            }
        });


        // $.ajax(requestConfig).then(function(response){
        //     alert(response)

        // });
     });

     
  });
  