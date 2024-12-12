from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import MatchScheduleForm
from .models import Match
from .models import Player



def index(request):
    players = Player.objects.all()  # Query all players, or adjust as needed
    return render(request, 'teams/index.html', {'players': players})
    # return render(request, 'teams/index.html')
def team(request):
    return render(request,'teams/team.html')

def team_view(request):
    players = Player.objects.all()
    return render(request, 'teams/team.html', {'players': players})

def player_update_view(request, player_id):
    player = get_object_or_404(Player, id=player_id)

    if request.method == 'POST' and 'delete' in request.POST:
        player.delete()
        return redirect('team')  # Redirect back to the team page after deletion

    return render(request, 'teams/player_update.html', {'player': player})



def schedule_match(request):
    if request.method == "POST":
        form = MatchScheduleForm(request.POST)
        if form.is_valid():
            # Save the form to create a Match instance
            match = form.save()
            # Redirect to match_success page with the match ID
            return redirect('match_list')
        else:
            messages.error(request, "There was an error with the form.")
    else:
        form = MatchScheduleForm()
    return render(request, 'teams/schedule_match.html', {'form': form})


def match_list(request):
    matches = Match.objects.all()
    return render(request, 'teams/match_list.html', {'matches': matches})
   
def match_success(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    return render(request, 'teams/match_success.html', {'match': match})
