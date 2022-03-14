from django.urls import path

from core.views import *
from supplies.views import AddSuppliesView, AddSuppliersView

urlpatterns = [
       path('AddSuppliesView/', AddSuppliesView.as_view(), name='AddSuppliesView'),
       path('AddSuppliersView/', AddSuppliersView.as_view(), name='AddSuppliersView'),


]