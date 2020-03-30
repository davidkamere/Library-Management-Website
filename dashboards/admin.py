from django.contrib import admin
from dashboards.models import Borrowed, Waiting


# Register your models here.
admin.site.register(Borrowed)
admin.site.register(Waiting)

