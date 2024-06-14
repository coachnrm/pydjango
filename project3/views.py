from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def date(request, day, month, year):
    return HttpResponse(f'Date: {day}-{month}-{year}')

def show_title(request, title):
    return HttpResponse(f'Title: {title}')

def maps(request):
    type = request.GET.get('type', 'hybrid')
    lat = request.GET.get('lat', '13.7245601')
    lon = request.GET.get('lon', '100.4930241')
    zoom = request.GET.get('z', 11)

    return HttpResponse(f"Map type: {type} <br> \
                        Location: {lat},{lon}<br> \
                        Zoom: {zoom}")

def filter_custom(request):
    now = datetime.today()
    return render(request, 'filter-custom.html', {'now':now})