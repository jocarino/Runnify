from django.urls import path
from django.conf.urls import url


from . import views

urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('route', views.get_route, name='route'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    #url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    #url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
]
