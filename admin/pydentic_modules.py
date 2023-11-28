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