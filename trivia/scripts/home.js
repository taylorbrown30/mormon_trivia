$(function() {


    $("#new_game_button").click(function() {
        $('.loader').show()
        History.pushState({url:"index.new_game"}, "", "");
        $.ajax({
            url: "/trivia/index.new_game" ,
            success: function (result) {
                $('.loader').hide()
                $("#panel_contents").html(result)

            }
        });
    });

    $(".play_game_button").click(function() {
        $('.loader').show()
        History.pushState({url:"index.category"}, "", "");
        var id = $(this).attr('id');
        $.ajax({
            url: "trivia/index.category/" + id ,
            success: function (result) {
                $('.loader').hide()
                $("#panel_contents").html(result)
            }
        });
    });

});