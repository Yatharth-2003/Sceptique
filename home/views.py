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
