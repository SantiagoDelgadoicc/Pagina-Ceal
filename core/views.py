from django.shortcuts import render
from calendar.models import CalendarEvent
from news.models import News
from .models import HomeFeature , PendingTask

def home(request):
    reminders = PendingTask.objects.all().order_by('-created_at')[:3]
    feature = HomeFeature.objects.first()
    latest_news = News.objects.all().order_by('-date_posted')[:4]

    return render(request, 'core/index.html', {
        'reminders': reminders,
        'feature': feature,
        'latest_news': latest_news
    })