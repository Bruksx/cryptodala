from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from index.models import Verification, Customer, user_package
import requests

# Create your views here.
def verifications(request):
    pending_verifications = Verification.objects.all()
    data = {}
    for i in pending_verifications:
        dict = data[str(i.customer)] = {}
        dict["id"] = str(i.customer)
        dict["real_id"] = i.customer.id
        dict["doc_type"] = i.doc_type
        dict["document"] = i.document

    return JsonResponse(data)

def verify(request,customer_id):
    user = Customer.objects.filter(id=customer_id)[0]
    context = user_package(user)
    
    data = {
        "message": "{} has been verified".format(user)
    }
    verification = Verification.objects.get(customer=user)
    context["src"] = verification.document
    context["doc_type"] = verification.doc_type

    if request.GET.get("verify"):
        user.verified = True
        data = {
        "message": "{} has been verified".format(user)
    }
        verification.delete()
        user.save()
        return JsonResponse(data)

    return render(request, "index/verify.html", context)



def check_ip(request):
    ip = requests.get("https://ipinfo.io/json").json().get("ip")
    return HttpResponse(ip)