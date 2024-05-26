from django.shortcuts import render,redirect



def loginPage(request):
    return render(request,"login.html")