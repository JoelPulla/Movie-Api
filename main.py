from fastapi import FastAPI
from routes import users

app = FastAPI()
app.version = '0.0.1'
app.title = 'MovieApi'

### Routes ###
app.include_router(users.router)

@app.get('/')
def root():
    return {'conection': True}

