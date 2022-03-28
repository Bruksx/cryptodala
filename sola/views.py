from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer
from index.models import Customer, address

sol_client = Client("https://api.mainnet.solana.com")

# Create your views here.
@csrf_exempt
def create(request):
    if request.session.get("logged_in"):
        logged_in = request.session.get("logged_in")
        try:
            user= Customer.objects.filter(phone=logged_in)[0]
        except IndexError:
            user= Customer.objects.filter(email=logged_in)[0]
        kp = Keypair.generate()
        pub_key = str(kp.public_key)
        secret_key = kp.secret_key

        data = {
            'public_key': pub_key,
            'secret_key': secret_key.decode("latin-1"),
        }

        new_sol_address = address(
            customer = user,
            type = "SOL",
            address = pub_key,
            public_key = pub_key,
            private_key = secret_key,
        )

        new_sol_address.save()

        return JsonResponse(data)
    
    else:
        return 1