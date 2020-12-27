// shuffle button
$('.shuffle').click(function() {
	$(this).toggleClass('clicked');
});

//music player settings (not needed any more)

// play / pause button
$('.pause').hide(); //hide pause button until clicked

//play button
$('.play').click(function() {
	$('.play').hide();
	$('.pause').show();
});

//pause button
$('.pause').click(function() {
	$('.play').show();
	$('.pause').hide();
});


//Show and hide the queue
$('.current-queue').hide();
var showed = false
$('.option').click(function() {
	if (!showed) {
		$('#player').css('height', '250px');
		$('.info').css('bottom', '130px');
		$('.current-queue').show();
		showed = true
	} else {
		$('#player').css('height', '120px');
		$('.info').css('bottom', '0');
		$('.current-queue').hide();
		showed = false
	};
});


// Display song when click
$('#queue-list').click(function() {
	$('.song-name span').text($('#get-track-name').text());
	$('.artist-name span').text($('#get-artist-name').text());
});

function addSongToQueue(id) {
	console.log('called with track id:', id)
	$.ajax({
		type: 'POST',
		url: queueAddUrl,
		headers: {'X-CSRFToken': CSRF_TOKEN},
		contentType: 'application/json',
		data: JSON.stringify({'id': id}),
		dataType: 'json',
		success: function(data) {
			console.log('done adding to queue in db, reload!')
			drawQueue(data.queue)
		}
	});
	return false;
}

// $('#add-button').click();
function initPlayer() {
	$.getJSON(queueGetUrl, function(data) {
			console.log(data)
			drawQueue(data.queue)
			drawPlayer(data.queue[data.current_index])
		}
	)
}

function drawQueue(queue) {
	const table = queue.map(song => `<ul class="queue-list">
	<li>${song.index}</li>
	<li class="get-track-name">${song.title}</li>
	<li>${song.duration}</li>
	<li class="get-artist-name">${song.artist}</li>
	</ul>`).join('')
	$('.current-queue').html(table)
}

function drawPlayer(song) {
	let $player = $('.currently-playing')
	$player.find('.song-name span').html(song.title)
	$player.find('.artist-name span').html(song.artist)
}


$(document).ready(function() {
	initPlayer()
})
