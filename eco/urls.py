from django . urls  import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    
]
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),  # Add this line
]
