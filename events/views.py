from django.shortcuts import render, get_object_or_404
from .models import Events
# Create your views here.

def events(request):
    events = Events.objects.all()
    context = {
        'events' : events,
        'pname' : 'session',
    }
    return render(request, 'events/events.html', context)


