from django.contrib import admin
from .models import productMainModel
from .models import productColourModel
from .models import productImageModel

# Register your models here.
admin.site.register(productMainModel)
admin.site.register(productColourModel)
admin.site.register(productImageModel)
