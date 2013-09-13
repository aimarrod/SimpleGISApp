from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponse
from forms import GPXUploadForm
from utils import parse_gpx
from simplegisapp.models import Route
import json

def route(request):
    if request.method == 'POST':
        form = GPXUploadForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            f, name= data['file'], data['name']
            route = parse_gpx(f=f, name=name)
    else:
        form = GPXUploadForm()
    routes = Route.objects.all()
    dict = {'form':form,'routes':routes}
    dict.update(csrf(request))
    return render_to_response('routepage.html', dict)

def routeJSON(request, pk):
    route = Route.objects.get(pk=pk)
    if route is not None:
        rt = {'name':route.name, 'dist':route.length(), 'nearest':route.nearest().name}
        rt["geojson"] = json.loads(route.geoJSON())
        return HttpResponse(json.dumps(rt), content_type="application/json")
    return HttpResponse("", content_type="application/json")
    