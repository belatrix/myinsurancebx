from django.urls import path

from .views import order_creation, order_detail, order_list, order_update, upload_file, order_status_list
from .views import order_status_change

urlpatterns = [
    path('create/', order_creation, name='order_creation'),
    path('<int:order_id>/detail/', order_detail, name='order_detail'),
    path('<int:order_id>/status/change/to/<int:status_id>', order_status_change, name='order_status_change'),
    path('<int:order_id>/update/', order_update, name='order_update'),
    path('<int:order_id>/upload/file/', upload_file, name='upload_file'),
    path('list/', order_list, name='order_list'),
    path('status/list/', order_status_list, name='order_status_list'),
]
