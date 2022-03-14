from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from core.forms import ProductForm
from core.models import Category, Product


class BaseView(TemplateView):
    template_name = 'index.html'


class InventoryView(TemplateView):
    template_name = 'details.html'


class UtilityCategoryView(TemplateView):
    template_name = 'categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


class AddCategoryView(View):
    def get(self, request):
        return render(request, 'categories.html')

    def post(self, request):
        category = request.POST.get('category')
        categories = Category()
        categories.name = category
        categories.save()
        return HttpResponse('category added')


class ActivityLog(TemplateView):
    template_name = 'Activity_Log.html'


class ProductUtilityView(View):
    def get(self, request):
        form = ProductForm()
        context = {'form': form}
        return render(request, 'Products.html', context)

    def post(self, request):
        form = ProductForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            return HttpResponse('submitted response')
        return render(request, 'Products.html', context)


class NotificationsView(TemplateView):
    template_name = 'blank.html'


class MessagesView(TemplateView):
    template_name = 'Activity_Log.html'


class ErrorPageView(TemplateView):
    template_name = '404.html'


class BlankPageView(TemplateView):
    template_name = 'blank.html'


class ChartsView(View):
    def get(self, request):
        labels = []
        data = []
        products = Product.objects.all()
        for products in products:
            labels.append(products.name)
            data.append(products.price)
        return render(request, 'charts.html', {'labels': labels, 'data': data})

    def post(self, request):
        return render(request, 'charts.html')


class TablesView(TemplateView):
    template_name = 'tables.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


