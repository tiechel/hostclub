from django.urls import path
from hostclub import views

app_name = 'hostclub'

urlpatterns = [
    path('/', views.TopView.as_view(), name='top'),
]
