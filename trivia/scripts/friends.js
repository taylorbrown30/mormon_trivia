$(function() {

    $(".play_friend_button").click(function() {
        $('.loader').show();
        var id = $(this).attr('id');
        $.ajax({
            url: "trivia/index.create_game/" + id,
            success: function (result) {
                data = JSON.parse(result);
                if (data["success"]) {
                    var game_id = data["id"];
                    History.pushState({url:"index.category/" + game_id}, "", "");
                }
            }
        });
    });
});