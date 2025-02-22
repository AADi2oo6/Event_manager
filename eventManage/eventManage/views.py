# from django.http import HttpResponse , HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.mail import send_mail

from userlongin.models import login
from services.models import Event, Ticket, volunteer # Assuming you have an Event and Ticket model



user = "admin"
def index(reqeust):
    return render(reqeust,'index.html')

def ulogin(request):
    udata = login.objects.all()
    users = {i.uname: i.password for i in udata}
    data = {"message": "", "message_type": ""}

    if request.method == 'POST':
        if 'signup' in request.POST:
            uname = request.POST.get('uname')
            email = request.POST.get('email')
            pwd = request.POST.get('pswd')

            if uname in users:
                data['message'] = "User already exists!"
                data['message_type'] = "warning"
            else:
                login.objects.create(uname=uname, email=email, password=pwd)
                data['message'] = "User registered successfully!"
                data['message_type'] = "success"

        elif 'login' in request.POST:
            uname = request.POST.get('uname')
            pwd = request.POST.get('pswd')

            if uname in users and users[uname] == pwd:
                global user
                user = uname
                return redirect('/home/')  # Redirect after successful login
            else:
                data['message'] = "Invalid username or password!"
                data['message_type'] = "danger"

    return render(request, 'login.html', data)
def register_event(request):
    if request.method == 'POST':
        name = request.POST['name']
        date = request.POST['date']
        description = request.POST['description']

        # Save the event to the database
        Event.objects.create(name=name,host = user, date=date, description=description)

        return redirect('/calendar/')  # Redirect after saving
    
    return render(request, 'register_event.html')

def event_calendar(request):
    # You may want to pass actual events data here

    events = Event.objects.filter(host__in=[user, 'admin']).order_by('date')

    return render(request, 'event_calendar.html', {'events': events})

def events_list(request):
    # You might want to show all events or a specific list
    events = Event.objects.all()
    return render(request, 'events_list.html', {'events': events})


def register_success(request):
    return render(request, 'register_success.html')

def register(request):
    return render(request, 'register.html')

def schedule(request):
    current_date = timezone.now().date()
    events = Event.objects.filter(date__gt=current_date, host__in=[user, 'admin']).order_by('date')
    return render(request, 'events_list.html', {'events': events})

def ticket_booking_success(request,name):
    try:
        event_data = Ticket.objects.filter(name=name).first()
        send_mail(
            f"Your Ticket For the Event {event_data.event}",
            f"Dear {event_data.name},\n\n"
            f"Thank you for booking a ticket for the event '{event_data.event}'. Here are your ticket details:\n\n"
            f"Event Name: {event_data.event}\n"
            f"Name: {event_data.name}\n"
            f"Email: {event_data.email}\n"
            f"Phone: {event_data.phone}\n\n"
            "We look forward to seeing you at the event!\n\n"
            "Best regards,\n"
            "Event Management Team",
            "adi20062024@gmail.com",
            [event_data.email],
            fail_silently=False,
        )
    except Exception as e:
        return HttpResponse(f"Error occurred: {e}")

    data = {
        "event":event_data,

    }
    return render(request, 'ticket_booking_success.html',data)

def ticket_booking(request):
    if request.method == 'POST':
        try:
            ticket_count = int(request.POST.get('tickets', 0))
            for i in range(ticket_count):
                name = request.POST.get(f'name{i}')
                email = request.POST.get(f'email{i}')
                phone = request.POST.get(f'phone{i}')
                event = request.POST.get("event")

                # Save ticket details in the database (using the Ticket model)
                Ticket.objects.create(name=name, event = event,email=email, phone=phone)

            # Redirect to the success page
            return redirect(f'/ticket_booking_success/{name}')
        except Exception as e:
            return HttpResponse(f"Error occurred: {e}")
        
    event = Event.objects.filter(host = 'admin')
    data ={
        'event':event,
    }
    return render(request, 'ticket_booking.html',data)

def volunteer_recruitment(request):
    event = Event.objects.filter(host='admin')
    vdata = volunteer.objects.all()
    data ={
        'event':event,
        "volunteers":vdata,
    }
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            event1 = request.POST.get('event')
            # Save volunteer details in the database (using the Volunteer model)
            en = volunteer(name=name, event=event1)
            en.save()
            # Redirect to the success page
            return redirect('/volunteer_register_success/')
            
            # return render(request, 'volunteer_register_success.html')
        except Exception as e:
            return HttpResponse(f"Error occurred: {e}")
    return render(request, 'volunteer_recruitment.html',data)

def volunteer_register_success(request):
    return render(request, 'volunteer_register_success.html')
