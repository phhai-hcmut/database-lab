$('.shuffle').click(function(){
  $(this).toggleClass('clicked');
});

//music player settings

let audio = new Audio('./1-Phut-Andiez.mp3');

$('.pause').hide(); //hide pause button until clicked

//play button
$('.play').click(function(){
	audio.play();
    //$('.total').innerHTML = Math.floor(this.duration);
	// document.getElementById("myText").innerHTML = audio.duration;
    $('.play').hide();
	$('.pause').show();
});

//pause button
$('.pause').click(function(){
	audio.pause();
	$('.play').show();
	$('.pause').hide();
});

// function getDuration(src, cb) {
//     var audio = new Audio();
//     $(audio).on("loadedmetadata", function(){
//         cb(audio.duration);
//     });
//     audio.src = src;
// }

// getDuration('./1-Phut-Andiez.mp3', function(length) {
//     document.getElementById("time--total").textContent = length;
// });
$('total').innerHTML = Math.floor(this.currentTime) + ' / ' + Math.floor(this.duration);