from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from hostclub import models
from hostclub import forms


class CustomerCreate(CreateView):
    template_name = 'hostclub/customer/create.html'
    model = models.Customer
    form_class = forms.CustemerCreateForm
    success_url = 'hostclub:customer_create'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'お客様登録画面'
        return context


# class ReserveCreate(CreateView):
#     pass
