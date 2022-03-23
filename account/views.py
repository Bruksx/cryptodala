from urllib.request import HTTPRedirectHandler
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from index.models import Customer, Verification, address, handle_uploaded_file, handle_verification_doc
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError
import random

# Create your views here.
def index(request):
    random_variable= random.randint(1,10000)
    logged_in=request.session.get("logged_in")

    

    if logged_in: 
        try:
            user= Customer.objects.filter(phone=logged_in)[0]
        except IndexError:
            user= Customer.objects.filter(email=logged_in)[0]
    
    

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



    return render(request, "index/index2.html", context)

@csrf_exempt
def modify(request):
    arg = request.POST
    file = request.FILES

    
    if request.FILES.get("image"):
        ext = str(file["image"]).split(".")[-1]

    random_variable= random.randint(1,10000)
    logged_in=request.session.get("logged_in")
    if logged_in: 
        try:
            user= Customer.objects.filter(phone=logged_in)[0]
        except IndexError:
            user= Customer.objects.filter(email=logged_in)[0]
    
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

    if request.FILES.get("image"):
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

@csrf_exempt
def verify(request):
    file = request.FILES
    data = request.POST

    logged_in=request.session.get("logged_in")
    if logged_in: 
        try:
            user= Customer.objects.filter(phone=logged_in)[0]
        except IndexError:
            user= Customer.objects.filter(email=logged_in)[0]

    if file.get("document"):
        print(user.id)

        ext = handle_verification_doc(user.id, file["document"])

        old_verification = Verification.objects.filter(customer= user)
        for docs in old_verification:
            docs.delete()

        new_ver = Verification(
            customer = user,
            doc_type = data.get("type"),
            document = "/static/verify/{}.{}".format(user.id, ext)
        )
        new_ver.save()


    return redirect("/account")

@csrf_exempt
def add_address(request):
    data = request.POST
    print(data)
    logged_in=request.session.get("logged_in")
    if logged_in: 
        try:
            user= Customer.objects.get(phone=logged_in)
        except:
            user= Customer.objects.get(email=logged_in)
    else:
        redirect("/")
    
    new_address = address(
        customer = user,
        type = data.get("type"),
        address = data.get("address"),
    )
    try:
        new_address.save()
        print(new_address)
        return redirect("/account?profile=1")
    except IntegrityError:
        return redirect("/account?profile=1")

def get_address(request):
    logged_in = request.session.get("logged_in")
    if logged_in: 
        try:
            user= Customer.objects.get(phone=logged_in)
        except:
            user= Customer.objects.get(email=logged_in)
    else:
        data = {
            "message": "you are not logged in"
        }
        return JsonResponse(data)
    
    address_list = address.objects.filter(customer = user).all()
    data = {}
    for adrs in address_list:
        data[adrs.address] = adrs.type
    print(data)
    return JsonResponse(data)






def logout(request):
    del request.session["logged_in"]
    return redirect("/")