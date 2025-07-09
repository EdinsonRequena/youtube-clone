import os
from importlib import import_module

env_name = os.getenv("DJANGO_ENV", "local").lower()
module = import_module(f"yclone.settings.{env_name}")

for setting_key in dir(module):
    if setting_key.isupper():
        globals()[setting_key] = getattr(module, setting_key)
