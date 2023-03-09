from __future__ import unicode_literals
from django.shortcuts import render
from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse, JsonResponse

cl = MpesaClient()
stk_push_callback_url = 'https://api.darajambili.com/express-payment'
b2c_callback_url = 'https://api.darajambili.com/b2c/result'


def oauth__success(request):
    r = cl.access_token()
    return JsonResponse(r, safe=False)


def index(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone')
        amount = request.POST.get('amount')
        amount = int(amount)
        account_Reference = "HARRISON"
        transaction_desc = 'STK Push Description'
        callback_url = stk_push_callback_url
        r = cl.stk_push(phone_number, amount, account_Reference, transaction_desc,callback_url)
        return JsonResponse(r.response_description, safe=False)

    return render(request, 'index.html')
