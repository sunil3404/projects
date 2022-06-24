from fastapi import FastAPI
from routers import stocks, company
from database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(stocks.router)
app.include_router(company.router)