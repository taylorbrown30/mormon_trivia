$(function() {
    //Once page loads
    //$.ajax({
    //    url: "trivia/index.spin_ajax" ,
    //    success: function (result) {
    //        $("#panel_contents").html(result)
    //    }
    //});

    $(".play_friend_button").click(function() {
        $('.loader').show()
        History.pushState({url:"index.create_game"}, "", "");
        var id = $(this).attr('id');
        $.ajax({
            url: "trivia/index.create_game/" + id,
            success: function (result) {
                $('.loader').hide()
                $("#panel_contents").html(result)
            }
        });
    });


});