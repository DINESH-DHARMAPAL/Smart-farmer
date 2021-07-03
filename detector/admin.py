from django.contrib import admin
from .models import Photos, AnimalsDetected, HumansDetected
# Register your models here.

admin.site.register(Photos)
admin.site.register(AnimalsDetected)
admin.site.register(HumansDetected)