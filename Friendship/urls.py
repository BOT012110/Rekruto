from django.urls import URLPattern, path
from . import views
from .models import StartFriendShip

urlpatterns = [
    path('name=<name>&message=<message>', views.site, name="site"),
]