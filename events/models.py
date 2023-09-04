from django.db import models

# Create your models here.

class Events(models.model):
    EVENT_TYPE = [
        ('Live events', 'Live events'),
        ('Corporate workshops', 'Corporate workshops'),
        ('Past events', 'Past events'),
    ]
    
    name = models.CharField(max_length=200, primary_key=True)
    event_type = models.CharField(max_length=50, choices = EVENT_TYPE, null=False, default = None)
    description = models.TextField(max_length=800, default = None)
    event_url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True) 
    created_at = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.name   #used to display only title of the event
    
    
    