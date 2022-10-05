from django.urls import path,include
from . import views 

urlpatterns = [
    path('',views.logandRegs),
    path('regsProcess',views.regs),
    path('success1',views.success1),
    path('login',views.login),
    path('logout',views.logout),
    path('logged',views.logged),
    
]
