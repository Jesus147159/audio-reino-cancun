from django.db import migrations


def replace_panel_faq(apps, schema_editor):
    FAQ = apps.get_model("rental", "FAQ")
    FAQ.objects.filter(question="Puedo subir fotos desde el panel?").update(
        question="Con cuanta anticipacion debo reservar?",
        answer="Lo ideal es reservar con 1 a 2 semanas de anticipacion para asegurar disponibilidad de equipo y personal tecnico.",
    )


def restore_panel_faq(apps, schema_editor):
    FAQ = apps.get_model("rental", "FAQ")
    FAQ.objects.filter(question="Con cuanta anticipacion debo reservar?").update(
        question="Puedo subir fotos desde el panel?",
        answer="Si. El panel de administradores permite actualizar logo, imagen principal, galeria y equipos.",
    )


class Migration(migrations.Migration):
    dependencies = [
        ("rental", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(replace_panel_faq, restore_panel_faq),
    ]
