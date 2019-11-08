from django.db import models
from django.contrib.auth.models import User


class urldetails(models.Model):
    name 		= models.CharField(max_length=100, null=True)
    full_url 	= models.URLField()
    key 		= models.CharField(max_length=100, unique=True, null=True)
    short_url 	= models.CharField(max_length=100, unique=True, null=True)
    
    user 		= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    app_status 	= models.BooleanField(default=True)
    
    created_on 	= models.DateTimeField(auto_now_add=True, null=True)
    updated_on 	= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    