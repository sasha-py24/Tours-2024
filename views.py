from config import app, templates
from fastapi.responses import HTMLResponse
from fastapi import Request, Depends, Form
from sqlalchemy.orm import Session
from db import get_db, User, Admin, Tour
import datetime

@app.route('/')
def index(request: Request, db: Session = Depends(get_db)):  # параметр щоб дістати щось з бд
    # tours = db.query(Tour).all()'tours': tours,
    return templates.TemplateResponse('index.html', {'title': 'Tours', 'request': request})