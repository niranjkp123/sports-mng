from django.contrib import admin
from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="home"),
    path('team/', views.team_view, name='team'),
    path('team/player_update/<int:player_id>/', views.player_update_view, name='player_update'),
    # path('login', views.loginn, name="login"),
    # path('register', views.register, name="register"),
    path('schedule/', views.schedule_match, name='schedule_match'),
    path('match_list/', views.match_list, name='match_list'),
    path('match_success/<int:match_id>/', match_success, name='match_success'),  # Add this line
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
