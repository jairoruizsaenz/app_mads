::: Instalar aplicación en settings.py 
-----------------------------------------------------------------------------------------
Agregar 'accounts.apps.AccountsConfig', en INSTALLED_APPS

::: Incluir en settings.py
-----------------------------------------------------------------------------------------
AUTH_USER_MODEL = 'accounts.CustomUser'

# LOGIN_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = 'persuasivo_app:index'
LOGOUT_REDIRECT_URL = 'persuasivo_app:index'

# Used for debug, it saves the emails as files in the "sent_files" folder
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")

'''
# Gmail SMTP server
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
#EMAIL_USE_SSL = True
#EMAIL_PORT = 465
EMAIL_HOST_USER = 'your_account@gmail.com'
EMAIL_HOST_PASSWORD = 'your_accounts password'
'''