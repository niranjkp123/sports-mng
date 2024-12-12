from django import forms
from teams.models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'  # Include all fields except owner
