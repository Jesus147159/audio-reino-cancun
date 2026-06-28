from .models import SiteSettings


def site_settings(request):
    settings_obj = SiteSettings.objects.filter(is_active=True).order_by("-updated_at").first()
    return {"site_settings": settings_obj}
