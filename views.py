from config import app, templates
from fastapi.responses import HTMLResponse
from fastapi import Request, Depends, Form
from sqlalchemy.orm import Session
from db import get_db, User, Admin, Tour
import datetime

@app.get('/', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):  # параметр щоб дістати щось з бд
    tours = db.query(Tour).all()
    return templates.TemplateResponse('index.html', {'tours': tours, 'request': request})


@app.post('/create-tour')
def create_tour(name=Form(), db: Session = Depends(get_db)):  # параметр щоб дістати щось з бд
    tour = Tour(name=name)
    db.add(tour)
    db.commit()
    db.refresh(tour)
    return {}



