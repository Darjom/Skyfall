# **Skyfall Flask Project**  
_“Because every great mission needs a front… and a backoffice!”_

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)  
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-11%20or%2015-blue)](https://www.postgresql.org/)

## **Overview**

Esta es una arquitectura **Flask** que separa la aplicación en dos módulos:

- **oh_sansi**: Aplicación “front”  
- **backoffice**: Panel administrativo con Flask-Admin y Flask-Security

Ambos comparten la misma lógica de dominio en la carpeta `src/`.

> **¿Por qué “Skyfall”?**  
> Porque, a diferencia de un monolito, **cae** en distintas capas sin colapsar todo el sistema. ¡Más modular, menos drama!

---

## **Table of Contents**
1. [Estructura del Proyecto](#estructura-del-proyecto)
2. [Requisitos Previos](#requisitos-previos)
3. [Instalación y Configuración](#instalación-y-configuración)
4. [Ejecutar la Aplicación](#ejecutar-la-aplicación)
5. [Uso y Comandos Útiles](#uso-y-comandos-útiles)
6. [Checklist de Tareas](#checklist-de-tareas)
7. [Support / Contacto](#support--contacto)
8. [Contribuyendo](#contribuyendo)
9. [Licencia](#licencia)
10. [Estado del Proyecto](#estado-del-proyecto)

---

## **Estructura del Proyecto**

```plaintext
.
├── apps/
│   ├── __init__.py                    # Manejo de extensiones (db, etc.)
│   ├── backoffice/                    # Backoffice app (Flask-Admin, Flask-Security)
│   │   ├── __init__.py
│   │   ├── controllers/
│   │   ├── static/
│   │   └── templates/
│   └── oh_sansi/                      # oh_sansi (front)
│       ├── __init__.py
│       ├── controllers/
│       ├── static/
│       └── templates/
├── src/                               # Lógica de dominio (roles, etc.)
│   └── roles/
│       ├── domain/
│       └── infrastructure/
├── config.py                          # Config con python-decouple
├── run.py                             # Levanta ambas apps (puertos 5000 y 5001)
├── requirements.txt                   # Dependencias
└── .flaskenv --> (Renombrar a .env)   # Variables de entorno
```
**Principales componentes**:
- **`apps/backoffice`**: Panel de administración con seguridad (Flask-Admin + Flask-Security).  
- **`apps/oh_sansi`**: Front-end de la aplicación.  
- **`src/`**: Código de dominio y persistencia (evita mezclar lógica de negocio con vistas).  
- **`run.py`**: Punto de entrada (modo desarrollo) que levanta oh_sansi y backoffice en threads.

---

## **Requisitos Previos**

- [ ] **Python 3.9+**  
- [ ] **PostgreSQL** (versión 11 o 15)  
- [ ] **Git** (para clonar el repo)  
- [ ] Conexión a Internet para instalar dependencias

---

## **Instalación y Configuración**

1. **Clonar el proyecto**:
   ```bash
   git clone https://github.com/Darjom/Skyfall.git
   cd Skyfall
   ```
	2.	**Renombrar .flaskenv a .env**
	•	Abre el archivo .flaskenv y revísalo. Renómbralo a .env.
	•	Ajusta la configuración de tu base de datos PostgreSQL en .env, por ejemplo:
  ```dotenv
  DB_ENGINE=postgresql
  DB_NAME=tis
  DB_HOST=localhost
  DB_PORT=5432
  DB_USERNAME=postgres
  DB_PASS=admin123
  ```
  3. **Crear el entorno virtual (opcional pero recomendado):**
  ```bash
  pip install -r requirements.txt
  ```
  •	Activar el entorno:
	  •	Windows: venv\Scripts\activate
	  •	macOS / Linux: source venv/bin/activate
  4. **Instalar dependencias:**
  Descomentar el  **psycopg2** para usuarios windows y comentar el binary
    ```bash
    pip install -r requirements.txt
    ```
  5.  **Configurar PostgreSQL**
  	•	Crea una base de datos local con el nombre configurado en .env (por defecto **tis**):
  ```sql
    CREATE DATABASE tis;
  ```
---

## Ejecutar la Aplicación

1. **Iniciar en local:**
 ```bash
 python run.py
```
- **Levanta oh_sansi en http://127.0.0.1:5000**
-	**Levanta backoffice en http://127.0.0.1:5001**

2.	Verifica la consola para asegurarte de que ambas apps corren sin errores.
## Uso y Comandos Útiles
	•	Iniciar migraciones con Flask-Migrate (opcional):
  ```bash
  # Solo si deseas track de migraciones
  export FLASK_APP=apps.backoffice:create_backoffice_app
  flask db init
  flask db migrate -m "Initial"
  flask db upgrade
  ```
## **Checklist de Tareas**

- [ ] **Configurar** llaves SSH o tokens (PAT) para hacer push a GitHub.  
- [ ] **Verificar** `.env` con credenciales de PostgreSQL.  
- [ ] **Correr** `python run.py` para el modo local.  
- [ ] **Migrar** la DB si quieres un control de versiones (`flask db migrate` / `flask db upgrade`).  
- [ ] **Crear** tu usuario Admin en `backoffice`.  
- [ ] **Push** cambios con `git push` (recuerda que GitHub no acepta contraseñas, usa SSH o tokens).

---

## **Support / Contacto**

¿Dudas, problemas o sugerencias?  
- [Abrir un “issue” en GitHub](https://github.com/Darjom/Skyfall/issues)  
- Contactar a [Darjom](https://github.com/Darjom) o [JARO-Hub](https://github.com/JARO-Hub)

---

## **Contribuyendo**

¡Las contribuciones son bienvenidas!  
1. **Haz un fork** de este repositorio.  
2. Crea una **feature branch**:
   ```bash
   git checkout -b feature/<tu-feature>
   ```
3.	Commit tus cambios con mensajes claros.
4.	Push a tu fork y crea un Pull Request describiendo tus aportes.
## **Licencia**
Este proyecto está bajo licencia de … (Indica aquí la licencia que uses, e.g. MIT, Apache 2.0, etc.)

