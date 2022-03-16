from django.urls import path
from . import views 

urlpatterns = [
    
    path('', views.ProductsList.as_view()),
    path('<int:pk>/', views.ProductsDetails.as_view()),
]







# urlpatterns = [
#     path('', views.products_list),
#     path('<int:pk>/', views.product_details),  
# ]