from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('service/<int:service_id>', views.service, name='service'),
    path('contacts/', views.contacts, name='contacts'),
    path('myorders/', views.UserOrderListView.as_view(), name='user_orders'),
    path('customer/', views.new_customer, name='customer_data'),
    path('myorders/new/', views.UserOrderCreateView.as_view(), name='user_order_create'),
]