from django.urls import path

from .views import ProductItemsView

urlpatterns = [
    path('product/', ProductItemsView.as_view(), name='product_view')
]