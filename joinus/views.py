from django.shortcuts import render

# Create your views here.


def joinus(request):
    context={
        "pname":"join-us",
    }
    return render(request, "joinus/joinus.html", context)