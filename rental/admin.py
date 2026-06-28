from django.contrib import admin

from .models import Equipment, FAQ, GalleryImage, Lead, Package, Service, SiteSettings, Testimonial


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("business_name", "city", "phone", "email", "is_active", "updated_at")
    fieldsets = (
        ("Marca", {"fields": ("business_name", "tagline", "city", "logo", "hero_image")}),
        ("Contacto", {"fields": ("phone", "whatsapp_number", "email", "facebook_url", "instagram_url")}),
        ("Textos y SEO", {"fields": ("primary_cta", "secondary_cta", "meta_description", "is_active")}),
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "icon", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("title", "description")


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "is_featured", "is_active")
    list_filter = ("category", "is_featured", "is_active")
    search_fields = ("name", "description")


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ("name", "price_from", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("name", "description", "ideal_for")


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active", "updated_at")
    list_editable = ("order", "is_active")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "church_or_event", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "church_or_event", "quote")


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("question", "answer")


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "event_type", "event_date", "was_contacted", "created_at")
    list_filter = ("event_type", "was_contacted", "created_at")
    search_fields = ("name", "phone", "email", "location", "message")
    readonly_fields = ("created_at", "updated_at")
