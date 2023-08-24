from django.shortcuts import render

# Create your views here.


def chapters(request):
    context = {
        "pname":chapters,
    }

    return render(request, "chapters/index.html", context)