from django.db import models
import os 

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

def handle_uploaded_file(name, f, extension):
    with open(upload_site.format("avatar", name, extension), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_verification_doc(name, f):
	ext = str(f).split(".")[-1]
	with open(upload_site.format("verify", name, ext), 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)