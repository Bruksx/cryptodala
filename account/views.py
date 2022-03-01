from django.shortcuts import render
from django.http import JsonResponse
from index.models import customer, handle_uploaded_file
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError
import random

# Create your views here.
def index(request):
    random_variable= random.randint(1,10000)
    logged_in=request.session.get("logged_in")
    if logged_in: 
        try:
            user= customer.objects.filter(phone=logged_in)[0]
        except IndexError:
            user= customer.objects.filter(email=logged_in)[0]
    
    

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
        "logged_in": logged_in,
    }

    if request.GET.get("profile"):
         return render(request, "index/profile.html", context)



    return render(request, "index/index.html", context)

@csrf_exempt
def modify(request):
    arg = request.POST
    file = request.FILES
    print(arg)
    print(file)
    
    ext = str(file["image"]).split(".")[-1]
    print(arg)

    random_variable= random.randint(1,10000)
    logged_in=request.session.get("logged_in")
    if logged_in: 
        try:
            user= customer.objects.filter(phone=logged_in)[0]
        except IndexError:
            user= customer.objects.filter(email=logged_in)[0]
    
    try:
        user.email = arg.get("email")
    except IntegrityError:
        user.email = ""
    try:
        user.firstname = arg.get("firstname")
    except IntegrityError:
        user.firstname = ""
    try:
        user.lastname = arg.get("lastname")
    except IntegrityError:
        user.lastname = ""
    try:
        user.middlename = arg.get("middlename")
    except IntegrityError:
        user.middlename = ""

    if len(request.FILES) >= 0:
        user.avatar = "/static/avatar/{}.{}".format(user.id, ext)
        handle_uploaded_file(user.id, file["image"], ext)
    
    user.save()
    

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



    return render(request, "index/profile.html", context)