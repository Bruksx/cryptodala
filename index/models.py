from django.db import models

# Create your models here.

class customer(models.Model):
	email=models.CharField(max_length=50)
	phone=models.CharField(max_length=11)
	phone_code=models.CharField(max_length=4)
	password=models.CharField(max_length=200)