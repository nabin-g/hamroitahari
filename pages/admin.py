from django.contrib import admin
from .models import HomePage
# Register your models here.
class HomePageAdmin(admin.ModelAdmin):
    homepage_display=('id', 'title', 'description')

admin.site.register(HomePage, HomePageAdmin)
