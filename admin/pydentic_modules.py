# serializer
from pydantic import BaseModel

class CategoryItme(BaseModel):
    name:str
    description:str

class CategoryUpdate(CategoryItme):
    id:int

class CategoryDelete(BaseModel):
    id:int
class SubCategoryItems(BaseModel):
    category_id:int
    name:str
    description:str
class SubCategoryUpdate(BaseModel):
    id:int
    name:str
    description:str
class CubCategorDelete(BaseModel):
    id:int


class BrandItems(BaseModel):
    name:str
class BrandUpdate(BrandItems):
    id:int
class BrandDelete(BaseModel):
    id:int

class ProductItems(BaseModel):
    category_id:int
    subcategory_id:int
    brand_id:int
    product_name:str
    manufacturing:str
    product_code:int
    model_number:str
    description:str
    length:int
    width:int
    height:int
    weight:int
    hsn_code:int
    mrp_price:int
    base_price:int
    offer_price:int
    gst:int