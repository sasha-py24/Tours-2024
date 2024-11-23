import datetime

from config import app, templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import Request, Depends, Form

from sqlalchemy.orm import Session

from db import get_db, User, Admin, Tour



@app.get('/', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):  # параметр щоб дістати щось з бд
    tours = db.query(Tour).all()
    return templates.TemplateResponse('index.html', {'tours': tours, 'request': request})



@app.post('/create-tour')
def create_tour(name: str = Form(), city: str = Form(), days: int = Form(), price: int = Form(), date: str = Form(), db:Session = Depends(get_db)):  # параметр щоб дістати щось з бд
    date = datetime.datetime.strptime(date, '%Y-%m-%d', )
    tour = Tour(name=name, city=city, days=days, price=price, date=date)
    db.add(tour)
    db.commit()
    db.refresh(tour)
    return {'id': 'tour.id'}



@app.post('/login')
async def login(request: Request, username: str = Form(), email: str =Form(), db: Session = Depends(get_db)):  # параметр щоб дістати щось з бд
    user = db.query(User).filter_by(username=username, email=email).first()
    if user is None or email != email:
        return RedirectResponse(url='/login', status_code=302)
    return templates.TemplateResponse('index.html', {'users': user, 'request': request})



@app.get('/register', response_class=HTMLResponse)
def register(request: Request, username=Form(), email=Form(),  db: Session = Depends(get_db)):  # параметр щоб дістати щось з бд
    user = User(username=username, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return templates.TemplateResponse('register.html', {'user': user, 'request': request})

