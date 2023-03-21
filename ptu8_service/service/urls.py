from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('service/<int:service_id>', views.service, name='service'),
    path('contacts/', views.contacts, name='contacts'),
    path('myorders/', views.UserOrderListView.as_view(), name='user_orders'),
]