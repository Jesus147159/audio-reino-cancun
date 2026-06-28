# Publicar el proyecto

## Importante sobre GitHub Pages

GitHub Pages no ejecuta Django, Python ni PostgreSQL. Solo publica HTML, CSS y JavaScript estatico.

Este proyecto necesita:

- Django
- PostgreSQL
- Panel admin
- Carga de imagenes
- Formularios y API

Por eso, GitHub Pages no sirve para publicar la version completa.

## Ruta recomendada

Usa GitHub para guardar el codigo y un hosting para ejecutar Django:

- GitHub: repositorio del proyecto.
- Render, Railway, Fly.io, DigitalOcean o VPS: servidor Django.
- PostgreSQL administrado: base de datos.
- Dominio propio: conectado al hosting.

## Pasos para subir a GitHub

1. Instala Git:

   https://git-scm.com/download/win

2. Crea una cuenta en GitHub:

   https://github.com/

3. Crea un repositorio nuevo, por ejemplo:

   ```text
   audio-reino-cancun
   ```

4. En la terminal del proyecto ejecuta:

   ```powershell
   git init
   git add .
   git commit -m "Primer version del sitio Django"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/audio-reino-cancun.git
   git push -u origin main
   ```

## No subir archivos privados

El archivo `.env` no debe subirse a GitHub. Ya esta protegido por `.gitignore`.

Tampoco subas:

- `.venv/`
- `media/` si contiene archivos privados
- contrasenas
- claves API reales

## Publicar Django en Render

1. Entra a:

   https://render.com/

2. Crea un nuevo `Web Service`.
3. Conecta tu repositorio de GitHub.
4. Configura:

   ```text
   Build Command:
   bash build.sh

   Start Command:
   gunicorn config.wsgi:application
   ```

5. Agrega variables de entorno:

   ```env
   SECRET_KEY=una-clave-larga-y-segura
   DEBUG=False
   ALLOWED_HOSTS=tu-dominio.com,www.tu-dominio.com,tu-app.onrender.com
   CSRF_TRUSTED_ORIGINS=https://tu-dominio.com,https://www.tu-dominio.com,https://tu-app.onrender.com
   DB_NAME=...
   DB_USER=...
   DB_PASSWORD=...
   DB_HOST=...
   DB_PORT=5432
   DATABASE_URL=...
   WHATSAPP_NUMBER=529981234567
   CONTACT_EMAIL=ventas@tudominio.com
   PUBLIC_API_KEY=una-clave-segura
   ```

6. Crea una base PostgreSQL en Render y copia sus datos a las variables `DB_*`.

## Dominio

Cuando el hosting ya funcione, conecta tu dominio desde el panel del proveedor. Normalmente te dara un registro `CNAME` o `A` para configurar donde compraste el dominio.

## Si quieres usar GitHub Pages de todos modos

Solo seria para una version estatica sin:

- panel admin
- formularios reales
- base de datos
- API
- carga de imagenes desde administrador

Para este negocio, no es la opcion recomendada.
