from pydantic_settings import  BaseSettings , SettingConficDict


class Settings(BaseSettings):
    APP_NAME:str
    APP_VERSION:str
    APP_API_KEY:str


    class config:
        env_file=".env"

    def get_settings():
        return Settings()

