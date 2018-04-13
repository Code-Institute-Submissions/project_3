from django.shortcuts import render, redirect
from .models import Event
from .forms import NewEventForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def get_events_index(request):
    events = Event.objects.all()
    return render(request, 'locate_music/events.html', {'events': events})

def new_event(request):
    if request.method == "POST":
        form = NewEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.currency.upper()
            form.save()
            messages.success(request, "Successfully Posted!")
            return redirect('events')
    else:
        form = NewEventForm()
    return render(request, 'locate_music/new_event.html', {'form': form})