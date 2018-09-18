from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Animal)
admin.site.register(Phylum)
admin.site.register(ClassA)
admin.site.register(Order)
admin.site.register(Family)
admin.site.register(Genus)
admin.site.register(Species)
