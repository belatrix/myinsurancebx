from django.urls import path

from .views import order_bulk_deletion, order_priority_change, auto_repair_shop_assign
from .views import order_creation, order_detail, order_list, order_update, upload_file, order_status_list
from .views import order_status_change, auto_repair_shop_list, order_budget_update


urlpatterns = [
    path('create/', order_creation, name='order_creation'),
    path('delete/list/', order_bulk_deletion, name='order_bulk_deletion'),
    path('<int:order_id>/budget/change/', order_budget_update, name='order_budget_update'),
    path('<int:order_id>/detail/', order_detail, name='order_detail'),
    path('<int:order_id>/status/change/to/<int:status_id>', order_status_change, name='order_status_change'),
    path('<int:order_id>/repairshop/change/to/<int:repairshop_id>', auto_repair_shop_assign, name='repairshop_assign'),
    path('<int:order_id>/priority/change/to/<int:priority>', order_priority_change, name='order_priority_change'),
    path('<int:order_id>/update/', order_update, name='order_update'),
    path('<int:order_id>/upload/file/', upload_file, name='upload_file'),
    path('list/', order_list, name='order_list'),
    path('status/list/', order_status_list, name='order_status_list'),
    path('repairshop/list/', auto_repair_shop_list, name='auto_repair_shop_list'),
]
