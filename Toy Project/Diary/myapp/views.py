from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def diary(request):
    return render(request, 'asd.html')

def chart(request):
    return render(request, 'Chart.html')

# Create your views here.
