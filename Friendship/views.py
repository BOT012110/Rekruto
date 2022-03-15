from email import message
from unicodedata import name
from django.shortcuts import render, get_object_or_404
from .models import StartFriendShip

def site(request, name, message): 
    return render(request, 'Friendship/nice.html', {'name': name, 'message': message})

# Create your views here.
