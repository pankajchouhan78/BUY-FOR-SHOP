from fastapi import APIRouter, Request, Form, status, Depends, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from .models import Category, SubCategory, Brand
from passlib.context import CryptContext
from .pydentic_modules import CategoryItme, CategoryUpdate, CategoryDelete, SubCategoryItems, SubCategoryUpdate, CubCategorDelete, BrandItems, BrandUpdate, BrandDelete

# pip install slugify
from slugify import slugify

from fastapi_login import LoginManager
SECRET = 'your-secret-key'

import os
from datetime import datetime

router = APIRouter()

manager = LoginManager(SECRET, token_url='/auth/token')
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
def get_password_hash(password):
    return pwd_context.hash(password)

@router.post('/category/')
async def create_category(data:CategoryItme=Depends(),
                          category_image:UploadFile = File(...)):
    # validation
    if await Category.exists(name=data.name):
        return {"status":False,"message":"Category Already Exists"}
    else:
        name=data.name
        # Convert the name to a string if it's not already
        if not isinstance(name, str):
            name=str(name)
        slug = slugify(name)

        FILEPATH = "static/images/category/"

        # Ensure the directory exists, create it if it doesn't
        os.makedirs(FILEPATH, exist_ok=True)

        filename=category_image.filename
        image_name = filename.split(".")[0]
        extension = filename.split(".")[1]

        if extension not in ['png', 'jpg','jpeg']:
            return {'status':False, 'message':"Invalid file type"}
        
        dt = datetime.now()
        dt_timestamp = round(datetime.timestamp(dt))

        modify_image_name = image_name + "_" + str(dt_timestamp) + "." + extension

        generated_name = FILEPATH + modify_image_name
        file_content = await category_image.read()
        with open(generated_name,'wb') as file:
            file.write(file_content)
            file.close()

        category_obj = await Category.create(category_image=generated_name,
                                             name=data.name,
                                             description=data.description,
                                             slug=slug)
        return category_obj
    
@router.get('/category/')
async def get_category():
    data = await Category.all()
    return data
    

@router.put('/category/')
async def update_category(data:CategoryUpdate=Depends(),
                         category_image:UploadFile=File(...)):
    
    name=data.name
    if not isinstance(name, str):
        name=str(name)
    slug = slugify(name)

    FILE_PATH = "static/images/category/"
    os.makedirs(FILE_PATH, exist_ok=True)

    file_name=category_image.filename
    image_name = file_name.split('.')[0]
    extenstion = file_name.split('.')[1]

    if extenstion not in ['png','jpg','jpeg']:
        return {"status":False,"message":"Invalid File Type"}
    
    dt = datetime.now()
    # print("dt is :",dt)
    dt_timestamp = round(datetime.timestamp(dt))
    # print("time stamp is ",dt_timestamp)

    modify_image_name = image_name + "_" + str(dt_timestamp) + "." + extenstion
    generated_name = FILE_PATH + modify_image_name
    file_content = await category_image.read()
    # print("file content is ", file_content)

    with open(generated_name, 'bw') as file:
        file.write(file_content)
        file.close()

    category_obj = await Category.filter(id=data.id).update(
        category_image=generated_name,
        name=data.name,
        description=data.description,
        slug=slug,
    )
    return category_obj

@router.delete('/category/')
async def delete_category(data:CategoryDelete):
    if await Category.exists(id=data.id):
        category_obj = await Category.get(id=data.id)
        await category_obj.delete()
        return category_obj
    else:
        return {"status":False,"message":"Invalid ID"}   
@router.post('/subcategory/')
async def create_subcategory(data:SubCategoryItems=Depends(),
                             sub_cate_image:UploadFile=File(...)):
    if await Category.exists(id=data.category_id):
        category_obj = await Category.get(id=data.category_id)
        print (category_obj)

        if await SubCategory.exists(name = data.name):
            return {"status":False, "message":"Sub-Category Already Exists"}
        else:

            FILEPATH = "static/images/subcategory/"
            os.makedirs(FILEPATH, exist_ok=True)

            file_name = sub_cate_image.filename
            image_name = file_name.split('.')[0]
            extension = file_name.split('.')[1]

            if extension not in ['png','jpg','jpeg']:
                return {"status":False,"message":"Invalid File Type"}
            
            dt = datetime.now()
            dt_timestamp = round(datetime.timestamp(dt))

            modify_image_name = image_name + "_" + str(dt_timestamp) + "." + extension
            generated_name = FILEPATH + modify_image_name
            file_content = await sub_cate_image.read()

            with open(generated_name, 'bw') as file:
                file.write(file_content)
                file.close()

            sub_cate_obj = await SubCategory.create(
                category = category_obj,
                sub_cate_image = generated_name,
                name = data.name,
                sub_cate_description = data.description,
            )
            return sub_cate_obj
    else:
        return {"status":False,"message":"Invalid Category ID"}
@router.get('/subcategory/')
async def get_subcategory():
    subcategory_obj = await SubCategory.all()
    return subcategory_obj
@router.put("/subcategory/")
async def update_subcategory(data:SubCategoryUpdate = Depends(),
                            sub_cate_image:UploadFile = File(...)):
    if await SubCategory.exists(id=data.id):
        FILEPATH = "static/images/subcategory/"
        os.makedirs(FILEPATH, exist_ok=True)

        file_name = sub_cate_image.filename
        image_name = file_name.split('.')[0]
        extention = file_name.split('.')[1]

        if extention not in ['png','jpg','jpeg']:
            return {"status":False, "message":"Invalid File Type"}
        
        dt = datetime.now()
        dt_timestamp = round(datetime.timestamp(dt))
        
        modify_image_name = image_name + "_" + str(dt_timestamp) + "." + extention
        generated_name = FILEPATH + modify_image_name
        file_content = await sub_cate_image.read()

        with open(generated_name, 'wb') as file:
            file.write(file_content)
            file.close()

        subcategory_obj = await SubCategory.filter(id=data.id).update(
            sub_cate_image = generated_name,
            name = data.name,
            sub_cate_description = data.description,
        )
        return subcategory_obj
    else:
        return {"status":False, "message":"Invalid Subcategory ID"}  
@router.delete('/subcategory/')
async def delete_subcategory(data:CubCategorDelete=Depends()):
    if await SubCategory.exists(id=data.id):
        subcategory_obj = await SubCategory.filter(id=data.id).delete()
        return {"status":True, "obj":subcategory_obj, "message":"Subcategory successfully deleted"}
    else:
        return {"status":False, "message":"Invalid Subcategory ID"}
    
@router.post('/brand/')
async def create_brand(data:BrandItems):
    # brand_obj = await Brand.create(**data.__dict__)
    if await Brand.exists(brand_name=data.name):
        return {"status":False, "message":"Brand Name Already Exists"}
    else:
        brand_obj = await Brand.create(brand_name=data.name)
        return brand_obj

@router.get('/brand/')
async def get_brand():
    brands = await Brand.all()
    return brands

@router.put('/brand/')
async def update_brand(data:BrandUpdate):
    if await Brand.exists(id=data.id):
        brand_obj = await Brand.filter(id=data.id).update(brand_name=data.name)
        return brand_obj
    else:
        return {"status":False, "message":"Invalid Brand ID"}
    
@router.delete('/brand/')
async def delete_brand(data:BrandDelete):
    if await Brand.exists(id=data.id):
        await Brand.filter(id=data.id).delete()
        return {"status":True,"message":"Brand Successfull Deleted"}
    else:
        return {"status":False, "message":"Invalid Brand ID"}
    