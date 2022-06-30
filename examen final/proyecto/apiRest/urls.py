from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductoView.as_view()),
    path('<int:id>/', views.ProductoDetail.as_view()),    
]