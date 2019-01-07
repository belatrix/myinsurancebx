from django.urls import path

from .views import user_detail


urlpatterns = [
    path('<int:user_id>/detail/', user_detail, name='user_detail'),
]
