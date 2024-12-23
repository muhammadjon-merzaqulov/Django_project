from django.shortcuts import render
from .models import Company, Worker


def homePageView(request):
    companies = Company.objects.all()
    workers = Worker.objects.all()
    context = {
        'companies': companies,
        'workers': workers
    }
    return render(request, 'home.html', context)


def teamPageView(request):
    workers = Worker.objects.all()
    context = {
        'workers': workers
    }
    return render(request, 'team.html', context)


def aboutPageView(request):
    companies = Company.objects.all()
    context = {
        'companies': companies
    }
    return render(request, 'about.html', context)


def contactPageView(request):
    return render(request, 'contact.html')

