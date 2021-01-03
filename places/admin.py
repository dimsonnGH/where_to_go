from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from places.models import Place, PlaceImage
from django.utils . safestring import mark_safe

class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):

    model = PlaceImage
    readonly_fields = ['preview']
    fields = ('image', 'preview', 'order')

    def preview(self, obj):
        return mark_safe('<img src="{url}" height={height} />'.format(
            url = obj.image.url,
            height=133,
            )
    )


class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline,]

admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceImage)