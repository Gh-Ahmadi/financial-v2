from django.urls import path
from .views import *

urlpatterns = [
    path('cut/', CutList.as_view(), name='cut-list'),
    path('cut/<slug:slug>/', CutDetail, name='cut-detail'),
    path('cut/create/', CutCreate.as_view(), name='cut-create'),
]
