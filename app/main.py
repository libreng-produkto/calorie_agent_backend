from fastapi import FastAPI
from app.api.routes import router

def create_app()-> FastAPI:
    app = FastAPI(title='Calorie Assistant API')
    app.include_router(router=router)
    return app

app = create_app()