from django.shortcuts import render
from django.http import HttpResponse
from . import url






def index(request):
    return render(request,"index.html")
def fakenews(request):
    return render(request,"fakenews.html")
def summary(request):
    if request.method == "POST":
        x = request.POST.get('url')
        y = int(request.POST.get('limit'))
        article1 = url.getdata(x)
        text = url.summarizer(article1,y)
        return render(request,"summarizer.html",{'text':text,'x': x , 'y': str(y)})
    else:
        return render(request,"summarizer.html")
    
def pressnpulse(request):
    return render(request,"pressnpulse.html")
def usingurl(request):
     if request.method == "POST":
        x = request.POST.get('url')
        article1 = url.getdata(x)
        result = url.sentiment_analysis(article1)
        return render(request,"usingurl.html",{'result':result,'x':x})
     else:
        return render(request,"usingurl.html")
def usingname(request):
    return render(request,"usingname.html")
def usingimage(request):
    return render(request,"usingimage.html")
def about(request):
    return render(request,"about.html")
