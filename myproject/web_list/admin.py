from django.contrib import admin
from .models import Search

# Register your models here.
class SearchAdmin(admin.ModelAdmin):
    fields = [
        'search']

admin.site.register(Search, SearchAdmin)