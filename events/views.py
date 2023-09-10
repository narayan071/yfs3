from django.shortcuts import render, get_object_or_404
from .models import Events
# Create your views here.

def events(request):
    live_events = Events.objects.filter(event_type='Live events')
    corporate_workshops = Events.objects.filter(event_type='Corporate workshops')
    past_events = Events.objects.filter(event_type='Past events')
    context = {
        'live_events' : live_events,
        'corporate_workshops' :corporate_workshops,
        'past_events' :past_events,
        'pname' : 'session',
    }
    print(events)
    return render(request, 'events/events.html', context)


