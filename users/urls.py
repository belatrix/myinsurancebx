from django.urls import path

from .views import user_detail, user_list


urlpatterns = [
    path('<int:user_id>/detail/', user_detail, name='user_detail'),
    path('list/', user_list, name='user_list'),
]
