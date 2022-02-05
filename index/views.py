from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import customer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
     return render(request, "index/index.html")

@csrf_exempt
def register(request):
     cd= request.POST
     
     if cd.get("contact_type")== "mobile":
          full_phone=  cd["country_code"] + cd["mobile"]
          full_phone =  "".join(full_phone.split())
          already_exists= customer.objects.filter(phone=full_phone)
          if already_exists:
               data ={
                    "status": "error",
                    "message": "A profile has already been opened with this phone number"
               }
               
          else:
               data={
                    "status":"success",
                    "message":"Profile created successfully"
               }
               new_profile = customer(phone=full_phone)
               new_profile.save()
          
          return JsonResponse(data)

     
     if cd.get("contact_type")== "email":
          already_exists= customer.objects.filter(phone=cd["email"])
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
               new_profile = customer(email=cd["email"])
               new_profile.save()
          
          return JsonResponse(data)
     """
	#check if email already exists
     already_exists= customer.objects.filter(email=cd["email"])
     print(already_exists)
     if len(already_exists) > 0:
	     messages.error(request, 'Document deleted.')
	     return redirect("registration")
		
     #check if password matches
     if cd["password"] != cd["confirm_password"]:
          messages.error(request, 'Password do not match')
          return redirect("registration")
     #check password length
     password= cd["password"]
     if len(password)<5:
          messages.error(request, 'Password too short. Should be at least 6 characters')
          return redirect("registration")
		
     new_user= collector(
	     first_name=cd["first_name"],
	     middle_name=cd["middle_name"],
	     last_name= cd["last_name"],
	     password= cd["password"],
          email= cd["email"],
	     )
     new_user.save()
		
     messages.error(request,"Registration Successful")
     """
     return redirect("/")