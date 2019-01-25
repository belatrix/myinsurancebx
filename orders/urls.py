from django.urls import path

from .views import order_detail, order_list


urlpatterns = [
    path('<int:order_id>/detail/', order_detail, name='order_detail'),
    path('list/', order_list, name='order_list'),
]
