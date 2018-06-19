from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'prsm-site/index.html')

def aboutView(request):
    return render(request, 'prsm-site/about.html')

def workshopsView(request):
    return render(request, 'prsm-site/workshops.html')

def calendarView(request):
    return render(request, 'prsm-site/calendar.html')

def multimediaView(request):
    return render(request, 'prsm-site/multimedia.html')


