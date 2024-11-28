import datetime

from config import app, templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import Request, Depends, Form, status

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
async def login(request: Request, username: str = Form(), password: str = Form(), db: Session = Depends(get_db)):
    user = db.query(User).filter_by(username=username, password=password).first()
    if user is None:
        return RedirectResponse(url='/login', status_code=302)
    if user in user:
        session_id = Session(user['user_id'])
        return{"message": "Logged in successfully", "session_id": session_id}
    return templates.TemplateResponse('index.html', {'users': user, 'request': request})



@app.get('/register', response_class = HTMLResponse)
def reg(request: Request, db: Session = Depends(get_db)):
    users = db.query(User).all()
    return templates.TemplateResponse('register.html', {'users': users, 'request': request})



@app.post('/register')
def register(request: Request, username: str = Form(), email: str = Form(), password: str = Form(),  db: Session = Depends(get_db)):  # параметр щоб дістати щось з бд
    user = User(username=username, email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return RedirectResponse('/', status_code=303)



