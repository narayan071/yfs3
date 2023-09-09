from django.shortcuts import render
from django.http import HttpResponse
from .forms import CarbonFootprintForm

def calculate_carbon_footprint(request):
    if request.method == "POST":
        form = CarbonFootprintForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            motorcycle = data.get("motorcycle", False)
            car = data.get("car", False)
            bus = data.get("bus", False)
            train = data.get("train", False)
            plane = data.get("plane", False)
            ship = data.get("ship", False)
            q_motorcycle = data.get("q_motorcycle", 0)
            q_car = data.get("q_car", 0)
            q_bus = data.get("q_bus", 0)
            q_train = data.get("q_train", 0)
            q_plane = data.get("q_plane", 0)
            q_ship = data.get("q_ship", 0)
            persons_motorcycle = data.get("persons_motorcycle", 0)
            persons_car = data.get("persons_car", 0)

            pp = q_motorcycle * (0.021 / persons_motorcycle) if motorcycle else 0
            oo = q_car * (0.181 / persons_car) if car else 0
            ii = q_bus * 0.103 if bus else 0
            uu = q_train * 0.037 if train else 0
            yy = q_plane * 226.796 if plane else 0
            tt = q_ship * 0.037 if ship else 0

            total_carbon_footprint = pp + oo + ii + uu + yy + tt
            total_carbon_footprint = round(total_carbon_footprint,2)

            context = {
                "carbon_footprint": total_carbon_footprint,
                "pname":'cfpresult',
            }
            return render(request, "carbonfp/result.html", context)
    else:
        form = CarbonFootprintForm()

    context = {
        "form": form,
        'pname':"calculator",
    }
    return render(request, "carbonfp/calculator.html", context)
