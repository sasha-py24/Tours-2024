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
def create_tour(name=Form(), city=Form(), days=Form(), price=Form(), date=Form(), db: Session = Depends(get_db)):  # параметр щоб дістати щось з бд
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    tour = Tour(name=name, city=city, days=days, price=price, date=date)
    db.add(tour)
    db.commit()
    db.refresh(tour)
    return {}



@app.get('/user', response_class=HTMLResponse)
def user(request: Request, db: Session = Depends(get_db)):  # параметр щоб дістати щось з бд
    users = db.query(User).all()
    return templates.TemplateResponse('index.html', {'users': users, 'request': request})


@app.post('/add-user')
def add_user(username=Form(), email=Form(), db: Session = Depends(get_db)):  # параметр щоб дістати щось з бд
    user = User(username=username, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {}