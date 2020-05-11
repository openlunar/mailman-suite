import random

################################################################################
# Install file for webapp.  Mostly this generates a new SECRET_KEY for Django.
#
# TODO:  This really should generate random passwords for Mailman and Postgres.
################################################################################

LOCAL_SETTINGS_FILE = "local_settings.py"

print(("Writing %s" % LOCAL_SETTINGS_FILE))
new_secret = ''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50))
with open(LOCAL_SETTINGS_FILE, 'w') as settings_file:
    settings_file.writelines(f"SECRET_KEY = '{new_secret}'\n")
    settings_file.writelines("\n")
    settings_file.writelines("# Mailman API Credentials\n")
    settings_file.writelines("MAILMAN_REST_API_URL = 'http://localhost:8001'\n")
    settings_file.writelines("MAILMAN_REST_API_USER = 'admin'\n")
    settings_file.writelines("MAILMAN_REST_API_PASS = '5eHfDgEn'\n")
    settings_file.writelines("MAILMAN_ARCHIVER_KEY = 'p7PQASwe4JysG8yT'\n")
    settings_file.writelines("MAILMAN_ARCHIVER_FROM = ('127.0.0.1', '::1')\n")
    settings_file.writelines("\n")
    settings_file.writelines("# Database Credentials\n")
    settings_file.writelines("DATABASES = {\n")
    settings_file.writelines("    'default': {\n")
    settings_file.writelines("       'ENGINE': 'django.db.backends.postgresql_psycopg2',\n")
    settings_file.writelines("       'NAME': 'mailman-webapp-db',\n")
    settings_file.writelines("       'USER': 'mailman',\n")
    settings_file.writelines("       'HOST': 'localhost',\n")
    settings_file.writelines("       'PASSWORD': 'j2AheVGC',\n")
    settings_file.writelines("    }\n")
    settings_file.writelines("}\n")
