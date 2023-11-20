from fastapi import APIRouter, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from .models import *
from passlib.context import CryptContext

from fastapi_login import LoginManager
SECRET = 'your-secret-key'


router = APIRouter()
manager = LoginManager(SECRET, token_url='/auth/token')
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
def get_password_hash(password):
    return pwd_context.hash(password)


