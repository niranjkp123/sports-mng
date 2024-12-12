# teams/forms.py

from django import forms
from .models import Match
from .models import Match, Team
# class MatchScheduleForm(forms.ModelForm):
#     class Meta:
#         model = Match
#         fields = ['team1', 'team2', 'match_date', 'venue']

#     def clean(self):
#         cleaned_data = super().clean()
#         team1 = cleaned_data.get("team1")
#         team2 = cleaned_data.get("team2")

#         if team1 == team2:
#             raise forms.ValidationError("A team cannot play against itself.")
        
#         return cleaned_data
class MatchScheduleForm(forms.ModelForm):
    team1 = forms.ModelChoiceField(queryset=Team.objects.all(), label="Select Team 1")
    team2 = forms.ModelChoiceField(queryset=Team.objects.all(), label="Select Team 2")

    class Meta:
        model = Match
        fields = ['team1', 'team2', 'date', 'location']

