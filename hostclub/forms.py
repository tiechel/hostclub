from django import forms

from hostclub import models

"""
フォームの作り方参考
@ref https://qiita.com/dai-takahashi/items/5042db0792c9f7d01c1e
"""

class CustemerCreateForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['name', 'image', 'memo']
