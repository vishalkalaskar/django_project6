from django.shortcuts import render
# from models import registration
from . models import registration
def showindex(request):
    return render(request,"index.html")

def useregi(request):
    if request.method =="POST":
        n=  request.POST.get("name")
        num =  request.POST.get("contact")
        email = request.POST.get("email")
        passs = request.POST.get("pass")
        loc =   request.POST.get("location")

        registration(name=n,contact=num,email=email,password=passs,location=loc).save()
        return render(request,"registration.html",{"message":"Registrtion is Done"})
    else:
       return render(request,"registration.html")

def userlogin(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        passs = request.POST.get("pass")
        username = request.POST.get("username")
        n = request.POST.get("name")

        try:
            l_crential =registration.objects.get(email=username, password=passs)
            name= registration(name=n)
            return render(request,"welcome.html",{"name":name})
        except registration.DoesNotExist:
            return render(request,"login.html", {"messg":"Invalid user"})
