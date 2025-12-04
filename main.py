image.pngfckcrsr.pngfrom fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from authx import AuthX, AuthXConfig

app = FastAPI()

config = AuthXConfig()
config.JWT_SECRET_KEY = "SECRET_KEY"
config.JWT_ACCESS_COOKIE_NAME = "my_token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str

@app.get("/points")
async def handle_click():
    return


class UserRegistration(BaseModel):
    email: EmailStr
    password: str

@app.post("/login")
async def login(creds: UserLoginSchema):
    if creds.username == "test" and creds.password == "test":
        token = security.create_access_token(uid="12345")
        return{"access_token": token}
    raise HTTPException(status_code=401, detail="Incorrect username or password")


@app.get("/protected")
async def protected():


'''
@app.post("/register/")
async def register_user(user: UserRegistration):
    
    return {"message": "Пользователь зарегистрирован", "user": user}
'''