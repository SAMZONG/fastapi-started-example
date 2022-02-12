# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""
from typing import Optional, List
import fastapi
from pydantic import BaseModel
from fastapi import Query, Path

router = fastapi.APIRouter()


class User(BaseModel):
    # user_id: int
    user_name: str
    email: str
    age: int
    is_active: bool
    bio: Optional[str]


users = []


@router.get("/users", response_model=List[User], tags=["users"])
async def get_users():
    return users


@router.post("/users", tags=["users", "items"])
async def create_user(user: User):
    users.append(user)
    return "Success"


@router.get("/users/{id}", tags=["users"],
            summary="This is summary for api.users",
            response_description="This is a response_description")
async def get_user(
        id: int = Path(..., description="The ID of the user you want to get", gt=1),
        q: str = Query(None, max_length=6)
):
    return {"user": users[id], "q": q}


@router.delete("/user/{id}", tags=["items"], deprecated=True)
async def delete_user(id: int = Path(..., description="The ID of the user is you want remove it")):
    """
    - This line 1
    - This line 2
    """
    users.pop(id)
    return "Success"
