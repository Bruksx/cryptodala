from django.db import models
import os
import random

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR.split("\\")[0] == "C:":
	upload_site = "account/static/{}/{}.{}"
else:
	upload_site = "mysite/cryptogalaproject/account/static/{}/{}.{}"

# Create your models here.

class Customer(models.Model):
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

	

class Verification(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	doc_type = models.CharField(max_length=6)
	document = models.CharField(max_length=60)

class address(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	type = models.CharField(max_length=6)
	address = models.CharField(max_length=100, unique=True)




def handle_uploaded_file(name, f, extension):
    with open(upload_site.format("avatar", name, extension), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_verification_doc(name, f):
	print(name)
	ext = str(f).split(".")[-1]
	print(ext)
	with open(upload_site.format("verify", name, ext), 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)
	return ext

def user_package(user):
	random_variable= random.randint(1,10000)
	context={
        "random_variable": random_variable,
        "email": user.email,
        "password": user.password,
        "phone": user.phone,
        "country_code": user.phone_code,
        "firstname": user.firstname,
        "middlename": user.middlename,
        "lastname": user.lastname,
        "id": user.id,
        "avatar": user.avatar,
    }
	return context