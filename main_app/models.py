from django.db import models
from django.urls import reverse

# Create your models here.
class WishList(models.Model):
    item = models.TextField()
    
    def get_absolute_url(self):
        return reverse('home')