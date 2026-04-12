from django.db import models

class AcademicResource(models.Model):
    name = models.CharField(max_length=100, default="Google Drive Recursos")
    drive_url = models.URLField(help_text="Pega aquí el link compartido de Google Drive")

    def __str__(self):
        return self.name