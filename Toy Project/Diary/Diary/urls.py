
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('diary/', views.diary, name='diary'),
    path('chart/', views.chart, name='chart'),

]
