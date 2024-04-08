import os


class Settings:
    # Database settings.
    DATABASE_CONNECTIION_URL: str = os.getenv("DATABASE_CONNECTION_URL")


settings = Settings()
