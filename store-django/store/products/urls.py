from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.decorators.cache import cache_page

from products.views import ProductsListView, basket_add, basket_remove
from users.views import UserProfileBasketView

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('category/<int:category_id>/', cache_page(30)(ProductsListView.as_view()), name='category'),
    path('page/<int:page>', ProductsListView.as_view(), name='paginator'),
    path('profile/<int:pk>', login_required(UserProfileBasketView.as_view()), name='basket'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
