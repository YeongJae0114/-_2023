from django.urls import path
from crud import views 

urlpatterns=[
    path('',views.list, name='list'),
    path('new/',views.create, name='create'),
    path('<int:id>/',views.delete, name='detail'),
    path('<int:id>/edit/',views.update, name='update'),
    path('<int:id>/delete/',views.delete, name='delete'),

]