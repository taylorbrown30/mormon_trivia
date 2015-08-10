$(function() {

    $("#friends_button").click(function() {
        $('.loader').show()
        History.pushState({url:"index.friends"}, "", "");
        $.ajax({
            url: "/trivia/index.friends" ,
            success: function (result) {
                $('.loader').hide()
                $("#panel_contents").html(result)
            }
        });
    });
    $("#random_button").click(function() {

        $.ajax({
            url: "/trivia/index.random" ,
            success: function (result) {
                $("#panel_contents").html(result)
            }
        });
    });


});