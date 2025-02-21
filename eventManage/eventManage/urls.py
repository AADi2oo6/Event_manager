"""
URL configuration for eventManage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from eventManage import views


urlpatterns = [
     path('admin/', admin.site.urls),
    path('', views.ulogin,name = "ulogin"),  # Ensure this is the root URL
    path('home/', views.index,name = "home"),  # Ensure this is the root URL
    # path("index/",views.index),
    path('calendar/', views.event_calendar, name='event_calendar'),
    path('list/', views.events_list, name='events_list'),
    path('register_event/', views.register_event, name='register_event'),
    path('register_success/', views.register_success, name='register_success'),
    path('register/', views.register, name='register'),
    path('schedule/', views.schedule, name='schedule'),
    path('ticket_booking_success/<name>', views.ticket_booking_success, name='ticket_booking_success'),
    path('ticket_booking/', views.ticket_booking, name='ticket_booking'),
    path('volunteer_recruitment/', views.volunteer_recruitment, name='volunteer_recruitment'),
    path('volunteer_register_success/', views.volunteer_register_success),
]