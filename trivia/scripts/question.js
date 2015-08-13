$(function() {
    var answer_result = "";
    var game = "";
    $(".answer_button").click(function() {
        var question_id = $(this).attr('question');
        var answer = $(this).attr('id');
        var category = $(this).attr('category');
        game = $(this).attr('game_id');
        var game_data= { question_id: question_id, answer: answer, game: game, category: category };
        $.ajax({
            url: "trivia/index.check_answer/",
            data: game_data,
            success: function (result) {
                answer_result=result;
                //$(".answer_button").hide();
                $(".answer_button").css("visibility", "hidden");
                $("#continue_button").show();
                if(result == "correct"){
                    $("#answered_correct").show();
                    console.log($("#answered_correct"));
                }
                else if(result== "incorrect"){
                    $("#answered_incorrect").show()
                }
            }
        });
    });

    $("#continue_button").click(function() {
        $('.loader').show();

        if(answer_result == "correct"){

            $.ajax({
                url: "trivia/index.category/"+game ,
                success: function (result) {
                    $('.loader').hide();
                    $("#panel_contents").html(result)
                }
            });
        }else if(answer_result== "category"){
            $.ajax({
                url: "trivia/index.win_category/" + game,
                success: function (result) {
                    $('.loader').hide();
                    $("#panel_contents").html(result)
                }
            });
        }else if(answer_result== "won_game") {
            History.pushState({url:"index.home"}, "", "");
        }
        else if(answer_result== "incorrect") {
            History.pushState({url:"index.home"}, "", "");
        }
    });
});




