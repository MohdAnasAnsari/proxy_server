# src/config.py

import os

SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("No SECRET_KEY set for the application")
