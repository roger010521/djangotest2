# 🧩 Django REST Framework API 

## 🚀 Requisitos

- Python 3.8+
- pip
- Git
- (Opcional) Virtualenv
---

## 🛠️ Instalación local

```bash
# 1. Clonar el repositorio
git clone https://github.com/roger010521/djangotest2.git
cd TU_REPOSITORIO

# 2. Crear y activar entorno virtual (opcional pero recomendado)
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Crear archivo .env si usas variables de entorno
cp .env.example .env

# 5. Migrar la base de datos
python manage.py migrate

# 6. Crear superusuario (opcional)
python manage.py createsuperuser

# 7. Correr el servidor local
python manage.py runserver
