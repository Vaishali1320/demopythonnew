from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team
# Create your views here.
def demo(request):
   obj=Place.objects.all()
   obj1=Team.objects.all()
   return render(request,"index.html",{'result':obj,'result1':obj1})

#def addition(request):
  # x=int(request.GET['num1'])
   # y=int(request.GET['num2'])
   # res=x+y
   # sub=x-y
   #mul=x*y
   #div=x/y
   #return render(request,"result.html",{'result':res,'result1':sub,'result2':mul,'result3':div})

#def home(request):
    #return render(request,"home.html")

#def about(request):
    #return HttpResponse("Hello I'm about")

#def contact(request):
    #return render(request,"contact.html")

#def detail(request):
    #return HttpResponse("Hello I'm detail")

#def thanks(request):
    #return render(request,"thanks.html")