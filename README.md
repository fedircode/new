# Administrador de Datos Multimedia

Este proyecto es una herramienta de línea de comandos para administrar contenido multimedia, incluyendo la subida a diversas plataformas, gestión de bases de datos, generación de previsualizaciones y automatización de tareas relacionadas.

## Características Principales

*   **Subida de Archivos**:
    *   Soporte para subir videos a Voe ([`src/upload/uploader_voe.py`](src/upload/uploader_voe.py)).
    *   Soporte para subir videos a Filemoon ([`src/upload/uploader_filemoon.py`](src/upload/uploader_filemoon.py)).
    *   Subida de imágenes de previsualización a ImageKit ([`src/upload/upload_imagekit.py`](src/upload/upload_imagekit.py) y [`src/portal/portal_imagekit.py`](src/portal/portal_imagekit.py)).
*   **Gestión de Base de Datos (Supabase)**:
    *   Añadir nuevos datos multimedia ([`src/database/add_data.py`](src/database/add_data.py)).
    *   Actualizar datos existentes ([`src/database/update_data.py`](src/database/update_data.py)).
    *   Interacción con la API de Supabase ([`src/api/supabase_api.py`](src/api/supabase_api.py)).
*   **Generación de Contenido**:
    *   Creación de previsualizaciones de imágenes para videos ([`src/utils/prev_img.py`](src/utils/prev_img.py) y [`src/portal/portal_img_prev.py`](src/portal/portal_img_prev.py)).
    *   Generación de plantillas para posts en portales ([`src/portal/post_portal.py`](src/portal/post_portal.py)).
*   **Automatización y Utilidades**:
    *   Reconstrucción de despliegues en Cloudflare ([`src/utils/rebuild.py`](src/utils/rebuild.py)).
    *   Organización de archivos descargados en carpetas estructuradas ([`src/utils/ordenar_carpeta.py`](src/utils/ordenar_carpeta.py)).
    *   Monitorización de la validez de enlaces de Voe ([`src/monitor/test_voe.py`](src/monitor/test_voe.py)).
    *   Registro de actividades ([`src/utils/logger_base.py`](src/utils/logger_base.py)).

## Estructura del Proyecto

```
.
├── .github/workflows/       # Workflows de GitHub Actions
│   ├── rebuild.yml          # Workflow para reconstruir en Cloudflare
│   └── tester_voe.yml       # Workflow para probar enlaces de Voe
├── src/
│   ├── api/                 # Módulos para interactuar con APIs externas (Filemoon, Supabase, Voe)
│   ├── database/            # Scripts para la gestión de la base de datos
│   ├── monitor/             # Scripts para monitorización
│   ├── portal/              # Scripts relacionados con la creación de contenido para portales
│   ├── upload/              # Scripts para la subida de archivos a diferentes plataformas
│   └── utils/               # Scripts de utilidad (generación de previsualizaciones, ordenamiento, etc.)
├── .env                     # Archivo de configuración para variables de entorno (no versionado)
├── main.py                  # Script principal de la aplicación
├── requirements.txt         # Dependencias del proyecto
└── setup.py                 # Script de configuración para el empaquetado
```

## Instalación

1.  Clona el repositorio:
    ```sh
    git clone <url-del-repositorio>
    cd data_manager
    ```
2.  Crea un entorno virtual (recomendado):
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # En Windows: .venv\Scripts\activate
    ```
3.  Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Configuración

Crea un archivo `.env` en la raíz del proyecto y añade las siguientes variables de entorno con tus claves API y configuraciones:

```env
SUPABASE_URL="TU_SUPABASE_URL"
SUPABASE_KEY="TU_SUPABASE_KEY"
API_KEY_VOE="TU_API_KEY_VOE"
API_KEY_FILEMOON="TU_API_KEY_FILEMOON"
CLOUDFLARE_EMAIL="TU_CLOUDFLARE_EMAIL"
CLOUDFLARE_API_KEY="TU_CLOUDFLARE_API_KEY" # O CLOUDFLARE__API_KEY dependiendo del uso
CF_PROJECT_NAME="TU_CF_PROJECT_NAME"
CF_ACCOUNT_ID="TU_CF_ACCOUNT_ID"

