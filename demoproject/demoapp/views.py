from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")
# def about(request):
#     return render(request,"inddd.html")
# def contact(request):
#     return render(request,"cont.html")
# def details(request):
#     return render(request,"det.html")
# def thanks(request):
#     return render(request,"index.html")