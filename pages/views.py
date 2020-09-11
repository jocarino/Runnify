from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import json
from .models import Coordinates, RouteRequest
from .openstreetmaps import main_as_function
#from django.contrib.gis.utils import GeoIP
#from django.contrib.gis.geoip2 import GeoIP2
import geocoder
from django.forms import modelform_factory
from .forms import RouteRequestForm
from django.conf import settings
from django.utils.http import is_safe_url
from django.http import HttpResponse, Http404, JsonResponse




ALLOWED_HOSTS = settings.ALLOWED_HOSTS


Coordinates = Coordinates()
def SaveCoordinatesToDB(list_of_coordinates):
    Coordinates.coordinates = json.dumps(list_of_coordinates)
    Coordinates.save()


#object for generation route
class routeRequestClass(object):
    def __init__(self, coords, original_run):
        self.lat = coords[0]
        self.lng = coords[1]
        self.original_run = original_run



def HomePageView(request):
    form = RouteRequestForm()
    return render(
        request,
        'pages/home.html',
        context={},
        status=200,
    )

def get_route(request):
    form = RouteRequestForm(request.POST or None)
    next_url = request.POST.get("route") or None

    if form.is_valid():
        obj = form.save(commit=False)
        
        #get the info from the frontend
        running_distance = form.cleaned_data['running_distance']
        user_location_info = form.cleaned_data['user_location']
        obj.user_location = user_location_info
                
        #generate the route
        user_location = user_location_info.split(',')
        route_request = routeRequestClass(user_location, running_distance)
        route_json = main_as_function(route_request,print_delta=True)
        list_of_coordinates = route_json['0']

        # Save form object
        #obj.save()

        route = RouteRequest(running_distance= running_distance,
                             user_location= str(user_location_info))

        if request.is_ajax():
            return JsonResponse({"coordinates": list_of_coordinates}, status=201) # 201 == created items
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
    return render(
        request,
        'pages/home.html',
        context={'form':form,
                'coordinates':list_of_coordinates}
    )

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

'''
def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

class SignUpView(CreateView):
    template_name = 'core/signup.html'
    form_class = UserCreationForm
'''




