from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render, redirect

from django.http import HttpResponse
from services.models import Event, Ticket, volunteer # Assuming you have an Event and Ticket model

def index(reqeust):
    return render(reqeust,'index.html')

def register_event(request):
    if request.method == 'POST':
        name = request.POST['name']
        date = request.POST['date']
        description = request.POST['description']

        # Save the event to the database
        Event.objects.create(name=name, date=date, description=description)

        return redirect('/calendar/')  # Redirect after saving
    
    return render(request, 'register_event.html')

def event_calendar(request):
    # You may want to pass actual events data here
    events = Event.objects.all()
    return render(request, 'event_calendar.html', {'events': events})

def events_list(request):
    # You might want to show all events or a specific list
    events = Event.objects.all()
    return render(request, 'events_list.html', {'events': events})

def home(request):
    return render(request, 'home.html')

def register_success(request):
    return render(request, 'register_success.html')

def register(request):
    return render(request, 'register.html')

def schedule(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'events_list.html', {'events': events})
    # return render(request, 'events_list.html')

def ticket_booking_success(request,name):
    event_data = Ticket.objects.get(name=name)

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
        
    event = Event.objects.all()
    data ={
        'event':event,
    }
    return render(request, 'ticket_booking.html',data)

def volunteer_recruitment(request):
    event = Event.objects.all()
    vdata = volunteer.objects.all()
    data ={
        'event':event,
        "volunteers":vdata,
    }
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            event1 = request.POST.get('event')
            print(name,event1,"thedafata======================================")
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
