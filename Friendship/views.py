from email import message
from unicodedata import name
from django.shortcuts import render
from .models import StartFriendShip

def site(request):
    f_text = StartFriendShip.objects.all()
    return render(request, 'Friendship/nice.html', {'start_f': f_text})  

# Create your views here.
