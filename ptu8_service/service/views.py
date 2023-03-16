from django.core.paginator import Paginator
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
    queryset = models.Service.objects
    query = request.GET.get('search')
    if query:
        queryset = queryset.filter(name__icontains=query)
    paginator = Paginator(queryset.all(), 10)
    page_number = request.GET.get('page')
    services = paginator.get_page(page_number)
    return render (request, 'service/services.html', {
        'services': services,
    })

def service(request, service_id):
    service = get_object_or_404(models.Service, id=service_id)
    return render(request, 'service/service.html', {
        'service': service,
    })