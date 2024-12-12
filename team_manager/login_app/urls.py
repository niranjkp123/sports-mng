from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns=[
    path('login/',views.log_in, name='login'),
    path('index/',views.home, name='index'),
    path('add/', views.add_player, name='add'),
    path('players/', views.players, name='player'),
    path('add/', views.add_player, name='add_player'), 
    path('edit/<int:player_id>/', views.edit_player, name='edit_player'),  # Edit player URL
    path('delete/<int:player_id>/', views.delete_player, name='delete_player'),  # Delete player URL
    path('players/', views.players, name='players'), 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)