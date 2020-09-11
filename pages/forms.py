from django import forms
from .models import RouteRequest


class RouteRequestForm(forms.Form):
    class Meta:
        model = RouteRequest
        fields = ['running_distance', 'user_location']

    def clean_running_distance(self):
        running_distance = self.cleaned_data.get("running_distance")
        if running_distance <= 0:
            raise forms.ValidationError("Running distance needs to be greater than zero.")
        return content

    
