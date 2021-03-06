from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)
    search_fields = ("town", "address", "owners__owner")
    list_display = ("address", "price", "new_building", "construction_year", "town")
    list_editable = ("new_building",)
    list_filter = ("new_building", "rooms_number", "has_balcony")
    raw_id_fields = ("liked_by",)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("flats",)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ("author", "flat")


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
