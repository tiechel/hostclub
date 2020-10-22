from django.shortcuts import render
from django.views.generic import TemplateView


class TopView(TemplateView):
    template_name = 'hostclub/top.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'トップページ'
        return context
