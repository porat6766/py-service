from app.db.mongodb import db
from app.core.security import get_password_hash, verify_password


async def get_user_by_email(email: str):
    return await db.users.find_one({"email": email})


async def create_user(email: str, password: str):
    hashed_password = get_password_hash(password)
    user = {"email": email, "hashed_password": hashed_password}
    await db.users.insert_one(user)
    return user


async def authenticate_user(email: str, password: str):
    user = await get_user_by_email(email)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user
