from django.shortcuts import render, get_object_or_404
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

def services(request):
    services = models.Service.objects.all()
    return render (request, 'service/services.html', {
        'services': services,
    })

def service(request, service_id):
    service = get_object_or_404(models.Service, id=service_id)
    return render(request, 'service/service.html', {
        'service': service,
    })