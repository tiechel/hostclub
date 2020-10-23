from django import forms

from hostclub import models


class CustemerCreateForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['name', 'image', 'memo']
