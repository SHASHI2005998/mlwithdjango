from django.urls import path
from .views import EmailView,ResultView
urlpatterns=[
    path('',EmailView.as_view(),name='home'),
    path('result/<int:pk>/', ResultView.as_view(), name='result'),
]