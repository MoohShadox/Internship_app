from django import forms
from .models import Pattern
class form_patterns(forms.Form):
    year = forms.CharField(label='Année', max_length=100)
    choices = [(p.name,p.name) for  p in Pattern.objects.all()]
    choice = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=choices)

    def get_choice(self):
        choices = [(p.name, p.name) for p in Pattern.objects.all()]
        choice = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=choices)
        self.choice = choice
        return self.choice

