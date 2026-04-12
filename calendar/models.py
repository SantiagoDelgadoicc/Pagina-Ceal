from django.db import models

class CalendarEvent(models.Model):
    CATEGORY_CHOICES = [
        ('EVALUATION', 'Evaluation'),
        ('SOCIAL', 'Social Event'),
        ('WORKSHOP', 'Workshop'),
    ]

    title = models.CharField(max_length=15)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    is_approved = models.BooleanField(default=False)
    is_modified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"