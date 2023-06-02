from pydantic import BaseSettings


class EnvSettings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def get_db_URL(self):
        user = f"{self.DB_USER}:{self.DB_PASS}"
        database = f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return f"postgresql+asyncpg://{user}@{database}"

    class Config:
        env_file = ".env"
        _env_file_encoding = "utf-8"


settings = EnvSettings()
print(settings.DB_HOST)
