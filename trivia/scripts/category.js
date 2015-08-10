
$("#play_button").click(function() {
    $('.loader').show()
	History.pushState({url:"index.question"}, "", "");
    var game_id= $(this).attr("data-game_id");
    var category_id = 1;
	$.ajax({
		url: "trivia/index.question/"+ game_id+"/"+category_id ,
		success: function (result) {
			$('.loader').hide()
			$("#panel_contents").html(result)
		}
	});
});

