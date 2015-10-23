var current_category = 0;
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


$("#play_button").click(function() {

    History.pushState({url:null}, "", "");
    var game_id= $(this).attr("data-game_id");
    var category_id = current_category;
    $('.loader').show();

    $.ajax({
        url: "trivia/index.question/"+ game_id+"/"+category_id ,
        success: function (result) {
            $('.loader').hide();
            $("#panel_contents").html(result)
        }
    });
});

// **************************Spinner Wheel ************************

//set default degree (360*5)
var degree = 1800;
//number of clicks = 0
var clicks = 0;

$(document).ready(function(){

	/*WHEEL SPIN FUNCTION*/
	$('#spin').click(function(){

		//add 1 every click
		clicks ++;

		/*multiply the degree by number of clicks
	  generate random number between 1 - 360,
    then add to the new degree*/
		var newDegree = degree*clicks;
		var extraDegree = Math.floor(Math.random() * (360 - 1 + 1)) + 1;
		totalDegree = newDegree+extraDegree;

		/*let's make the spin btn to tilt every
		time the edge of the section hits
		the indicator*/
		//$('#wheel .sec').each(function(){
		//	var t = $(this);
		//	var noY = 0;
        //
		//	var c = 0;
		//	var n = 700;
		//	var interval = setInterval(function () {
		//		c++;
		//		if (c === n) {
		//			clearInterval(interval);
		//		}
        //
		//		var aoY = t.offset().top;
		//		$("#txt").html(aoY);
		//		console.log(aoY);
        //
		//		/*23.7 is the minumum offset number that
		//		each section can get, in a 30 angle degree.
		//		So, if the offset reaches 23.7, then we know
		//		that it has a 30 degree angle and therefore,
		//		exactly aligned with the spin btn*/
		//		if(aoY < 23.89){
		//			console.log('<<<<<<<<');
		//			$('#spin').addClass('spin');
		//			setTimeout(function () {
		//				$('#spin').removeClass('spin');
		//			}, 100);
		//		}
		//	}, 10);

        $('#inner-wheel').css({
            'transform' : 'rotate(' + totalDegree + 'deg)'
        });
        $("#inner-wheel").one('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend', function(e) {
            console.log("DONE!!!");
            $('.loading').show();
            $('#play_button').show();

            if(extraDegree >= 46 && extraDegree <= 138){
                $('.category_name#cat_1').show(); // Culture
                current_category=4
            }
            if(extraDegree >= 139 && extraDegree <= 228){
                $('.category_name#cat_2').show(); //History
                current_category=2
            }
            if(extraDegree >= 229 && extraDegree <= 312){
                $('.category_name#cat_3').show(); //BOM
                current_category=1
            }if(extraDegree >= 313 || extraDegree <= 45){
                $('.category_name#cat_4').show(); //Prophets
                current_category=3
            }


        });

        console.log("here1");
        console.log(extraDegree);
		//	noY = t.offset().top;
        //
		//});
	});
});//DOCUMENT READY


