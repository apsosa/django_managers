from typing import Optional
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
#from managers.models import Order

class OrderManager(models.Manager):
    def find(self, order_id: int) -> Optional['Order']:
        queryset = self.get_queryset()
        try:
            instance = queryset.get(pk=order_id)
        except ObjectDoesNotExist:
            instance = None
        finally:
            return instance

    def find_all_for(self, customer_id: int) -> models.QuerySet:
        queryset = self.get_queryset()
        return queryset.filter(customer_id=customer_id)
    
    def find_all_with_product(self, product_id: int) -> models.QuerySet:
        queryset = self.get_queryset()
        return queryset.filter(items__product_id=product_id)