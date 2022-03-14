from django.shortcuts import render

def site(request):
    return render(request, 'Friendship/nice.html', {})  

# Create your views here.
