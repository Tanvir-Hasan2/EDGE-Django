from django.urls import path
from .views import ProductView

from . import views

urlpatterns = [
    path("",views.index, name = "index"),
    path('api/v1/products/', ProductView.as_view(),name='product-op'),
    path("api/v1/products/<int:id>/", ProductView.as_view(), name = "product-op-with-id"),
]