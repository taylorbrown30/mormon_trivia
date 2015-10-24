$(function() {

    $("#friends_button").click(function() {
        History.pushState({url:"index.friends"}, "", "");
    });
    //$("#random_button").click(function() {
    //    History.pushState({url:"index.random"}, "", "");
    //});


    $("#random_button").click(function() {
        $('.loader').show();

        $.ajax({
            url: "trivia/index.create_game/",
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