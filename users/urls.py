from django.urls import path

from .views import user_detail, user_list, CustomAuthToken, user_logout


urlpatterns = [
    path('authenticate/', CustomAuthToken.as_view()),
    path('<int:user_id>/detail/', user_detail, name='user_detail'),
    path('list/', user_list, name='user_list'),
    path('logout/', user_logout, name='user_logout'),
]
