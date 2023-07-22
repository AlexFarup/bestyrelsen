from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    return render(request, 'index.html')

def members(request):

    return render(request, './content/members.html')

def events(request):

    return render(request, './content/events.html')

def leaderboard(request):

    return render(request, './content/leaderboard.html')

def login(request):

    return render(request, './login/login.html')

def register(request):

    return render(request, './login/register.html')