# Variables para ImageKit (si son diferentes para portal y monkeysleaks)
IMAGEKIT_PRIVATE_KEY_MONKEYSLEAKS="TU_IMAGEKIT_PRIVATE_KEY"
IMAGEKIT_PUBLIC_KEY_MONKEYSLEAKS="TU_IMAGEKIT_PUBLIC_KEY"
IMAGEKIT_URL_ENDPOINT_MONKEYSLEAKS="TU_IMAGEKIT_URL_ENDPOINT"

IMAGEKIT_PRIVATE_KEY_PORTAL="TU_IMAGEKIT_PRIVATE_KEY_PORTAL"
IMAGEKIT_PUBLIC_KEY_PORTAL="TU_IMAGEKIT_PUBLIC_KEY_PORTAL"
IMAGEKIT_URL_ENDPOINT_PORTAL="TU_IMAGEKIT_URL_ENDPOINT_PORTAL"
```
Asegúrate de que las claves de ImageKit en el código ([`src/upload/upload_imagekit.py`](src/upload/upload_imagekit.py) y [`src/portal/portal_imagekit.py`](src/portal/portal_imagekit.py)) se gestionen también mediante variables de entorno si es necesario.

## Uso

Ejecuta el script principal para acceder al menú de opciones:

```sh
python main.py
```

Sigue las instrucciones en pantalla para seleccionar la operación deseada.

## Workflows de GitHub Actions

*   **Voe Tester** ([`.github/workflows/tester_voe.yml`](.github/workflows/tester_voe.yml)): Se ejecuta diariamente a las 05:00 UTC o manualmente para verificar los enlaces de Voe almacenados en la base de datos y genera un artefacto `fallas.md` con los enlaces rotos.
*   **Rebuild** ([`.github/workflows/rebuild.yml`](.github/workflows/rebuild.yml)): Se puede ejecutar manualmente para disparar una reconstrucción del proyecto en Cloudflare Pages.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un *issue* para discutir cambios importantes o envía un *pull request*.
```// filepath: /home/diego/Escritorio/proyectos/data_manager/README.md
# Administrador de Datos Multimedia

Este proyecto es una herramienta de línea de comandos para administrar contenido multimedia, incluyendo la subida a diversas plataformas, gestión de bases de datos, generación de previsualizaciones y automatización de tareas relacionadas.

## Características Principales

*   **Subida de Archivos**:
    *   Soporte para subir videos a Voe ([`src/upload/uploader_voe.py`](src/upload/uploader_voe.py)).
    *   Soporte para subir videos a Filemoon ([`src/upload/uploader_filemoon.py`](src/upload/uploader_filemoon.py)).
    *   Subida de imágenes de previsualización a ImageKit ([`src/upload/upload_imagekit.py`](src/upload/upload_imagekit.py) y [`src/portal/portal_imagekit.py`](src/portal/portal_imagekit.py)).
*   **Gestión de Base de Datos (Supabase)**:
    *   Añadir nuevos datos multimedia ([`src/database/add_data.py`](src/database/add_data.py)).
    *   Actualizar datos existentes ([`src/database/update_data.py`](src/database/update_data.py)).
    *   Interacción con la API de Supabase ([`src/api/supabase_api.py`](src/api/supabase_api.py)).
*   **Generación de Contenido**:
    *   Creación de previsualizaciones de imágenes para videos ([`src/utils/prev_img.py`](src/utils/prev_img.py) y [`src/portal/portal_img_prev.py`](src/portal/portal_img_prev.py)).
    *   Generación de plantillas para posts en portales ([`src/portal/post_portal.py`](src/portal/post_portal.py)).
*   **Automatización y Utilidades**:
    *   Reconstrucción de despliegues en Cloudflare ([`src/utils/rebuild.py`](src/utils/rebuild.py)).
    *   Organización de archivos descargados en carpetas estructuradas ([`src/utils/ordenar_carpeta.py`](src/utils/ordenar_carpeta.py)).
    *   Monitorización de la validez de enlaces de Voe ([`src/monitor/test_voe.py`](src/monitor/test_voe.py)).
    *   Registro de actividades ([`src/utils/logger_base.py`](src/utils/logger_base.py)).

