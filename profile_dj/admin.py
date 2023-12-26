from django.contrib import admin
from .models import Account_detail, Bank_detail

@admin.register(Account_detail)
class Account_detail(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone',)
    list_filter = ('first_name', 'email')
    search_fields = ('first_name', 'email')

@admin.register(Bank_detail)
class Bank_detail(admin.ModelAdmin):
    list_display = ('bank_name', 'bank_number', 'bank_account', 'bank_branch',)
    list_filter = ('bank_account', 'bank_number')
    search_fields = ('bank_account', 'bank_number')