# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""

from fastapi import FastAPI

from api.users import router

from db.db_setup import engine
from db.models import user

user.Base.metadata.create_all(bind=engine)

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

app = FastAPI(
    openapi_url="/api/v1/openapi.json",
    # docs_url="/documentation",
    redoc_url=None,
    openapi_tags=tags_metadata,
    title="user example",
    description="A demo project of user example",
    version="1.0",
    terms_of_service="https://samzong.me",
    contact={
        "name": "Alex",
        "url": "https://samzong.me",
        "email": "samzong.lu@gmail.com"
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
    },
)

app.include_router(router)


@app.get("/")
async def homepage():
    return {"message": "Hello World"}
