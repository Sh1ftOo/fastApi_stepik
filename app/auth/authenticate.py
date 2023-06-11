from datetime import datetime, timedelta

from fastapi import HTTPException, status
from pydantic import EmailStr

from app.users.dao import UsersDao
from .password_manager import verify_password, get_password_hash


async def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    pass


async def user_auth(email: EmailStr, password: str = ""):
    user = await UsersDao.find_one_or_none(email=email)
    print(f"HI {user}")
    print(user.password)
    if not user or not verify_password(plain_password=password, hashed_password=user.password):
        return None

    return user


async def create_user(data: dict):
    user = await UsersDao.add(email=data.email, password=get_password_hash(data.password))
    if not user:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return user