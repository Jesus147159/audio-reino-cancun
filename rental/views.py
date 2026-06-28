import json
from urllib.parse import quote_plus

from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .forms import LeadForm
from .models import Equipment, FAQ, GalleryImage, Package, Service, SiteSettings, Testimonial


def home(request):
    settings_obj = SiteSettings.objects.filter(is_active=True).order_by("-updated_at").first()
    form = LeadForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        lead = form.save()
        messages.success(request, "Recibimos tu solicitud. Te contactaremos pronto para preparar tu cotizacion.")

        whatsapp = (settings_obj.whatsapp_number if settings_obj else "") or getattr(settings, "WHATSAPP_NUMBER", "")
        if whatsapp:
            text = (
                f"Hola, soy {lead.name}. Necesito cotizar audio para un evento cristiano. "
                f"Tipo: {lead.get_event_type_display()}. Fecha: {lead.event_date or 'por confirmar'}. "
                f"Ubicacion: {lead.location or 'por confirmar'}."
            )
            return redirect(f"https://wa.me/{whatsapp}?text={quote_plus(text)}")
        return redirect(f"{reverse('home')}#contacto")

    context = {
        "settings_obj": settings_obj,
        "services": Service.objects.filter(is_active=True),
        "packages": Package.objects.filter(is_active=True),
        "equipment": Equipment.objects.filter(is_active=True, is_featured=True)[:6],
        "gallery": GalleryImage.objects.filter(is_active=True)[:8],
        "testimonials": Testimonial.objects.filter(is_active=True)[:3],
        "faqs": FAQ.objects.filter(is_active=True).exclude(question="Puedo subir fotos desde el panel?"),
        "form": form,
    }
    return render(request, "rental/home.html", context)


def api_site_content(request):
    settings_obj = SiteSettings.objects.filter(is_active=True).order_by("-updated_at").first()
    data = {
        "business": {
            "name": settings_obj.business_name if settings_obj else "Audio Reino Cancun",
            "tagline": settings_obj.tagline if settings_obj else "",
            "city": settings_obj.city if settings_obj else "Cancun, Quintana Roo",
            "phone": settings_obj.phone if settings_obj else "",
            "email": settings_obj.email if settings_obj else "",
        },
        "services": list(Service.objects.filter(is_active=True).values("title", "description", "icon", "order")),
        "packages": [
            {
                "name": package.name,
                "subtitle": package.subtitle,
                "description": package.description,
                "ideal_for": package.ideal_for,
                "price_from": str(package.price_from) if package.price_from else None,
                "includes": package.include_list,
            }
            for package in Package.objects.filter(is_active=True)
        ],
        "faqs": list(
            FAQ.objects.filter(is_active=True)
            .exclude(question="Puedo subir fotos desde el panel?")
            .values("question", "answer", "order")
        ),
    }
    return JsonResponse(data)


@csrf_exempt
@require_http_methods(["POST"])
def api_create_lead(request):
    configured_key = getattr(settings, "PUBLIC_API_KEY", "")
    request_key = request.headers.get("X-API-Key", "")
    if configured_key and request_key != configured_key:
        return JsonResponse({"error": "API key invalida."}, status=403)

    try:
        payload = json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON invalido."}, status=400)

    form = LeadForm(payload)
    if not form.is_valid():
        return JsonResponse({"errors": form.errors}, status=400)

    lead = form.save()
    return JsonResponse({"id": lead.id, "status": "recibido"}, status=201)
