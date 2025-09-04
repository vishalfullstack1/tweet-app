from django.contrib import admin
from .models import Tweet

# admin.site.register(Tweet)

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'created_at', 'updated')
    search_fields = ('text', 'user_name')
    list_filter = ('created_at',)
# Register your models here.
