# teams/admin.py

from django.contrib import admin
from .models import Team, Match
from .models import Player

admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Player)