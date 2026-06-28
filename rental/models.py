from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SiteSettings(TimeStampedModel):
    business_name = models.CharField("nombre del negocio", max_length=120, default="Audio Reino Cancun")
    tagline = models.CharField("frase principal", max_length=180, default="Renta de audio profesional para congregaciones y eventos cristianos")
    city = models.CharField("ciudad base", max_length=80, default="Cancun, Quintana Roo")
    phone = models.CharField("telefono", max_length=30, blank=True)
    whatsapp_number = models.CharField("WhatsApp con lada internacional", max_length=30, blank=True, help_text="Ejemplo: 529981234567")
    email = models.EmailField("correo", blank=True)
    facebook_url = models.URLField("Facebook", blank=True)
    instagram_url = models.URLField("Instagram", blank=True)
    logo = models.ImageField("logo", upload_to="branding/", blank=True, null=True)
    hero_image = models.ImageField("imagen principal", upload_to="hero/", blank=True, null=True)
    primary_cta = models.CharField("boton principal", max_length=60, default="Cotizar por WhatsApp")
    secondary_cta = models.CharField("boton secundario", max_length=60, default="Ver paquetes")
    meta_description = models.CharField("descripcion SEO", max_length=260, blank=True)
    is_active = models.BooleanField("configuracion activa", default=True)

    class Meta:
        verbose_name = "configuracion del sitio"
        verbose_name_plural = "configuracion del sitio"

    def __str__(self):
        return self.business_name


class Service(TimeStampedModel):
    title = models.CharField("titulo", max_length=120)
    description = models.TextField("descripcion")
    icon = models.CharField("icono", max_length=40, default="speaker", help_text="Opciones sugeridas: speaker, users, truck, mic, shield")
    order = models.PositiveIntegerField("orden", default=0)
    is_active = models.BooleanField("activo", default=True)

    class Meta:
        ordering = ["order", "title"]
        verbose_name = "servicio"
        verbose_name_plural = "servicios"

    def __str__(self):
        return self.title


class Equipment(TimeStampedModel):
    name = models.CharField("equipo", max_length=140)
    category = models.CharField("categoria", max_length=80, default="Audio")
    description = models.TextField("descripcion", blank=True)
    image = models.ImageField("imagen", upload_to="equipment/", blank=True, null=True)
    is_featured = models.BooleanField("destacado", default=False)
    is_active = models.BooleanField("activo", default=True)

    class Meta:
        ordering = ["category", "name"]
        verbose_name = "equipo"
        verbose_name_plural = "equipos"

    def __str__(self):
        return self.name


class Package(TimeStampedModel):
    name = models.CharField("paquete", max_length=120)
    subtitle = models.CharField("subtitulo", max_length=160, blank=True)
    description = models.TextField("descripcion")
    ideal_for = models.CharField("ideal para", max_length=180, blank=True)
    price_from = models.DecimalField("precio desde", max_digits=10, decimal_places=2, blank=True, null=True)
    includes = models.TextField("incluye", help_text="Escribe un elemento por linea")
    order = models.PositiveIntegerField("orden", default=0)
    is_active = models.BooleanField("activo", default=True)

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "paquete"
        verbose_name_plural = "paquetes"

    def __str__(self):
        return self.name

    @property
    def include_list(self):
        return [item.strip() for item in self.includes.splitlines() if item.strip()]


class GalleryImage(TimeStampedModel):
    title = models.CharField("titulo", max_length=120)
    image = models.ImageField("imagen", upload_to="gallery/")
    alt_text = models.CharField("texto alternativo", max_length=160, blank=True)
    order = models.PositiveIntegerField("orden", default=0)
    is_active = models.BooleanField("activo", default=True)

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "imagen de galeria"
        verbose_name_plural = "galeria"

    def __str__(self):
        return self.title


class Testimonial(TimeStampedModel):
    name = models.CharField("nombre", max_length=100)
    church_or_event = models.CharField("iglesia o evento", max_length=140, blank=True)
    quote = models.TextField("testimonio")
    is_active = models.BooleanField("activo", default=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "testimonio"
        verbose_name_plural = "testimonios"

    def __str__(self):
        return self.name


class FAQ(TimeStampedModel):
    question = models.CharField("pregunta", max_length=180)
    answer = models.TextField("respuesta")
    order = models.PositiveIntegerField("orden", default=0)
    is_active = models.BooleanField("activo", default=True)

    class Meta:
        ordering = ["order", "question"]
        verbose_name = "pregunta frecuente"
        verbose_name_plural = "preguntas frecuentes"

    def __str__(self):
        return self.question


class Lead(TimeStampedModel):
    EVENT_CHOICES = [
        ("culto", "Culto o reunion"),
        ("congreso", "Congreso"),
        ("concierto", "Concierto cristiano"),
        ("boda", "Boda cristiana"),
        ("otro", "Otro"),
    ]

    name = models.CharField("nombre", max_length=120)
    phone = models.CharField("telefono", max_length=30)
    email = models.EmailField("correo", blank=True)
    event_type = models.CharField("tipo de evento", max_length=30, choices=EVENT_CHOICES, default="culto")
    event_date = models.DateField("fecha del evento", blank=True, null=True)
    location = models.CharField("ubicacion", max_length=160, blank=True)
    message = models.TextField("mensaje")
    was_contacted = models.BooleanField("ya fue contactado", default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "solicitud"
        verbose_name_plural = "solicitudes"

    def __str__(self):
        return f"{self.name} - {self.phone}"
