from django.core.management.base import BaseCommand

from rental.models import FAQ, Package, Service, SiteSettings, Testimonial


class Command(BaseCommand):
    help = "Crea contenido inicial editable para la pagina."

    def handle(self, *args, **options):
        SiteSettings.objects.get_or_create(
            is_active=True,
            defaults={
                "business_name": "Audio Reino Cancun",
                "tagline": "Renta de audio profesional para congregaciones y eventos cristianos",
                "city": "Cancun, Quintana Roo",
                "phone": "+52 998 123 4567",
                "whatsapp_number": "529981234567",
                "email": "ventas@audioreino.mx",
                "meta_description": "Renta de audio para iglesias, congresos, conciertos y eventos cristianos en Cancun.",
            },
        )

        services = [
            ("Audio profesional", "Sistemas de bocinas, consola, microfonia y monitoreo configurados para voz y musica.", "sp", 1),
            ("Instalacion incluida", "Montaje limpio, cableado, pruebas de sonido y desmontaje al finalizar el evento.", "in", 2),
            ("Personal tecnico", "Tecnico en sitio para operar niveles, microfonos y musica durante la reunion.", "te", 3),
        ]
        for title, description, icon, order in services:
            Service.objects.get_or_create(title=title, defaults={"description": description, "icon": icon, "order": order})

        packages = [
            (
                "Reunion local",
                "Para grupos pequenos",
                "Solucion practica para reuniones de oracion, estudios o cultos en espacios pequenos.",
                "20 a 80 personas",
                2500,
                "2 bocinas activas\n2 microfonos\nConsola compacta\nInstalacion y pruebas",
                1,
            ),
            (
                "Congregacion",
                "Para cultos y celebraciones",
                "Mayor cobertura, microfonia y soporte tecnico para servicios con musica y predicacion.",
                "80 a 250 personas",
                4800,
                "Sistema principal\nConsola digital\nMicrofonos inalambricos\nPersonal tecnico en sitio",
                2,
            ),
            (
                "Evento especial",
                "Congresos y conciertos",
                "Produccion de audio para eventos cristianos con mayor asistencia y necesidades tecnicas.",
                "250+ personas",
                8900,
                "Sistema de alta potencia\nMonitoreo para plataforma\nMicrofonia multiple\nCoordinacion tecnica",
                3,
            ),
        ]
        for name, subtitle, description, ideal_for, price_from, includes, order in packages:
            Package.objects.get_or_create(
                name=name,
                defaults={
                    "subtitle": subtitle,
                    "description": description,
                    "ideal_for": ideal_for,
                    "price_from": price_from,
                    "includes": includes,
                    "order": order,
                },
            )

        faqs = [
            ("El servicio incluye instalacion?", "Si. Incluye montaje, pruebas y desmontaje. Tambien puedes contratar tecnico durante todo el evento.", 1),
            ("Atienden fuera de Cancun?", "Si, podemos cotizar traslados para Riviera Maya, Playa del Carmen, Puerto Morelos y otros puntos.", 2),
            ("Con cuanta anticipacion debo reservar?", "Lo ideal es reservar con 1 a 2 semanas de anticipacion para asegurar disponibilidad de equipo y personal tecnico.", 3),
        ]
        for question, answer, order in faqs:
            FAQ.objects.get_or_create(question=question, defaults={"answer": answer, "order": order})

        Testimonial.objects.get_or_create(
            name="Ministerio local",
            defaults={
                "church_or_event": "Cancun",
                "quote": "El audio fue claro, llegaron temprano y el equipo tecnico estuvo atento durante todo el servicio.",
            },
        )

        self.stdout.write(self.style.SUCCESS("Contenido inicial creado o verificado."))