## Estructura del Proyecto

```
.
├── .github/workflows/       # Workflows de GitHub Actions
│   ├── rebuild.yml          # Workflow para reconstruir en Cloudflare
│   └── tester_voe.yml       # Workflow para probar enlaces de Voe
├── src/
│   ├── api/                 # Módulos para interactuar con APIs externas (Filemoon, Supabase, Voe)
│   ├── database/            # Scripts para la gestión de la base de datos
│   ├── monitor/             # Scripts para monitorización
│   ├── portal/              # Scripts relacionados con la creación de contenido para portales
│   ├── upload/              # Scripts para la subida de archivos a diferentes plataformas
│   └── utils/               # Scripts de utilidad (generación de previsualizaciones, ordenamiento, etc.)
├── .env                     # Archivo de configuración para variables de entorno (no versionado)
├── main.py                  # Script principal de la aplicación
├── requirements.txt         # Dependencias del proyecto
└── setup.py                 # Script de configuración para el empaquetado
```

## Instalación

1.  Clona el repositorio:
    ```sh
    git clone <url-del-repositorio>
    cd data_manager
    ```
2.  Crea un entorno virtual (recomendado):
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # En Windows: .venv\Scripts\activate
    ```
3.  Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Configuración

Crea un archivo `.env` en la raíz del proyecto y añade las siguientes variables de entorno con tus claves API y configuraciones:

```env
SUPABASE_URL="TU_SUPABASE_URL"
SUPABASE_KEY="TU_SUPABASE_KEY"
API_KEY_VOE="TU_API_KEY_VOE"
API_KEY_FILEMOON="TU_API_KEY_FILEMOON"
CLOUDFLARE_EMAIL="TU_CLOUDFLARE_EMAIL"
CLOUDFLARE_API_KEY="TU_CLOUDFLARE_API_KEY" # O CLOUDFLARE__API_KEY dependiendo del uso
CF_PROJECT_NAME="TU_CF_PROJECT_NAME"
CF_ACCOUNT_ID="TU_CF_ACCOUNT_ID"

# Variables para ImageKit (si son diferentes para portal y monkeysleaks)
IMAGEKIT_PRIVATE_KEY_MONKEYSLEAKS="TU_IMAGEKIT_PRIVATE_KEY"
IMAGEKIT_PUBLIC_KEY_MONKEYSLEAKS="TU_IMAGEKIT_PUBLIC_KEY"
IMAGEKIT_URL_ENDPOINT_MONKEYSLEAKS="TU_IMAGEKIT_URL_ENDPOINT"

IMAGEKIT_PRIVATE_KEY_PORTAL="TU_IMAGEKIT_PRIVATE_KEY_PORTAL"
IMAGEKIT_PUBLIC_KEY_PORTAL="TU_IMAGEKIT_PUBLIC_KEY_PORTAL"
IMAGEKIT_URL_ENDPOINT_PORTAL="TU_IMAGEKIT_URL_ENDPOINT_PORTAL"
```
Asegúrate de que las claves de ImageKit en el código ([`src/upload/upload_imagekit.py`](src/upload/upload_imagekit.py) y [`src/portal/portal_imagekit.py`](src/portal/portal_imagekit.py)) se gestionen también mediante variables de entorno si es necesario.

## Uso

Ejecuta el script principal para acceder al menú de opciones:

```sh
python main.py
```

Sigue las instrucciones en pantalla para seleccionar la operación deseada.

## Workflows de GitHub Actions

*   **Voe Tester** ([`.github/workflows/tester_voe.yml`](.github/workflows/tester_voe.yml)): Se ejecuta diariamente a las 05:00 UTC o manualmente para verificar los enlaces de Voe almacenados en la base de datos y genera un artefacto `fallas.md` con los enlaces rotos.
*   **Rebuild** ([`.github/workflows/rebuild.yml`](.github/workflows/rebuild.yml)): Se puede ejecutar manualmente para disparar una reconstrucción del proyecto en Cloudflare Pages.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un *issue* para discutir cambios importantes o envía un *pull request*.