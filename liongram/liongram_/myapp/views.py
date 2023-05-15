from django.shortcuts import render, redirect
from .models import Post

def home(request):
    return render(request, 'index.html')

def delete(request, id):
    return render(request, 'post/delete.html')

def update(request, id):
    return render(request,'post/form.html')

def create(request):
    if request.method =="GET":
        return render(request,'post/form.html')
    else:
        img = request.FILES.get('img')
        content = request.POST.get('content')
        print(img)
        print(content)
        Post.objects.create(
            img = img,
            content=content,

        )
        return redirect('home')
    

def list(request):
    return render(request,'post/list.html')

def detail(request, id):
    return render(request,'post/detail.html')