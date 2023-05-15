
from django.contrib import admin
from django.urls import path, include
from myapp import views
from crud import urls as crud_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    #path('<str:username>/', views.url_par_view, name='par'),
    path('crud/', include(crud_urls)),

]
