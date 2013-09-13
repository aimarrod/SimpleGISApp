from django import forms
from simplegisapp.models import Route

class GPXUploadForm(forms.Form):
    name = forms.CharField(max_length=255)
    file = forms.FileField()
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if Route.objects.filter(name=name).count():
            raise forms.ValidationError("A route with that name already exists")
        return name
    
    def clean_file(self):
        f = self.cleaned_data['file']
        extension = f.name.split('.')[-1]
        if extension not in ['gpx']:
            raise forms.ValidationError("Format not supported")
        return f