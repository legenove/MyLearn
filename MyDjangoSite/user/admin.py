from django.contrib import admin

from .models import Account
class AcountAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'username', 'email', 'is_active')

admin.site.register(Account, AcountAdmin)