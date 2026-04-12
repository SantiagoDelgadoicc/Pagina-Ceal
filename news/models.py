from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200) 
    summary = models.TextField(max_length=300) 
    content = models.TextField() 
    image = models.ImageField(upload_to='news_images/') 
    date_posted = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False) 

    class Meta:
        ordering = ['-date_posted']
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def __str__(self):
        return self.title