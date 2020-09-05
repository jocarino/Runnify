from django.views.generic import TemplateView
from django.shortcuts import render
import json
from .models import Coordinates
from .openstreetmaps import main_as_function
#from django.contrib.gis.utils import GeoIP
#from django.contrib.gis.geoip2 import GeoIP2
import geocoder





'''
class HomePageView(TemplateView):
    template_name = 'home.html'
'''

Coordinates = Coordinates()
def SaveCoordinatesToDB(list_of_coordinates):
    Coordinates.coordinates = json.dumps(list_of_coordinates)
    Coordinates.save()
'''    
def get_client_ip(request):
   x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
   if x_forwarded_for:
       ip = x_forwarded_for.split(',')[0]
   else:
       ip = request.META.get('REMOTE_ADDR')
   return ip


def get_geolocation_for_ip(ip):
    url = f"http://api.ipstack.com/37.189.28.173?access_key=9a714779d3b8fbe82691763f96f27f83"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
'''
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
    geo_info = get_geolocation()
    route_request = routeRequest(geo_info, 20)
    
    route_json = main_as_function(route_request,print_delta=True)
    list_of_coordinates = route_json['0']
    
    #SaveCoordinatesToDB(list_of_coordinates)
    return render(
        request,
        'pages/home.html',
        context={'coordinates': list_of_coordinates}
    )

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'



from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_400_BAD_REQUEST

#URL /
@define_usage(returns={'url_usage': 'Dict'})
@api_view(['GET'])
@permission_classes((AllowAny,))
def api_index(requet):
    details = {}
    for item in list(globals().items()):
        if item[0][0:4] == 'api_':
            if hasattr(item[1], 'usage'):
                details[reverse(item[1].__name__)] = item[1].usage
    return Response(details)

