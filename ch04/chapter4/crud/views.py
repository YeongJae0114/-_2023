from django.shortcuts import render

def list(request):
    return render(request, 'list.html')

def create(request):
    return render(request, 'form.html')

def delete(request):
    return render(request, 'delete.html')

def update(request):
    return render(request, 'form.html')

def detail(request):
    return render(request, 'detail.html')