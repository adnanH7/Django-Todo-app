from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)

    due_date = models.DateField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name