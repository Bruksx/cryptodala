from django.db import models

# Create your models here.

class customer(models.Model):
	email = models.CharField(max_length = 50)
	phone = models.CharField(max_length = 11)
	phone_code = models.CharField(max_length = 6)
	password = models.CharField(max_length = 200)
	firstname = models.CharField(max_length = 200, default="")
	middlename = models.CharField(max_length = 200, default="")
	lastname = models.CharField(max_length = 200, default="")
	verified = models.BooleanField(default = False)
	avatar = models.CharField(max_length=60, default="/static/index/img/img_avatar.png")
	full_phone_num = models.CharField(max_length=15, default="",)

def handle_uploaded_file(name, f, extension):
    with open("account/static/avatar/{}.{}".format(name, extension), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)