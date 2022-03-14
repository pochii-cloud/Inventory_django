from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from orders.models import Orders


class OrderView(TemplateView):
    template_name = 'orders.html'


class AddOrderView(View):
    def get(self, request):
        return render(request, 'addorder.html')

    def post(self, request):
        product = request.POST.get('product')
        quantity = request.POST.get('quantity')
        cost = request.POST.get('cost')
        date = request.POST.get('date')
        delivered = request.POST.get('delivered')
        orders = Orders()
        orders.product = product
        orders.quantity = quantity
        orders.cost = cost
        orders.date_ordered = date
        orders.delivered = delivered
        orders.save()
        return HttpResponse('submitted')
