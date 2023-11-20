# to install tortoise : pip install tortoise

from tortoise.models import Model
from tortoise import Tortoise, fields
from datetime import datetime


class Category(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(200, unique=True)
    slug = fields.CharField(200)
    category_image = fields.TextField()
    description = fields.TextField()
    is_active = fields.BooleanField(default=True)
    updated_at = fields.DatetimeField(auto_now=True)
    created_at = fields.DatetimeField(auto_now_add=True)

