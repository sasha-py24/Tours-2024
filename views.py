import datetime

from config import app, templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import Request, Depends, Form, status

from sqlalchemy.orm import Session

from db import get_db, User, Admin, Tour, Buy



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
    request.session['user_id'] = user.id
    request.session['is_auto'] = True

    return RedirectResponse(url='/', status_code=302)



@app.post('/logout')
async def logout(request: Request, username: str = Form(), password: str = Form(), db: Session = Depends(get_db)):
    user = db.query(User).filter_by(username=username, password=password).first()
    if user is None:
        return RedirectResponse(url='/login', status_code=302)
    request.session['user_id'] = user.id
    request.session['is_auto'] = False

    return RedirectResponse(url='/', status_code=302)


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


@app.get('/buy', response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):  # параметр щоб дістати щось з бд
    tours = db.query(Tour).all()
    return templates.TemplateResponse('index.html', {'tours': tours, 'request': request})



@app.post('/buy-tour')
def buy_tour(user_id: str = Form(), tour_id: str = Form(), start_at: str = Form(), end_at: str = Form(), db: Session = Depends(get_db)):  # параметр щоб дістати щось з бд
    start_at = datetime.datetime.strptime(start_at, '%Y-%m-%d')
    end_at = datetime.datetime.strptime(end_at, '%Y-%m-%d')
    buy = Buy(user_id=user_id, tour_id=tour_id, start_at=start_at, end_at=end_at)
    db.add(buy)
    db.commit()
    db.refresh(buy)
    return {}
