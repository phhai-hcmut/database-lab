// shuffle button
$('.shuffle').click(function(){
  $(this).toggleClass('clicked');
});

//music player settings (not needed any more)

let audio = new Audio('');
// play / pause button
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


//Show and hide the queue
$('.current-queue').hide();
var showed = false
$('.option').click(function(){
    if(!showed) {
        $('#player').css('height','250px');
        $('.info').css('bottom','130px');
        $('.current-queue').show();
        showed = true
    } else {
        $('#player').css('height','120px');
        $('.info').css('bottom','0');
        $('.current-queue').hide();
        showed = false
    };
});


// Display song when click
$('#queue-list').click(function(){
    $('.song-name span').text($('#get-track-name').text());
    $('.artist-name span').text($('#get-artist-name').text());
});


