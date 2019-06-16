from django.db import models

class Location(models.Model):
    location_name = models.CharField(max_length=30, unique=True)
    
    
    def __str__(self):
            return self.location_name


    def save_location(self):
        self.save()

