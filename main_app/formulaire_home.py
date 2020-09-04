from django import forms
from .models import Pattern
class form_patterns(forms.Form):


    def __init__(self, *args, **kwargs):
        super(form_patterns, self).__init__(*args, **kwargs)
        self.fields["year"] = forms.CharField(label='Année', max_length=100)
        choices = [(p.name, p.name) for p in Pattern.objects.all()]
        self.fields["choice"] = forms.MultipleChoiceField(label="Filtres",widget=forms.CheckboxSelectMultiple, choices=choices)
