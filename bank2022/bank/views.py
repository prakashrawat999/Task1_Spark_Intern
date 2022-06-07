from django.shortcuts import render, redirect
from .models import customer, transaction_details
from django.db.models import F
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def customer_details(request):
    all_entries = customer.objects.all()
    context = {
        "cust_details" : all_entries
    }
    return render(request, 'customer_details.html', context)

    query1 = customer.objects.get(name =cust)
    query2 = customer.objects.exclude(name = cust)
    context = {
             "cust_name" : query1,
             "all_details" : query2,
             }
    return render(request, 'customer_details.html', context)


def transaction(request):
    if request.method =="POST":
        receiver= request.POST.get('to')
        money = request.POST.get('amount2')
        sender = request.POST.get('submit')
        query2 = customer.objects.get(name = sender)
        query2.amount= F('amount')- money
        query2.save()
        query1 = customer.objects.get(name= receiver)
        query1.amount= F('amount')+ money
        query1.save()
        result = customer.objects.get(name = sender)
        print(result)
        transact = transaction_details()
        transact.user_name = sender
        transact.user_accno = result.account_no
        transact.user_balance = result.amount
        transact.user_deposit = money
        transact.destiname = receiver
        transact.date = datetime.today()
        transact.save()
        return redirect('transaction')
    all_entries = transaction_details.objects.all()
    context = {
            "history" : all_entries
        }
    return render(request, 'transaction.html', context)

def view(request):
    if request.method == "POST":
         cust = request.POST.get('submit')
         query1 = customer.objects.get(name =cust)
         query2 = customer.objects.exclude(name = cust)
         context = {
             "cust_name" : query1,
             "all_details" : query2,
             }
         return render(request, 'view.html', context)


           