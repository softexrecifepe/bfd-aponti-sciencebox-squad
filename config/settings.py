from pathlib import Path
import os
import subprocess

# Caminho base
BASE_DIR = Path(__file__).resolve().parent.parent

# Segurança
SECRET_KEY = 'django-insecure-trocar-depois'

# Deixe True para debug, mas mude para False quando tudo estiver ok
DEBUG = True 

ALLOWED_HOSTS = ['*']

# =========================
# APPS
# =========================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',

    'apps.core',
    'apps.products',
    'apps.contacts',
]

# =========================
# MIDDLEWARE
# =========================

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # WhiteNoise deve estar aqui!
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# =========================
# URLS / TEMPLATES
# =========================

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'apps/core/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# =========================
# DATABASE
# =========================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# =========================
# INTERNACIONALIZAÇÃO
# =========================

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# =========================
# STATIC FILES (CONFIGURAÇÃO FINAL)
# =========================

STATIC_URL = '/static/'

# Pasta onde seus arquivos originais estão
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Pasta onde o Django vai reunir tudo
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# WhiteNoise Storage - Simplificado para evitar erros de Manifest no Vercel
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
WHITENOISE_USE_MANIFEST_STORAGE = False # Mude para False se os nomes com hash derem erro

# =========================
# MEDIA
# =========================

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ALLOW_ALL_ORIGINS = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.AllowAny']
}

# ==========================================================
# PLANO B: FORÇAR COLLECTSTATIC NO VERCEL
# ==========================================================
if os.environ.get('VERCEL'):
    try:
        print("Ambiente Vercel detectado. Rodando collectstatic...")
        # No Vercel, o comando costuma ser 'python' e não 'python3'
        subprocess.run(['python', 'manage.py', 'collectstatic', '--noinput'])
    except Exception as e:
        print(f"Erro no collectstatic: {e}")