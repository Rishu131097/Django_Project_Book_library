from django.shortcuts import render,HttpResponseRedirect

from mainApp.models import Books

# Create your views here.
def home(request):
    data = Books.objects.all()
    return render(request, "index.html" ,{"Data":data})
def addRecord(request):
    if(request.method=="POST"):
          e = Books()
          e.id = request.POST.get("id")
          e.title = request.POST.get("title")
          e.author = request.POST.get("author")
          e.privilege = request.POST.get("privilege")
          e.publisher = request.POST.get("publisher")
          e.city = request.POST.get("city")
          e.state = request.POST.get("state")
          e.save()
          return HttpResponseRedirect("/")
    return render(request, "add.html")
def deleteRecord(request,id):
    data = Books.objects.get(id=id)  
    data.delete()
    return HttpResponseRedirect("/")  

def updateRecord(request,id):
    data = Books.objects.get(id=id) 
    return render(request,"update.html",{"Data":data}) 