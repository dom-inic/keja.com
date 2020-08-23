from django.db import models
from django.utils import timezone

class MyKeja(models.Model):
    property_name = models.CharField(max_length=200, unique=True, )
    property_image = models.ImageField(blank=True)
    description = models.TextField(max_length=3000)
    location = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    email_address = models.EmailField()
    more_property_images= models.ImageField(blank=True)
    property_specs = models.CharField(max_length=300)
    published_date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "mykejas"

    def __str__(self):
        return self.property_name
    


