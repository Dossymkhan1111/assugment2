from django.shortcuts import render, redirect
from scrap import topAccounts

accounts = topAccounts()

def index(request): 
    context = {
        "accounts": accounts,   
    }

    return render(request, 'chartapp/index.html', context)
