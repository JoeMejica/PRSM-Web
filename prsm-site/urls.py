from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.aboutView, name='about'),
    path('workshops', views.workshopsView, name='workshops'),
    path('calendar', views.calendarView, name='calendar'),
    path('multimedia', views.multimediaView, name='multimedia')

]
