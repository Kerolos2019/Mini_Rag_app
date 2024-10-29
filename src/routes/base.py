from fastapi import FastAPI,APIRouter,Depends
import os
from src.helpers.config import get_settings,Settings

base_router=APIRouter()

@base_router.get("/")
def welcome(app_settings:Settings=Depends(get_settings)):
    
    app_name=app_settings.APP_NAME
    app_version=app_settings.APP_VERSION



    return {
        "app_name":app_name ,
        "app_version":app_version
    }
