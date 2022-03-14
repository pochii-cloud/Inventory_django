from django.urls import path

from core.views import *
from orders.views import OrderView, AddOrderView

urlpatterns = [
    path('OrderView/', OrderView.as_view(), name='OrderView'),
    path('AddOrderView/', AddOrderView.as_view(), name='AddOrderView'),

]