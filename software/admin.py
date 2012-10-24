from software.models import Software
from software.models import Lector
from django.contrib import admin

class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'product', 'appv', 'version', 'comment')
    search_fields = ['product']

class LectorAdmin(admin.ModelAdmin):
    list_display = ('username', 'fullname', 'telephone', 'software')
    search_fields = ['username']

admin.site.register(Software, SoftwareAdmin)
admin.site.register(Lector, LectorAdmin)
