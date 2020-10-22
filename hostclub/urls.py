from django.urls import path
from hostclub import views
from hostclub.views import customer as customer_view


app_name = 'hostclub'

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('customer/create', customer_view.CustomerCreate.as_view(), name="customer_create")
]
