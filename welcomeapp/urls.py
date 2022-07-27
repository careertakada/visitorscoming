
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('welcomeapp-login/', views.input, name='iriguchi'),
    path('output-login/', views.output, name='welcome'),
    path('visitor_kanri/', views.kanri, name='kanri'),
    path('edit-del/<int:pk>/', views.edit, name='edit_del'),
    path('delete-page/<int:pk>/',views.delete, name='deldata'),
    path('register/',views.AccountRegistration.as_view(), name='register'),
    path('login/',views.Login,name='Login'),
    path("logout/",views.Logout,name="Logout"),
    path("loginhome/",views.home,name="home"),
]
