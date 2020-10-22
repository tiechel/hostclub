from django.contrib import admin
from hostclub import models


admin.site.register(models.Host)
admin.site.register(models.Customer)
admin.site.register(models.Seat)
admin.site.register(models.Menu)
admin.site.register(models.Reserve)
