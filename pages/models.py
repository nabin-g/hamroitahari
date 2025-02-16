from django.db import models
from datetime import datetime
# Create your models here.
class HomePage(models.Model):
    sliding_image = models.ImageField(upload_to ='photos/%Y/%m/%d/')
    title = models.CharField(max_length =200)
    description = models.TextField(blank=True)
    home_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
