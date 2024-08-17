from fastapi import Depends, HTTPException, status, FastAPI
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "mouredev": {
        "username": "joeldev1",
        "full_name": "Joel Pulla",
        "email": "braismoure@mourede.com",
        "disabled": False,
        "password": "123456"
    },
    "mouredev2": {
        "username": "mariadev2",
        "full_name": "Maria dev",
        "email": "braismoure2@mourede.com",
        "disabled": True,
        "password": "654321"
    }
}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    return None


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    return None


async def current_user(token: str = Depends(oauth2)):
    # En un escenario real, aquí deberías decodificar el token
    # y obtener el username o el identificador del usuario del token.
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate": "Bearer"})

    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo")

    return user


@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")

    # En un entorno de producción, debes generar un JWT u otro tipo de token de sesión
    # Aquí simplemente devolvemos el nombre de usuario como un token, lo cual no es seguro
    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
