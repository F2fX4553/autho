"""
SIBNA Configuration File - Production Ready
"""

import os
from dotenv import load_dotenv

load_dotenv(override=True)

class Config:
    # Security
    SECRET_KEY = os.environ.get("SECRET_KEY", "change_this_to_a_random_64_char_string")
    OTP_LENGTH = 6
    OTP_EXPIRY: int = int(os.getenv("OTP_EXPIRY", "120"))
    MAX_OTP_ATTEMPTS: int = 5

    JWT_SECRET: str = os.getenv("JWT_SECRET", "super-secret-enterprise-key-do-not-share")
    JWT_EXPIRY_DAYS: int = int(os.getenv("JWT_EXPIRY_DAYS", "30"))

    RESEND_OTP_LIMIT: int = 5
    RESEND_OTP_WINDOW = 1800  # 30 minutes
    RATE_LIMIT_WINDOW = 3600  # seconds
    CHALLENGE_EXPIRY = 300    # 5 minutes

    # Database - PostgreSQL for production, SQLite as fallback
    DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./sibna_prod.db")

    # Redis
    REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/0")

    # SMTP (Gmail)
    SMTP_HOST = "smtp.gmail.com"
    SMTP_PORT = 465
    SMTP_USERNAME = os.environ.get("GMAIL_USER", "your_gmail@gmail.com")
    SMTP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD", "xxxx xxxx xxxx xxxx")
    SMTP_USE_SSL = True
    SMTP_FROM_NAME = "SIBNA"

    # CORS - Set your deployed frontend URLs
    CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "*").split(",")

    # Environment
    DEBUG = os.environ.get("DEBUG", "false").lower() == "true"
    ENVIRONMENT = os.environ.get("ENVIRONMENT", "production")
