from django.contrib import admin

from . import models

class FoodAdmin(admin.ModelAdmin):
    list_display = ('title',)
#Add food model to admin database to use
admin.site.register(models.Food, FoodAdmin)