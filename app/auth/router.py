from fastapi import APIRouter, HTTPException, status

from app.auth.authenticate import user_auth, create_user
from app.users.schemas import UsersAuthSchema

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Users"]
)


@router.post("/register")
async def register(user_data: UsersAuthSchema):
    user_exist = await user_auth(email=user_data.email)
    if user_exist:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    user = await create_user(user_data)
    print(f"user: {user}")
    if not user:
        raise

    return user

#
# @router.post("/signin")
# async def sign_in(response: Response, user_data: UsersAuthSchema):
#     print(user_data)
#     user = await user_auth(user_data.email, user_data.password)
#     if not user:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
#
#     access_token = create_access_token({"sub": user.id})
#     response.set_cookie("access_token", access_token)
#     return access_token
