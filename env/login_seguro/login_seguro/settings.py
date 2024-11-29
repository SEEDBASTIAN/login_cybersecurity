"""
Django settings for login_seguro project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4eld6^!$@r7zr949g-e(spvo_8733fl&&agraqy)1i2pk9k^(t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'mfa',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'login_seguro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'login_seguro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL='users.CustomUser'

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
]

INSTALLED_APPS += ['axes',]
MIDDLEWARE += ['axes.middleware.AxesMiddleware',]
AXES_FAILURE_LIMIT = 5
AXES_COOLOFF_TIME = 1  # 1 hora



# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from django.conf.global_settings import PASSWORD_HASHERS as DEFAULT_PASSWORD_HASHERS #Preferably at the same place where you import your other modules

MFA_UNALLOWED_METHODS=()   # Methods that shouldn't be allowed for the user e.g ('TOTP','U2F',)
MFA_LOGIN_CALLBACK=""      # A function that should be called by username to login the user in session
MFA_RECHECK=True           # Allow random rechecking of the user
MFA_REDIRECT_AFTER_REGISTRATION="mfa_home"   # Allows Changing the page after successful registeration
MFA_SUCCESS_REGISTRATION_MSG = "Go to Security Home" # The text of the link
MFA_RECHECK_MIN=10         # Minimum interval in seconds
MFA_RECHECK_MAX=30         # Maximum in seconds
MFA_QUICKLOGIN=True        # Allow quick login for returning users by provide only their 2FA
MFA_ALWAYS_GO_TO_LAST_METHOD = False # Always redirect the user to the last method used to save a click (Added in 2.6.0).
MFA_RENAME_METHODS={} #Rename the methods in a more user-friendly way e.g {"RECOVERY":"Backup Codes"} (Added in 2.6.0)
MFA_HIDE_DISABLE=('FIDO2',)     # Can the user disable his key (Added in 1.2.0).
MFA_OWNED_BY_ENTERPRISE = False   # Who owns security keys   
PASSWORD_HASHERS = DEFAULT_PASSWORD_HASHERS # Comment if PASSWORD_HASHER already set in your settings.py
PASSWORD_HASHERS += ['mfa.recovery.Hash'] 
RECOVERY_ITERATION = 350000 #Number of iteration for recovery code, higher is more secure, but uses more resources for generation and check...

TOKEN_ISSUER_NAME="PROJECT_NAME"      #TOTP Issuer name

U2F_APPID="https://localhost"    #URL For U2F
FIDO_SERVER_ID=u"localehost"      # Server rp id for FIDO2, it is the full domain of your project
FIDO_SERVER_NAME=u"PROJECT_NAME"

import mfa
MFA_FIDO2_RESIDENT_KEY = mfa.ResidentKey.DISCOURAGED  # Resident Key allows a special User Handle
MFA_FIDO2_AUTHENTICATOR_ATTACHMENT = None  # Let the user choose
MFA_FIDO2_USER_VERIFICATION = None         # Verify User Presence
MFA_FIDO2_ATTESTATION_PREFERENCE = mfa.AttestationPreference.NONE

MFA_ENFORCE_EMAIL_TOKEN = False          # If you want the user to receive OTP by email without enrolling, if this the case, the system admins shall make sure that emails are valid.
MFA_SHOW_OTP_IN_EMAIL_SUBJECT = False    #If you like to show the OTP in the email subject
MFA_OTP_EMAIL_SUBJECT= "OTP"       # The subject of the email after the token