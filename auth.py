import bcrypt
from database import create_user, get_user


def hash_password(password):
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()


def verify_password(password, hashed):
    return bcrypt.checkpw(
        password.encode(),
        hashed.encode()
    )


def signup(username, email, password):
    hashed = hash_password(password)
    return create_user(username, email, hashed)


def login(email, password):

    user = get_user(email)

    if user is None:
        return None

    if verify_password(password, user["password"]):
        return user

    return None