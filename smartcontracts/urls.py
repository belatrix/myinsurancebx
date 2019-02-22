from django.conf.urls import url
from . import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='SmartContract API')


urlpatterns = [
    url(r'stamp/', views.Stamp.as_view()),
    url(r'verify/', views.Verify.as_view()),
    url(r'getBlockNumber/', views.GetBlockNumber.as_view()),
    url(r'getHash/', views.GetHash.as_view()),
]
