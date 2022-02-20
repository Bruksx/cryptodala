from django.shortcuts import render
from index.models import customer

# Create your views here.
def index(request):
    logged_in=request.session.get("logged_in")
    if logged_in: 
        try:
            user= customer.objects.filter(phone=logged_in)[0]
        except IndexError:
            user= customer.objects.filter(email=logged_in)[0]
    
    

    context={
        "email": user.email,
        "password": user.password,
        "phone": user.phone,
        "country_code": user.phone_code
    }


    return render(request, "index/profile.html", context)