from django.shortcuts import render
from django.http import HttpResponse

def render_front_page(request):

    return render(request, 'frontpage.html')
