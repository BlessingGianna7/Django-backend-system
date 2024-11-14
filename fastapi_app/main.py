import os
import django
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')  
django.setup()

from fastapi import FastAPI, HTTPException
from fastapi_app.crud import (
    create_animal, get_animal, update_animal, delete_animal, get_all_animals,
    create_guider, get_guider, update_guider, delete_guider, get_all_guiders,
    create_guest, get_guest, update_guest, delete_guest, get_all_guests,
    AnimalCreate, AnimalUpdate, GuiderCreate, GuiderUpdate, GuestCreate, GuestUpdate
)
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8001"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Wildlife Conservation API"}

# Animal routes
@app.get("/animals", response_model=List[dict])
@app.get("/animals/", response_model=List[dict])
async def list_animals():
    print("GET /animals/ called")  # Debug print
    return await get_all_animals()

@app.post("/animals", response_model=dict)
@app.post("/animals/", response_model=dict)
async def create_animal_endpoint(animal: AnimalCreate):
    return await create_animal(animal)

@app.get("/animals/{animal_id}", response_model=dict)
async def get_animal_endpoint(animal_id: int):
    return await get_animal(animal_id)

@app.put("/animals/{animal_id}", response_model=dict)
async def update_animal_endpoint(animal_id: int, animal: AnimalUpdate):
    return await update_animal(animal_id, animal)

@app.delete("/animals/{animal_id}")
async def delete_animal_endpoint(animal_id: int):
    return await delete_animal(animal_id)

# Guider routes
@app.get("/guiders", response_model=List[dict])
@app.get("/guiders/", response_model=List[dict])
async def list_guiders():
    print("GET /guiders/ called")  # Debug print
    return await get_all_guiders()

@app.post("/guiders", response_model=dict)
@app.post("/guiders/", response_model=dict)
async def create_guider_endpoint(guider: GuiderCreate):
    return await create_guider(guider)

@app.get("/guiders/{guider_id}", response_model=dict)
async def get_guider_endpoint(guider_id: int):
    return await get_guider(guider_id)

@app.put("/guiders/{guider_id}", response_model=dict)
async def update_guider_endpoint(guider_id: int, guider: GuiderUpdate):
    return await update_guider(guider_id, guider)

@app.delete("/guiders/{guider_id}")
async def delete_guider_endpoint(guider_id: int):
    return await delete_guider(guider_id)

# Guest routes
@app.get("/guests", response_model=List[dict])
@app.get("/guests/", response_model=List[dict])
async def list_guests():
    print("GET /guests/ called")  # Debug print
    return await get_all_guests()

@app.post("/guests", response_model=dict)
@app.post("/guests/", response_model=dict)
async def create_guest_endpoint(guest: GuestCreate):
    return await create_guest(guest)

@app.get("/guests/{guest_id}", response_model=dict)
async def get_guest_endpoint(guest_id: int):
    return await get_guest(guest_id)

@app.put("/guests/{guest_id}", response_model=dict)
async def update_guest_endpoint(guest_id: int, guest: GuestUpdate):
    return await update_guest(guest_id, guest)

@app.delete("/guests/{guest_id}")
async def delete_guest_endpoint(guest_id: int):
    return await delete_guest(guest_id)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)