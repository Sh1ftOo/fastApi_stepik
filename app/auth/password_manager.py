from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    """Get hash of password

    :param password: passsword for hashing
    :return:  password
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify written password with hashed password

    :param plain_password: password that needs to verify
    :param hashed_password: hashed password
    :return: Is it similar or no
    """
    return pwd_context.verify(plain_password, hashed_password)
