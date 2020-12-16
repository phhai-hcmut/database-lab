

$('.shuffle').click(function(){
  $(this).toggleClass('clicked');
});

//music player settings

let audio = new Audio('');

$('.pause').hide(); //hide pause button until clicked

//play button
$('.play').click(function(){
	audio.play();
    $('.play').hide();
	$('.pause').show();
});

//pause button
$('.pause').click(function(){
	audio.pause();
	$('.play').show();
	$('.pause').hide();
});