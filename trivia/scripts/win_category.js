
$(".category_button").click(function() {

    History.pushState({url:null}, "", "");
    var game_id= $(this).attr("data-game_id");
    var category_id = $(this).attr("id");
	$.ajax({
		url: "trivia/index.question/"+ game_id+"/"+category_id ,
		success: function (result) {
			$('.loader').hide()
			$("#panel_contents").html(result)
		}
	});
});

