
from fastapi import FastAPI
from . approuting import router
  
app = FastAPI()

app.include_router(router)

