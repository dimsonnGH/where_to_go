from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from places.models import Place, PlaceImage
from django.utils.safestring import mark_safe
from django.utils.html import format_html


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline) :
    model = PlaceImage
    readonly_fields = ['preview']
    fields = ('image', 'preview', 'order')

    def preview(self, obj) :
        if obj.image :
            preview_content = format_html('<img src="{url}" height={height} />', url=obj.image.url, height=133)
        else :
            preview_content = 'Изображение не загружено'

        return preview_content


class PlaceAdmin(admin.ModelAdmin) :
    inlines = [PlaceImageInline, ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceImage)
