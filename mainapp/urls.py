from django.urls import path
from .views import PersonStat, QueryPersons
from .apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('stat/<int:pk>', PersonStat.as_view(), name='stat'),
    path('query/', QueryPersons.as_view(), name='query'),
]
