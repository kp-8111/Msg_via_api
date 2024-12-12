from django.shortcuts import render
from requests import *

def home(request):
    if request.POST.get("btn"):
        try:
            url = "https://zenquotes.io/api/random"
            res = get(url)
            data = res.json()
            msg = data[0]['q']
            return render(request,"home.html",{"msg":msg})
        except Exception as e :
            msg = "Issue" + str(e)
            return render(request,"home.html",{"msg":msg})
    else:
        return render(request,"home.html")

# Create your views here.
