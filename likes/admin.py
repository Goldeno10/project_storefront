from django.contrib import admin
from .models import LikedItem
# Register your models here.


@admin.register(LikedItem)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'content_type',
                    'object_id', 'content_object']
    search_fields = ['user__username', 'content_type__model']
    list_display_links = ['user', 'content_object']
    list_editable = ['content_type', 'object_id']

    class Meta:
        model = LikedItem
