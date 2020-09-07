from django import forms

class RouteRequestForm(forms.Form):
    running_distance = forms.FloatField(max_value=100)
    user_location = forms.CharField(max_length=100)