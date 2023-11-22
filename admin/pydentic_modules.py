# serializer

from pydantic import BaseModel


class CategoryItme(BaseModel):
    name:str
    description:str

class CategoryUpdate(CategoryItme):
    id:int

class CategoryDelete(BaseModel):
    id:int