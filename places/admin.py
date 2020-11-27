from django.contrib import admin
from places.models import Place, PlaceImage

class PlaceImageInline(admin.TabularInline):
    model = PlaceImage

class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline,]

admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceImage)