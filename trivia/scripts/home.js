$(function() {


    $("#new_game_button").click(function() {
        History.pushState({url:"index.new_game"}, "", "");

    });

    $(".play_game_button").click(function() {
        var id = $(this).attr('id');
        History.pushState({url:"index.category/" + id}, "", "");
    });

});