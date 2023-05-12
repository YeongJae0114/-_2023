from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    print(f'request.method: {request.method}')
    if request.method=='GET':
        print( f'request.GET: {request.GET}')
    elif request.method=='POST':
        print(f'request.POST: {request.POST}')
    return render(request,'home.html')

def url_par_view(request, username):
    print('url_par_view')
    print(f'username:{username}')
    print(f'request.GET: {request.GET}')
    return HttpResponse(username)


