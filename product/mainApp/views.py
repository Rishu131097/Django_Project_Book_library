from itertools import product
from django.shortcuts import render,HttpResponseRedirect
from mainApp.models import Product

# Create your views here.
def home(request):
    data = Product.objects.all()
    return render(request, "index.html" ,{"Data":data})
def addRecord(request):
    if(request.method=="POST"):
          e = Product()
          e.id = request.POST.get("id")
          e.name = request.POST.get("name")
          e.price = request.POST.get("price")
          e.product_description = request.POST.get("product_description")
          e.city = request.POST.get("city")
          e.state = request.POST.get("state")
          e.save()
          return HttpResponseRedirect("/")
    return render(request, "add.html")
def deleteRecord(request,id):
    data = Product.objects.get(id=id)  
    data.delete()
    return HttpResponseRedirect("/")  

def updateRecord(request,id):
    data = Product.objects.get(id=id)
    if(request.method=="POST"):
          data = Product()
          data.id = request.POST.get("id")
          data.name = request.POST.get("name")
          data.price = request.POST.get("price")
          data.product_description = request.POST.get("product_description")
          data.city = request.POST.get("city")
          data.state = request.POST.get("state")
          data.save()
          return HttpResponseRedirect("/") 
    return render(request,"update.html",{"Data":data})   