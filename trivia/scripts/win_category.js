$(function() {

    var number_right = $('#outer_gauge').attr('number-right');
    console.log(number_right);

    var g = new JustGage({
        id: "gauge",
        value: number_right,
        min: 0,
        max: 3,
        hideMinMax: true,
        customSectors: [{
            color : "#337ab7",
            lo : 0,
            hi : 1
        },{
            color : "#5CB85C",
            lo : 1,
            hi : 2
        }, {
            color : "#BD0000",
            lo : 2,
            hi : 3
        }]
    });

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
});


