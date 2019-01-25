from django.urls import path

from .views import order_detail


urlpatterns = [
    path('<int:order_id>/detail/', order_detail, name='order_detail'),
]
