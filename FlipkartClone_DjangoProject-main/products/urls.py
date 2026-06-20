from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.home, name='home'),
    path('add/', views.add_product, name='add_product'),    #add_product 
    path('delete/<int:id>/', views.delete_products,name='delete'),  #delete_product 
    path('update/<int:id>/', views.update_products, name='update_products'), #update_product 
    path('', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]
