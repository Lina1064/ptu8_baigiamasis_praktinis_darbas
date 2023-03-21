from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views import generic
from . import models 


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
    paginator = Paginator(queryset.all(), 15)
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

def contacts(request):
    return render(request, 'service/contacts.html', {            
    })

class UserOrderListView(LoginRequiredMixin, generic.ListView):
    model = models.Order
    template_name = 'service/user_order_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(client=self.request.user)
        return qs