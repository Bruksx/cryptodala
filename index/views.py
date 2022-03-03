from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import customer
from django.views.decorators.csrf import csrf_exempt
import random

# Create your views here.
def index(request):
     random_variable= random.randint(1,10000)
     context= {
          "random_variable": random_variable,
     }
     return render(request, "index/index.html", context)

@csrf_exempt
def register(request):
     cd= request.POST
     print(cd)
     
     if cd.get("contact_type")== "mobile":
          print["mobile"]

          full_phone=  cd["country_code"] + cd["mobile"]
          full_phone =  "".join(full_phone.split())
          print(full_phone)

          #check if user already exists
          already_exists= customer.objects.filter(phone=cd["mobile"])
          if already_exists:
               data ={
                    "status": "error",
                    "message": "A profile has already been opened with this phone number"
               }
          #check if phone number is valid
          elif full_phone.isdigit() == False:
                data ={
                    "status": "error",
                    "message": "Invalid phone number"
               }

          else:
               data={
                    "status":"success",
                    "message":"Profile created successfully"
               }
               new_profile = customer(
                    phone=cd["mobile"],
                    phone_code= cd["country_code"],
                    password = cd["password"]
               )
               new_profile.save()
          
          return JsonResponse(data)

     
     if cd.get("contact_type")== "email":
          already_exists= customer.objects.filter(email=cd["email"])
          if already_exists:
               data ={
                    "status": "error",
                    "message": "A profile has already been opened with this email"
               }
               
          else:
               data={
                    "status":"success",
                    "message":"Profile created successfully"
               }
               new_profile = customer(
                    email=cd["email"],
                    password = cd["password"])
               new_profile.save()
          
          return JsonResponse(data)

@csrf_exempt
def login(request):
     cd=request.POST
     print(cd)

     #check if user exists
     try:
          exist= customer.objects.filter(phone=cd["email_or_phone"])[0]
          user_type= exist.phone
          print(exist)
          print(exist.password)
     
     except IndexError:
          try:
               exist= customer.objects.filter(email=cd["email_or_phone"])[0]
               user_type=exist.email
          except IndexError:
               data= {
               "status":"error",
               "message":"This email or phone number is not registered",
          }
               return JsonResponse(data)


     #check password
     if exist.password==cd["password"]:
          data= {
               "status":"success",
               "message":"Logged in successfully",
          }
          request.session["logged_in"]= user_type
          request.session.modified = True
          return JsonResponse(data)

     else:
          data= {
              "status":"error",
              "message":"incorrect email/phone or password",
          } 
          return JsonResponse(data)