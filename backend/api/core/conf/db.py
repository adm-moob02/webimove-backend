from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="DB_", str_to_upper=True)
    user: str = "localuser"
    password: str = "localpass"
    host: str = "db"
    port: int = 5432
    name: str = "imigraweb"


db_settings = DBSettings()
