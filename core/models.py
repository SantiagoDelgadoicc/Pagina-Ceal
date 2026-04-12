from django.db import models

class HomeFeature(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=60)
    image = models.ImageField(upload_to='home/') 

    def __str__(self):
        return self.title
    
class PendingTask(models.Model):
    task_name = models.CharField(max_length=200, verbose_name="Título del recordatorio")
    description = models.CharField(max_length=255, blank=True, verbose_name="Nota corta")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name