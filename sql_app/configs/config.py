import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_env: str = 'dev'
    app_name: str = "Awesome API"
    admin_email: str
    items_per_user: int = 50

    class Config:
        if os.getenv("ENV_STATE") is None:
           env_file = '.env'
        else:
           env_file = f'{os.getenv("ENV_STATE")}.env'