# 📘 KATA_PT

## Descripción

**KATA_PT** está basado en la kata del Superviviente Zombie implementado con metodología TDD; permitiendo gestionar partidas, supervivientes y equipos en un entorno postapocalíptico. Utilizamos Django Rest Framework (DRF) para la creación de una API REST, junto con Swagger para la documentación interactiva. 

---

## 🚀 Funcionalidades principales

- **Partidas**: Crea, lista, y gestiona partidas de supervivientes.
- **Supervivientes**: Controla la vida, heridas y niveles de los supervivientes.
- **Equipos**: Administra el equipo que cada superviviente puede llevar.
- **Swagger y Redoc**: Documentación interactiva generada automáticamente.

---

## 🛠️ Configuración del entorno

Sigue estos pasos para configurar el entorno de desarrollo local:

### 1. Crear y activar el entorno virtual
#### 1.1 Crear el entorno virtual
```bash
python -m venv venv

```
#### 1.2 Activar el entorno virutal
#### Windows

```bash
venv\Scripts\activate
```
#### Mac/Linux

```bash
source venv/bin/activate
```
### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```
## 🏃‍♂️ Ejecutar el proyecto

### 1. Migrar la base de datos

```bash
python manage.py migrate
```

### 2. Cerar un superusuario 

```bash
python manage.py createsuperuser
```
### 3. Cerar un superusuario 

```bash
python manage.py runserver
```

## 🧪 Pruebas
### Ejecuta las pruebas para validar el funcionamniento: 
```bash
pytest
```

## 🤓 Flujo de Trabajo

- **1**: Rama principal (main)
- **2**: Rama desarrollo (dev)
- **3**: Rama test (test(KPT-XX))
- **4**: Rama funcionalidades (feat(KPT-XX))
- **5**: Rama refactorización (fix(KPT-XX))

## 👉 Proceso de Trabajo

- **1**: Crear una rama para la funcionalidad: git checkout -b feat-nueva-funcionalidad
- **2**: Realizar commits siguiendo la convención: feat(KPT-XX): descripción.
- **3**: Abrir Pull Request hacia dev
- **4**: Revisar y aprobar cambios antes de fusionar


## 📖 Documentación de la API

### Swagger:
#### Documentación interactiva de la API en:
http://127.0.0.1:8000/api/swagger/

### Redoc:
#### Documentación alternativa: 
http://127.0.0.1:8000/api/redoc/

## ⚡ Próximos pasos

- **4**: Experiencia y niveles
- **5**: Salida 
- **6**: Avance
- **7**: ¡No dejar de aprender nunca! 
