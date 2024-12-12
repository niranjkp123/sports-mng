from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from teams.views import *
from .forms import *


# Create your views here.

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('index')  # Redirect to the home page
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request,'home.html')

def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            form.save()  # Now save it to the database
            return redirect('player') # Redirect to car list after saving
    else:
        form = PlayerForm()
    return render(request, 'add.html', {'form': form})

def players(request):
    players = Player.objects.all()  # Fetch players (not cars) from the database
    return render(request, 'player.html', {'players': players})




def edit_player(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            messages.success(request, "Player updated successfully!")
            return redirect('players')
    else:
        form = PlayerForm(instance=player)
    
    return render(request, 'player.html', {'form': form, 'player': player})
# Delete player view
def delete_player(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    if request.method == 'POST':  # Confirm delete on POST request
        player.delete()  # Delete the player
        messages.success(request, "Player deleted successfully.")
        return redirect('players')  # Ensure this is correct
    return render(request, 'delete_player.html', {'player': player})

