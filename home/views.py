from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
def fakenews(request):
    return render(request,"fakenews.html")
def summary(request):
    return render(request,"summarizer.html")
def pressnpulse(request):
    return render(request,"pressnpulse.html")
def usingurl(request):
    return render(request,"usingurl.html")
def usingname(request):
    return render(request,"usingname.html")
def usingimage(request):
    return render(request,"usingimage.html")