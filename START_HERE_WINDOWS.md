# Empezar en Windows

Si PowerShell muestra este error:

```powershell
pip : El termino 'pip' no se reconoce...
```

significa que Python no esta instalado o no quedo agregado al PATH de Windows.

## 1. Instala Python

Descarga Python desde:

https://www.python.org/downloads/windows/

Durante la instalacion marca esta opcion:

```text
Add python.exe to PATH
```

Luego cierra y vuelve a abrir Visual Studio Code.

## 2. Verifica Python

En la terminal del proyecto ejecuta:

```powershell
python --version
```

Debe salir algo parecido a:

```text
Python 3.12.x
```

Tambien verifica pip:

```powershell
python -m pip --version
```

## 3. Crea el entorno virtual

Desde la carpeta del proyecto:

```powershell
python -m venv .venv
```

Activalo:

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activacion, ejecuta:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Cierra y abre la terminal otra vez, y vuelve a activar:

```powershell
.\.venv\Scripts\Activate.ps1
```

## 4. Instala dependencias

Usa este comando, no `pip` directo:

```powershell
python -m pip install -r requirements.txt
```

## 5. Configura variables

Copia el ejemplo:

```powershell
copy .env.example .env
```

Luego abre `.env` y configura tu base de datos PostgreSQL.

## 6. Levanta PostgreSQL

Si tienes Docker Desktop instalado:

```powershell
docker compose up -d
```

En `.env` puedes usar:

```env
DB_NAME=audio_renta
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

## 7. Prepara Django

```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_content
python manage.py runserver
```

Abre:

```text
http://127.0.0.1:8000/
```

Panel admin:

```text
http://127.0.0.1:8000/admin/
```
