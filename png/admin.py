from django.contrib import admin
from.models import Reg
from.models import news
from.models import event

# Register your models here.

admin.site.register(Reg),
admin.site.register(news),
admin.site.register(event)