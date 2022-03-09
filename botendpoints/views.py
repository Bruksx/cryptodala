from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from index.models import Verification, Customer

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
    user.verified = True
    data = {
        "message": "{} has been verified".format(user)
    }
    verification = Verification.objects.filter(customer=user)[0]
    verification.delete()
    user.save()

    return JsonResponse(data)