
from django.urls import path
from . import views

urlpatterns = [
    path('welcomeapp-login/', views.input, name='iriguchi'),
    path('output-login/', views.output, name='welcome'),
    path('visitor_kanri/', views.kanri, name='kanri'),
    path('edit-del/<int:pk>/', views.edit, name='edit_del'),
    path('delete-page/<int:pk>/',views.delete, name='deldata'),
]
