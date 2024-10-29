from pydantic_settings import  BaseSettings , SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME:str
    APP_VERSION:str
    #APP_API_KEY:str


    class Config:
        env_file="src/.env"

def get_settings():
    return Settings()

