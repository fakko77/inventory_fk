from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('connect/', views.check, name='connect'),
    path('setting/', views.setting, name='setting'),

]
