from fastapi import FastAPI
from admin import router as UserRouter
from tortoise.contrib.fastapi import register_tortoise



app = FastAPI()
app.include_router(UserRouter.router)
# app.include_router(apirouter.app, tags=['api'])

register_tortoise(
    app,
    db_url="postgres://postgres:8821@127.0.0.1/buy-for-shop",
    modules={'models': ['admin.models',]},
    generate_schemas=True,
    add_exception_handlers=True
)

