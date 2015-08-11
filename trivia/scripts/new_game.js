$(function() {

    $("#friends_button").click(function() {
        History.pushState({url:"index.friends"}, "", "");
    });
    $("#random_button").click(function() {
        History.pushState({url:"index.random"}, "", "");
    });

});