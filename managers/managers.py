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
