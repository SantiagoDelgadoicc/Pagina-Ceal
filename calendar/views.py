import json
from django.shortcuts import render, redirect, get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder
from .models import CalendarEvent

def calendar_index(request):
    events_queryset = CalendarEvent.objects.filter(is_approved=True).values(
        'id', 'title', 'description', 'date', 'time', 'category', 'is_modified'
    )
    
    events_json = json.dumps(list(events_queryset), cls=DjangoJSONEncoder)
    
    return render(request, 'calendar/index.html', {
        'events_json': events_json
    })

def create_event(request):
    if request.method == 'POST':
        CalendarEvent.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            date=request.POST.get('date'),
            time=request.POST.get('time') or None,
            category=request.POST.get('category'),
            is_approved=False 
        )
    return redirect('calendar_index')

def update_event(request, event_id):
    event = get_object_or_404(CalendarEvent, id=event_id)
    
    if request.method == 'POST':
        event.title = request.POST.get('title')
        event.category = request.POST.get('category')
        event.date = request.POST.get('date')
        event.time = request.POST.get('time') or None
        event.description = request.POST.get('description')
        event.is_approved = False 
        event.is_modified = True
        event.save()
        
    return redirect('calendar_index')