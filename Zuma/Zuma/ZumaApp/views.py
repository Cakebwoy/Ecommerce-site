from django.shortcuts import render 
from django.shortcuts import  redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .models import Signup


# Create your views here.



def signin(request):



    template ="main/signin.html"
    return render ( request,template)

# def signup(request):
    
    # if request.method = "POST":
    #     data = request.POST
    #     username = date["username"]
    #     password = data.get("password")

    #     user_exist = Signup.objects.filter(username=username)
    #     if len(user_exist) > 0:
    #         return render(request,"main/signin.html",{"error": "user already exist"} )
    #     else: 
    #         new_user = Signup(username = username, password = password)
    #         new_user.save()
    #         return render(request, "main/signup.html", {"msg":f'{username}succesfully signed up')
    #     return render(request,"main/signup.html",{"name": username})
    # return render(request,"main/signup.html")
            


    
    # template ="main/signin.html"

    # return render ( request,template)
    


def index(request):
    template ="main/index.html"

    return render ( request, template)

def buysel(request):
    template ="main/buysel.html"

    return render ( request, template)


