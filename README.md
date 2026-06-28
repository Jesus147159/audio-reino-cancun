# Audio Reino Cancun - Django + PostgreSQL

Proyecto base para una pagina profesional de renta de equipos de audio para congregaciones cristianas y eventos cristianos en Cancun, Mexico.

## Que incluye

- Pagina principal responsiva para movil, tablet y escritorio.
- Panel administrativo en `/admin/`.
- Contenido editable: marca, logo, imagen principal, servicios, paquetes, equipos, galeria, testimonios, preguntas frecuentes y solicitudes.
- Formulario de cotizacion que guarda solicitudes en PostgreSQL.
- Redireccion opcional a WhatsApp con mensaje armado automaticamente.
- API basica para integraciones futuras.
- Configuracion preparada para produccion con variables de entorno.

## Requisitos

Instala en tu computadora:

- Python 3.12 o superior.
- PostgreSQL 16 o superior.
- Git, recomendado para subir el proyecto a GitHub.
- Docker Desktop, opcional si quieres levantar PostgreSQL facil.

## Instalacion paso a paso

Abre una terminal dentro de esta carpeta:

```powershell
cd C:\Users\jesus\Documents\Codex\2026-06-28\n\outputs\cristianos_audio_rental
```

Crea y activa un entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

Instala dependencias:

```powershell
pip install -r requirements.txt
```

Copia el archivo de variables:

```powershell
copy .env.example .env
```

Edita `.env` y cambia:

- `SECRET_KEY`
- `DB_PASSWORD`
- `WHATSAPP_NUMBER`
- `CONTACT_EMAIL`
- `PUBLIC_API_KEY`

## Base de datos PostgreSQL

Opcion A, con Docker:

```powershell
docker compose up -d
```

Usa en `.env`:

```env
DB_NAME=audio_renta
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

Opcion B, con PostgreSQL instalado normal:

1. Crea una base de datos llamada `audio_renta`.
2. Crea o usa un usuario de PostgreSQL.
3. Actualiza los datos en `.env`.

## Primer arranque

Ejecuta migraciones:

```powershell
python manage.py migrate
```

Crea tu usuario administrador:

```powershell
python manage.py createsuperuser
```

Carga contenido inicial:

```powershell
python manage.py seed_content
```

Inicia el servidor:

```powershell
python manage.py runserver
```

Abre:

- Sitio publico: http://127.0.0.1:8000/
- Panel admin: http://127.0.0.1:8000/admin/

## Como actualizar la pagina

Entra a `/admin/` con tu usuario administrador.

Puedes editar:

- `Configuracion del sitio`: nombre, slogan, telefono, WhatsApp, correo, logo e imagen principal.
- `Servicios`: textos de las tarjetas de servicio.
- `Paquetes`: paquetes, precios y lista de lo que incluye.
- `Equipos`: inventario destacado con imagenes.
- `Galeria`: fotos de eventos o montajes.
- `Testimonios`: comentarios de clientes.
- `Preguntas frecuentes`: preguntas y respuestas.
- `Solicitudes`: leads que llegan desde el formulario.

## API basica

Una API permite que otro sistema lea o envie datos a tu pagina.

Este proyecto trae dos endpoints:

### Leer contenido publico

```http
GET /api/site/
```

Devuelve servicios, paquetes, preguntas frecuentes y datos principales del negocio en JSON.

### Crear una solicitud

```http
POST /api/leads/
X-API-Key: tu_PUBLIC_API_KEY
Content-Type: application/json
```

Ejemplo:

```json
{
  "name": "Juan Perez",
  "phone": "9981234567",
  "email": "juan@example.com",
  "event_type": "congreso",
  "event_date": "2026-08-15",
  "location": "Cancun Centro",
  "message": "Necesito audio para 250 personas."
}
```

La API guarda la solicitud y responde:

```json
{
  "id": 1,
  "status": "recibido"
}
```

## Que falta antes de publicarla

- Comprar dominio, por ejemplo `tumarca.mx`.
- Contratar hosting compatible con Django y PostgreSQL.
- Subir fotos reales de tus equipos y eventos.
- Cambiar textos y precios definitivos.
- Configurar correo transaccional si quieres recibir emails automaticos.
- Activar HTTPS en produccion.
- Poner `DEBUG=False` en produccion.

## Recomendacion de despliegue

Para empezar, usa un proveedor que soporte Python/Django y PostgreSQL, por ejemplo Render, Railway, Fly.io, DigitalOcean o un VPS. Para un negocio real, PostgreSQL administrado y backups automaticos son buena idea.

Variables importantes en produccion:

```env
DEBUG=False
ALLOWED_HOSTS=tudominio.com,www.tudominio.com
CSRF_TRUSTED_ORIGINS=https://tudominio.com,https://www.tudominio.com
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

## Siguiente etapa sugerida

La base ya esta pensada para crecer. Las mejoras naturales son: pagos de anticipo, calendario de disponibilidad, cotizador por numero de asistentes, correos automaticos, integracion con Google Analytics y panel de reportes.
