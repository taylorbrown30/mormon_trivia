$(function() {
    var History = window.History;
    History.Adapter.bind(window,'statechange',function(){ // Note: We are using statechange instead of popstate
        var State = History.getState(); // Note: We are using History.getState() instead of event.state
        if (State){
            $('.loader').show();
            //$("#panel_contents").load(State.data.url);
            if(State.data.url != null){
                $.ajax({
                    url: State.data.url ,
                    success: function (result) {
                        $('.loader').hide();
                        $("#panel_contents").html(result)
                    }
                });
                console.log("Loading: "+ State.data.url)
            }
            else{
                $('.loader').hide();
            }


        }
        //History.log(State.data, State.title, State.url);
    });
    //Once page loads
    $('.loader').show();
    $.ajax({
        url: "trivia/index.home" ,
        success: function (result) {
            $('.loader').hide();
            $("#panel_contents").html(result);
            History.pushState({url:"index.home"}, "", "");

        }
    });
});