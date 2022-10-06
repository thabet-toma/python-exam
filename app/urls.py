from django.urls import path,include
from . import views 

urlpatterns = [
    path('',views.logandRegs),
    path('regsProcess',views.regs),
    path('success1',views.success1),
    path('login',views.login),
    path('logout',views.logout),
    path('logged',views.logged),
    path('new/tree',views.addNew),
    path('addProcess',views.addProcess),
    path('backToDash',views.backToDash),
    path('user/account',views.myTrees),
    path('edit/<int:id>',views.editShow),
    path('editProcess',views.editProcess),
    path('show/<int:id>',views.showTree),
    path('delete/<int:id>',views.delete),
    
]
