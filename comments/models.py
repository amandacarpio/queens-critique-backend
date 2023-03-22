from django.db import models
# from django.contrib.auth.models import User
# from django.db.models import Avg

# Create your models here.

class Comment(models.Model):
    
    name = models.CharField(
        max_length=40,
        null=False, 
        blank=False,
        )
    city = models.CharField(
        max_length=15,
        default="none",
        null=False,
        blank=False,
    )
    rating = models.IntegerField(
        null=False,
        blank=False,
        default=1,
    )
    review = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        ) 
    
    
    