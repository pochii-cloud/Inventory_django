from django.urls import path

from core.views import *

urlpatterns = [
    path('', BaseView.as_view(), name='BaseView'),
    path('InventoryView/', InventoryView.as_view(), name='InventoryView'),
    path('UtilityCategoryView/', UtilityCategoryView.as_view(), name='UtilityCategoryView'),
    path('AddCategoryView/', AddCategoryView.as_view(), name='AddCategoryView'),
    path('ProductUtilityView/', ProductUtilityView.as_view(), name='ProductUtilityView'),
    path('ActivityLog/', ActivityLog.as_view(), name='ActivityLog'),
    path('NotificationsView/', NotificationsView.as_view(), name='NotificationsView'),
    path('MessagesView/', MessagesView.as_view(), name='MessagesView'),
    path('ErrorPageView/', ErrorPageView.as_view(), name='ErrorPageView'),
    path('BlankPageView/', BlankPageView.as_view(), name='BlankPageView'),
    path('ChartsView/', ChartsView.as_view(), name='ChartsView'),
    path('TablesView/', TablesView.as_view(), name='TablesView'),

]
