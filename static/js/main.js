$(function() {

    $(".right-bar, .left-bar").click(function(){
		var position = $(".image-container").css("left");
		var divWidth = $(".image-container").parent().width();
		var numImages = $(".image-container figure").length - 1;
		var slideIndex = Math.round(parseInt(position,10) / divWidth * -1);
        console.log(position, slideIndex);
		if ($(this).hasClass("right-bar")) {
		    if (slideIndex < numImages){
    		    var newSlideIndex = ++slideIndex;
		    } else {
		        var newSlideIndex = 0;
		    }
		} else {
		    if (slideIndex > 0){
		        var newSlideIndex = --slideIndex;
		    } else {
		        var newSlideIndex = numImages;
		    }
		}
		var newPosition = newSlideIndex * (-100);
        console.log(newPosition, newSlideIndex);
        $(".image-container").css("left", newPosition + "%");
    });
    function slideResize () {
        currentWidth = $(".slideshow").width();
        if ($(".slideshow").hasClass("vertical-layout")) {
            proportionedHeight = currentWidth * percentageHeight / 600;
            $(".left-bar, .right-bar").css({"height": proportionedHeight + "px", "margin-top": proportionedHeight * 2.5 + "px", "width": proportionedHeight/2 + "px"});
        } else if (currentWidth) {
            proportionedHeight = currentWidth * percentageHeight / 300;
            $(".left-bar, .right-bar").css({"height": proportionedHeight + "px", "margin-top": proportionedHeight + "px", "width": proportionedHeight/2 + "px"});
        }
    }
    slideResize();
    window.addEventListener('resize', function(event){
        slideResize();
    });
    $("#loginForm").submit(function(e){
        e.preventDefault();
        jQuery.ajax({
            url: '.',
            method: 'POST',
            data: $('#loginForm').serialize()
        }).done(function(response) {
            if (response == "success") {
                location.reload();
            } else {
                $(".errors").html(response).css("height", "1.5em");
            }
        }).fail(function() {
            alert("Whoops! We had an error; please try again!");
        })
        
    });
});
