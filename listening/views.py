from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import InQueue


@login_required
def listening_queue(request):
    """Render user's listening queue"""
    queue = InQueue.objects.filter(user=request.user).order_by('queue_index')
    # TODO: link to template
