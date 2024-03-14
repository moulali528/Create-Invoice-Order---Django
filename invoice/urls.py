from django.contrib import admin
from django.urls import path, include
from invoice import views
#from invoice import urls

urlpatterns = [
    path('', views.invoiceList, name = 'LIST'),
    path('<int:pk>/', views.invoiceDetails, name = 'Datails'),
]