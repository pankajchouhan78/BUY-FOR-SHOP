# to install tortoise : pip install tortoise

from tortoise.models import Model
from tortoise import Tortoise, fields



class Category(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(200, unique=True)
    slug = fields.CharField(200)
    category_image = fields.TextField()
    description = fields.TextField()
    is_active = fields.BooleanField(default=True)
    updated_at = fields.DatetimeField(auto_now=True)
    created_at = fields.DatetimeField(auto_now_add=True)

class SubCategory(Model):
    id = fields.IntField(pk=True)
    category = fields.ForeignKeyField("models.Category", related_name='subcategory', on_delete="CASCADE")
    name = fields.CharField(200, unique=True)
    sub_cate_image = fields.TextField()
    sub_cate_description = fields.TextField()
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

class Brand(Model):
    id = fields.IntField(pk=True)
    brand_name = fields.CharField(200, unique=True)
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)

class Product(Model):
    id = fields.IntField(pk=True)
    product_name = fields.CharField(150)
    manufacturing = fields.CharField(50)
    product_image = fields.TextField()
    video = fields.TextField()
    product_code = fields.IntField()
    model_number = fields.CharField(200)
    description = fields.TextField()
    length = fields.IntField() 
    width = fields.IntField()
    height = fields.IntField()
    weight = fields.FloatField()
    hsn_code = fields.IntField()
    mrp_price = fields.IntField()
    base_price = fields.FloatField()
    offer_price = fields.IntField()
    gst = fields.IntField()
    category = fields.ForeignKeyField("models.Category", related_name="category", on_delete="CASCADE")
    subcategory = fields.ForeignKeyField("models.SubCategory", related_name="subcategory", on_delete="CASCADE")
    brand = fields.ForeignKeyField("models.Brand", related_name="brand", on_delete="CASCADE")
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

class ProductGallaryImages(Model):
    id = fields.IntField(pk=True)
    product = fields.ForeignKeyField("models.Product", related_name="productimage" , on_delete="CASCADE")
    image = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
