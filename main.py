from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from models import Plant, Family
from database import db
from schema import Plants_post

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/plants/", response_model=Plants_post)
async def create_plant(plant: Plants_post):
    db.add(plant)
    db.commit()
    db.refresh(plant)
    return plant

@app.get("/plants")
async def get_all_plants():
    plants = db.query(Plant).all()
    return plants


@app.get("/families")
async def get_all_families():
    families = db.query(Family).all()
    return families



