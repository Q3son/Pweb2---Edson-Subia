# Tarea Django01 - Programación Web 2

# 📝 Sistema de Gestión de Contactos - Django

![Django Version](https://img.shields.io/badge/django-5.2-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)

Aplicación web para gestión de contactos desarrollada como parte de la **Tarea Django01** del curso de Programación Web 2 en la Universidad Nacional de San Agustín.

## 🌟 Características Principales

- **Panel de Administración Personalizado**
  - Visualización de campos clave (nombre, email, teléfono)
  - Filtros por fecha y estado
  - Formato de fechas personalizado
- **Modelo de Contactos Completo**
  - Campos: nombre, email (único), teléfono, dirección, fecha_registro
  - Validaciones automáticas
- **Interacción con Django Shell**
  - Creación y consulta de contactos mediante ORM

## 🛠️ Tecnologías Utilizadas

- ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
- ![Django](https://img.shields.io/badge/-Django-092E20?logo=django&logoColor=white)
- ![SQLite](https://img.shields.io/badge/-SQLite-003B57?logo=sqlite&logoColor=white)

## 🚀 Instalación Local

### Requisitos Previos

- Python 3.11+
- pip

### Pasos de Configuración

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/django-tarea1.git
   cd django-tarea1
   ```

2. Configurar entorno virtual:

   ```
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   ```
3. Instalar dependencias:

   ```
   pip install -r requirements.txt
   ```
4. Configuración inicial:

   ```
   python manage.py migrate
   python manage.py createsuperuser
   ```

## 🖥️ Uso del Sistema

### Panel de Administración

Accede al panel en `http://localhost:8000/admin` y gestiona tus contactos con:

* Creación/edición individual
* Búsqueda por nombre o email
* Filtros avanzados

### Consola Django

Ejemplos de uso con Django Shell:

```
from personas.models import Contacto
# Crear nuevo contacto
Contacto.objects.create(nombre="Ejemplo", email="ejemplo@test.com")
# Consultar contactos activos
Contacto.objects.filter(activo=True)
```

## 📂 Estructura del Proyecto

```
django-tarea1/
├── listaContactos/       # Configuración principal
│   ├── settings.py       # Configuración (idioma, zona horaria)
│   └── urls.py           # Rutas principales
├── personas/            # App de contactos
│   ├── models.py        # Modelo Contacto
│   ├── admin.py         # Panel admin personalizado
│   └── views.py         # Lógica de vistas
├── manage.py
└── README.md
```

## 📝 Historial de Desarrollo

| Cambio Significativo             | Archivos Modificados       |
| -------------------------------- | -------------------------- |
| Creación del modelo Contacto    | personas/models.py         |
| Personalización del panel admin | personas/admin.py          |
| Configuración de zona horaria   | listaContactos/settings.py |

## 🤝 Contribución

1. Haz fork del proyecto
2. Crea tu rama (`git checkout -b feature/nueva-funcionalidad`)
3. Haz commit de tus cambios (`git commit -m 'feat: Nueva funcionalidad'`)
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

MIT © [Subia Huaicane Edson Fabricio] - Universidad Nacional de San Agustín

## ❓FAQS

```
### ¿Cómo cambiar la configuración regional?
Edita `LANGUAGE_CODE` y `TIME_ZONE` en `listaContactos/settings.py`
```
