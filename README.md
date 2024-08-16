# Sistema de Gestión de Empleados

Este proyecto es una aplicación web creada con Django para gestionar empleados dentro de una empresa. La interfaz de usuario utiliza plantillas y estilos de Foundation Zurb, proporcionando un diseño moderno y responsivo.
![empleados](https://res.cloudinary.com/dqa2kd0vc/image/upload/v1723770021/screencapture-127-0-0-1-8000-2024-08-15-18_58_50_xwjor9.png)

## Características

- **Gestión de Empleados:** Añadir, editar y eliminar empleados.
- **Gestión de Departamentos:** Administración de los diferentes departamentos de la empresa.
- **Interfaz de Usuario:** Uso de Foundation Zurb para el diseño y la experiencia de usuario.
- **Configuración Modular:** La configuración del proyecto está seccionada en tres archivos diferentes dentro de `empleado/settings` para facilitar la administración y el despliegue.

## Estructura del Proyecto

El proyecto sigue una arquitectura de aplicaciones dentro de Django, con las siguientes aplicaciones locales:

- **Departamento:** Administración de departamentos.
- **Empleados:** Gestión de empleados.
- **Home:** Página principal y vistas generales.
- **Persona:** Gestión de información personal de los empleados.

### Configuración

La configuración del proyecto se divide en tres archivos principales dentro de `empleado/settings`:

1. **`base.py`:** Contiene la configuración base del proyecto, incluyendo las aplicaciones instaladas, middlewares, configuración de plantillas, validación de contraseñas, internacionalización, entre otros. Ejemplo de configuración:

    ```python
    BASE_DIR
    SECRET_KEY
    INSTALLED_APPS 
    MIDDLEWARE 
    ROOT_URLCONF
    TEMPLATES 
    WSGI_APPLICATION
    AUTH_PASSWORD_VALIDATORS
    LANGUAGE_CODE
    TIME_ZONE
    USE_I18N 
    USE_TZ
    DEFAULT_AUTO_FIELD
    ```

2. **`local.py`:** Contiene la configuración para el entorno de desarrollo local, incluyendo la configuración de la base de datos y directorios estáticos.

3. **`prod.py`:** Configuración para el entorno de producción, con detalles para el despliegue, incluyendo configuraciones de seguridad y bases de datos específicas para producción.

## Instalación

1. **Clonar el Repositorio:**

    ```bash
    git clone https://github.com/usuario/nombre-del-repositorio.git
    ```

2. **Crear y Activar un Entorno Virtual:**

    ```bash
    python3 -m venv env
    source env/bin/activate  # En Windows: env\Scripts\activate
    ```

3. **Instalar Dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Aplicar Migraciones:**

    ```bash
    python manage.py migrate
    ```

5. **Iniciar el Servidor:**

    ```bash
    python manage.py runserver
    ```

## Despliegue

Para el despliegue en producción, asegúrate de configurar correctamente el archivo `prod.py` dentro de `empleado/settings` con las variables de entorno adecuadas para tu servidor.
