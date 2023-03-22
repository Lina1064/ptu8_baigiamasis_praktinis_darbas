from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views import generic
from . import models 


def home(request):
    service_count = models.Service.objects.count()
    customer_count = models.Customer.objects.count()
    done_order_count = models.Order.objects.filter(status='d').count()
    service_1 = models.ServiceOrder.objects.filter(service=1).count()
    service_2 = models.ServiceOrder.objects.filter(service=2).count()
    service_3 = models.ServiceOrder.objects.filter(service=3).count()
    service_4 = models.ServiceOrder.objects.filter(service=4).count()
    service_5 = models.ServiceOrder.objects.filter(service=5).count()
    service_6 = models.ServiceOrder.objects.filter(service=6).count()
    service_7 = models.ServiceOrder.objects.filter(service=7).count()
    service_8 = models.ServiceOrder.objects.filter(service=8).count()
    service_9 = models.ServiceOrder.objects.filter(service=9).count()
    service_10 = models.ServiceOrder.objects.filter(service=10).count()
    service_11 = models.ServiceOrder.objects.filter(service=11).count()
    service_list = ['ISO S - ns', 'ISO 1 - ns', 'R - ns', 'DM - ns', 'ISO S - fs', 'ISO 1 - fs', 'R - fs',  'DM - fs', 'RS 1-3h - ns', 'RS - 4ns', 'CW']
    number_list = [service_1, service_2, service_3, service_4, service_5, service_6, service_7, service_8, service_9, service_10, service_11]
    return render(request, 'service/home.html', {
        'service_count': service_count,
        'customer_count': customer_count,
        'done_order_count': done_order_count,
        'service_list': service_list,
        'number_list': number_list
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