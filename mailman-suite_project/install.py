import random

LOCAL_SETTINGS_FILE = "settings_local.py"

print(("Writing %s" % LOCAL_SETTINGS_FILE))
new_secret = ''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50))
with open(LOCAL_SETTINGS_FILE, 'w') as f:
    f.writelines(f'SECRET_KEY="{new_secret}"')
