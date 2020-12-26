import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from music.models import Recording, Track

from .models import InQueue, UserQueue


def serialize_queue(queue):
    return [
        {
            'index': song.queue_index,
            'title': song.recording.name,
            'artist': ", ".join(artist.name for artist in song.recording.artist_credits.all()),
            'duration': str(song.recording.duration),
        }
        for song in queue
    ]


@login_required
def list_queue(request):
    """Render user's listening queue"""
    if not request.is_ajax():
        return

    if request.method != 'GET':
        return HttpResponse(status=405)

    queue = InQueue.objects.filter(user=request.user).order_by('queue_index')
    current_index = UserQueue.objects.get(user=request.user).recording.queue_index
    data = {'current_index': current_index, 'queue': serialize_queue(queue)}
    return JsonResponse(data)


@login_required
def add_song_to_queue(request):
    """Add new recording to queue"""
    if not request.is_ajax():
        return

    if request.method != 'POST':
        return HttpResponse(status=405)

    track_id = json.loads(request.body)['id']
    recording = Track.objects.get(pk=track_id).recording
    queue = InQueue.objects.filter(user=request.user).order_by('queue_index')
    if queue:
        # The user has queued some songs
        last_queued = queue.last()
        new_index = last_queued.queue_index + 1
        InQueue.objects.create(
            user=request.user, recording=recording, queue_index=new_index
        )
    else:
        InQueue.objects.create(user=request.user, recording=recording, queue_index=1)

    queue = InQueue.objects.filter(user=request.user).order_by('queue_index')
    return JsonResponse({'queue': serialize_queue(queue)})
