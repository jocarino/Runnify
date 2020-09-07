from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
import json
from .models import Coordinates, RouteRequest
from .openstreetmaps import main_as_function
#from django.contrib.gis.utils import GeoIP
#from django.contrib.gis.geoip2 import GeoIP2
import geocoder
from django.forms import modelform_factory
from .forms import RouteRequestForm


Coordinates = Coordinates()
def SaveCoordinatesToDB(list_of_coordinates):
    Coordinates.coordinates = json.dumps(list_of_coordinates)
    Coordinates.save()

def get_geolocation():
    '''
    returns tuple (latitude, longitude)
    '''
    g = geocoder.ip('me')
    return (g.lat, g.lng)

class routeRequest(object):
    def __init__(self, coords, original_run):
        self.lat = coords[0]
        self.lng = coords[1]
        self.original_run = original_run



def HomePageView(request):
    #g = GeoIP() 
    #lat,lng = g.lat_lon(user_ip)
    '''
    geo_info = get_geolocation()
    route_request = routeRequest(geo_info, 20)
    #SaveCoordinatesToDB(list_of_coordinates)
    list_of_coordinates = []
    

    if request.method == "POST":
        coordinate_request = CoordinateRequest(request.POST, user_coordinates = "[10,4]")
        if coordinate_request.is_valid():
            coordinate_request.save()
            route_json = main_as_function(route_request,print_delta=True)
            list_of_coordinates = route_json['0']
    else:
        coordinate_request = CoordinateRequest()
    
    return render(
        request,
        'pages/home.html',
        context={'coordinates': list_of_coordinates,
                 'coordinate_request': coordinate_request
        }
    )
    '''
    form = RouteRequestForm()
    list_of_coordinates = [[51.509, -0.08], [51.503, -0.06], [51.51, -0.047]]
    return render(
        request,
        'pages/home.html',
        context={'form':form,
                 #'coordinates':list_of_coordinates
                 }
    )
    
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

def get_route(request):
    form = RouteRequestForm(request.POST)
    #get user location
    user_location_info = get_geolocation()
    print("#####################################")

    if form.is_valid():
        running_distance = form.cleaned_data['running_distance']
        user_location_info = form.cleaned_data['user_location']
        user_location = user_location_info.split(',')
        #print(user_location)
        route = RouteRequest(running_distance= running_distance,
                             user_location= str(user_location_info))
        route.save()
        
        #generate the route
        #print(user_location)
        route_request = routeRequest(user_location, running_distance)
        route_json = main_as_function(route_request,print_delta=True)
        list_of_coordinates = route_json['0']
    return render(
        request,
        'pages/home.html',
        context={'form':form,
                'coordinates':list_of_coordinates}
    )

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'




