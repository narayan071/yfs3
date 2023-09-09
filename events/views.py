from django.shortcuts import render, get_object_or_404
from .models import LiveEvents,CorporateWorkshops,PastEvents
# Create your views here.

def live_events(request):
    events = LiveEvents.objects.all()
    context = {
        'events' : events,
    }
    return render(request, 'events/events.html', context)

def corporate_workshops(request):
    events = CorporateWorkshops.objects.all()
    context = {
        'events' : events,
    }
    return render(request, 'events/events.html', context)

def past_events(request):
    events = PastEvents.objects.all()
    context = {
        'events' : events,
    }
    return render(request, 'events/events.html', context)


