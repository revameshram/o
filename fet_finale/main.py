from fastapi import FastAPI #for importing fast api
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
import re
from pathlib import Path


app=FastAPI()

BASE_DIR = Path(__file__).resolve().parent

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")    

@app.get("/")
def home():  #it is browser's request to ask for rendering templates
    return FileResponse(str(BASE_DIR / "py_file.html"))

@app.get("/code")
def code():  #it is browser's request to ask for rendering templates
    return FileResponse(str(BASE_DIR / "py_file.html"))

@app.get("/list")
def list_code():
    files = os.listdir(BASE_DIR / "static" / "code")
    files.sort(key=natural_sort_key)
    return {"files": files}
