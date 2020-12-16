

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

function addItem(){
	var ul = document.getElementById("dynamic-list");
	var candidate = document.getElementById("candidate");
	var li = document.createElement("li");
	li.setAttribute('id',candidate.value);
	li.appendChild(document.createTextNode(candidate.value));
	ul.appendChild(li);
}

function removeItem(){
	var ul = document.getElementById("dynamic-list");
	var candidate = document.getElementById("candidate");
	var item = document.getElementById(candidate.value);
	ul.removeChild(item);
}
