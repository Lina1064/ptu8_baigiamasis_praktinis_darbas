from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class Customer(models.Model):
    first_name = models.CharField(_('first name'), max_length=50, db_index=True)
    last_name = models.CharField(_('last name'), max_length=50, db_index=True)
    address = models.CharField(_('address'), max_length=100, db_index=True)
    email = models.EmailField(_('email'), db_index=True)
    phone_number = models.CharField(_('phone number'), max_length=15, db_index=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.address} {self.email} {self.phone_number}"

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name =_('customer')
        verbose_name_plural = _('customers')


class Service(models.Model):
    name = models.CharField(_('name'), max_length=100, db_index=True)
    price = models.DecimalField(_('price'), max_digits=8, decimal_places=2)
    description = models.TextField(_('description'), max_length=4000, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} {self.price}"
    
    class Meta:
        ordering = ['name']
        verbose_name =_('service')
        verbose_name_plural = _('services')

class Order(models.Model):
    date = models.DateTimeField(_('order date'), auto_now_add=True)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name='orders',
        verbose_name=_('customer')
    )
    total_order_price = models.DecimalField(_('total order price'), max_digits=10, decimal_places=2, blank=True)
    
    @property
    def total_order_price(self):
        total = 0
        for line in self.service_orders.all():
            total+=line.total_price
        return total

    ORDER_STATUS = (
        ('o', _('ordered')),
        ('p', _('in process')),
        ('d', _('done')),
        ('c', _('cancelled')),
    )
    
    status = models.CharField(_('status'), max_length=1, choices=ORDER_STATUS, default='o')

    def __str__(self) -> str:
        return f"{self.date} {self.customer} {self.status} {self.total_order_price}"

    class Meta:
        ordering = ['date']
        verbose_name =_('order')
        verbose_name_plural = _('orders') 


class ServiceOrder(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.PROTECT,
        related_name='service_orders',
        verbose_name=_('service'),
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT,
        related_name='service_orders',
        verbose_name=_('orders'),
    )
    quantity = models.PositiveIntegerField(_('quantity'), default=1)
    total_price = models.DecimalField(_('total order price'), max_digits=10, decimal_places=2, blank=True)

    @property
    def total_price(self):
        return self.service.price * self.quantity
    
    def __str__(self) -> str:
        return f"{self.service} {self.order} {self.quantity} {self.total_price}"
    
    class Meta:
        ordering = ['order']
        verbose_name =_('service order')
        verbose_name_plural = _('service orders') 