from django.shortcuts import render
from . import models 

# Create your views here.

def home(request):
    service_count = models.Service.objects.count()
    customer_count = models.Customer.objects.count()
    done_order_count = models.Order.objects.filter(status='d').count()

    return render(request, 'service/home.html', {
        'service_count': service_count,
        'customer_count': customer_count,
        'done_order_count': done_order_count,
    })