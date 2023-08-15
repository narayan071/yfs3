from django.shortcuts import render, get_object_or_404

# Create your views here.

def events(request):
    context = {
        'pname' : 'events',
    }
    return render(request, 'events/events.html', context)
