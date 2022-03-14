from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from supplies.models import Suppliers, Supplies


class AddSuppliesView(View):
    def get(self, request):
        return render(request, 'add_supplies.html')

    def post(self, request):
        username = request.POST.get('username')
        products = request.POST.get('products')
        quantity = request.POST.get('quantity')
        cost = request.POST.get('cost')
        date = request.POST.get('date')
        supplied = request.POST.get('supplies')
        supplies = Supplies()
        supplies.Username = username
        supplies.supplies = products
        supplies.quantity = quantity
        supplies.cost = cost
        supplies.supply_date = date
        supplies.supplied = supplied
        supplies.save()
        return HttpResponse('submitted')


class AddSuppliersView(View):
    def get(self, request):
        return render(request, 'add_suppliers.html')

    def post(self, request):
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        location = request.POST.get('location')
        suppliers = Suppliers()
        suppliers.username = username
        suppliers.phone = phone
        suppliers.address = address
        suppliers.location = location
        suppliers.save()
        return HttpResponse('submitted')
