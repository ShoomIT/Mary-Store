from django.urls import path

from orders.views import (CanceledTemplateView, OrderCreateView,
                          OrderDetailView, OrderListView, SuccessTemplateView)

app_name = 'orders'

urlpatterns = [
    path('', OrderListView.as_view(), name='orders-list'),
    path('order-create/', OrderCreateView.as_view(), name='order-create'),
    path('order-success/', SuccessTemplateView.as_view(), name='order-success'),
    path('order-cancel/', CanceledTemplateView.as_view(), name='order-cancel'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order'),
]
