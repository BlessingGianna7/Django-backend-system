
from typing import List, Optional
from pydantic import BaseModel
from fastapi import HTTPException
from animals.models import Animal
from guiders.models import Guider
from guests.models import Guest
from asgiref.sync import sync_to_async

class AnimalCreate(BaseModel):
    name: str
    species: str
    age: int
    guider_ids: List[int] = []

class AnimalUpdate(BaseModel):
    name: Optional[str] = None
    species: Optional[str] = None
    age: Optional[int] = None
    guider_ids: Optional[List[int]] = None

class GuiderCreate(BaseModel):
    name: str
    age: int
    service_hours: int

class GuiderUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    service_hours: Optional[int] = None

class GuestCreate(BaseModel):
    name: str
    visit_date: str  
    guider_ids: List[int] = []

class GuestUpdate(BaseModel):
    name: Optional[str] = None
    visit_date: Optional[str] = None
    guider_ids: Optional[List[int]] = None

@sync_to_async
def create_animal_sync(name: str, species: str, age: int, guider_ids: List[int]):
    animal = Animal(name=name, species=species, age=age)
    animal.save()
    animal.guiders.set(guider_ids)
    return animal

async def create_animal(data: AnimalCreate):
    return await create_animal_sync(data.name, data.species, data.age, data.guider_ids)

@sync_to_async
def get_animal_sync(animal_id: int):
    return Animal.objects.filter(id=animal_id).first()

async def get_animal(animal_id: int):
    animal = await get_animal_sync(animal_id)
    if not animal:
        raise HTTPException(status_code=404, detail="Animal not found")
    return animal

@sync_to_async
def update_animal_sync(animal_id: int, data: dict):
    animal = Animal.objects.filter(id=animal_id).first()
    if animal:
        if 'name' in data:
            animal.name = data['name']
        if 'species' in data:
            animal.species = data['species']
        if 'age' in data:
            animal.age = data['age']
        if 'guider_ids' in data:
            animal.guiders.set(data['guider_ids'])
        animal.save()
    return animal

async def update_animal(animal_id: int, data: AnimalUpdate):
    update_data = {k: v for k, v in data.dict().items() if v is not None}
    animal = await update_animal_sync(animal_id, update_data)
    if not animal:
        raise HTTPException(status_code=404, detail="Animal not found")
    return animal

@sync_to_async
def delete_animal_sync(animal_id: int):
    animal = Animal.objects.filter(id=animal_id).first()
    if animal:
        animal.delete()
    return animal

async def delete_animal(animal_id: int):
    animal = await delete_animal_sync(animal_id)
    if not animal:
        raise HTTPException(status_code=404, detail="Animal not found")
    return {"detail": "Animal deleted"}


@sync_to_async
def create_guider_sync(name: str, age: int, service_hours: int):
    guider = Guider(name=name, age=age, service_hours=service_hours)
    guider.save()
    return guider

async def create_guider(data: GuiderCreate):
    return await create_guider_sync(data.name, data.age, data.service_hours)

@sync_to_async
def get_guider_sync(guider_id: int):
    guider = Guider.objects.filter(id=guider_id).first()
    if guider:
        return {
            "id": guider.id,
            "name": guider.name,
            "age": guider.age,
            "service_hours": guider.service_hours
        }
    return None

async def get_guider(guider_id: int):
    guider = await get_guider_sync(guider_id)
    if not guider:
        raise HTTPException(status_code=404, detail="Guider not found")
    return guider

@sync_to_async
def update_guider_sync(guider_id: int, data: dict):
    guider = Guider.objects.filter(id=guider_id).first()
    if guider:
        if 'name' in data:
            guider.name = data['name']
        if 'age' in data:
            guider.age = data['age']
        if 'service_hours' in data:
            guider.service_hours = data['service_hours']
        guider.save()
    return guider

async def update_guider(guider_id: int, data: GuiderUpdate):
    update_data = {k: v for k, v in data.dict().items() if v is not None}
    guider = await update_guider_sync(guider_id, update_data)
    if not guider:
        raise HTTPException(status_code=404, detail="Guider not found")
    return guider

@sync_to_async
def delete_guider_sync(guider_id: int):
    guider = Guider.objects.filter(id=guider_id).first()
    if guider:
        guider.delete()
    return guider

async def delete_guider(guider_id: int):
    guider = await delete_guider_sync(guider_id)
    if not guider:
        raise HTTPException(status_code=404, detail="Guider not found")
    return {"detail": "Guider deleted"}

# Guest CRUD operations
@sync_to_async
def create_guest_sync(name: str, visit_date: str, guider_ids: List[int]):
    guest = Guest(name=name, visit_date=visit_date)
    guest.save()
    guest.guiders.set(guider_ids)
    return guest

async def create_guest(data: GuestCreate):
    return await create_guest_sync(data.name, data.visit_date, data.guider_ids)

@sync_to_async
def get_guest_sync(guest_id: int):
    return Guest.objects.filter(id=guest_id).first()

async def get_guest(guest_id: int):
    guest = await get_guest_sync(guest_id)
    if not guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    return guest

@sync_to_async
def update_guest_sync(guest_id: int, data: dict):
    guest = Guest.objects.filter(id=guest_id).first()
    if guest:
        if 'name' in data:
            guest.name = data['name']
        if 'visit_date' in data:
            guest.visit_date = data['visit_date']
        if 'guider_ids' in data:
            guest.guiders.set(data['guider_ids'])
        guest.save()
    return guest

async def update_guest(guest_id: int, data: GuestUpdate):
    update_data = {k: v for k, v in data.dict().items() if v is not None}
    guest = await update_guest_sync(guest_id, update_data)
    if not guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    return guest

@sync_to_async
def delete_guest_sync(guest_id: int):
    guest = Guest.objects.filter(id=guest_id).first()
    if guest:
        guest.delete()
    return guest

async def delete_guest(guest_id: int):
    guest = await delete_guest_sync(guest_id)
    if not guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    return {"detail": "Guest deleted"}


@sync_to_async
def get_all_animals_sync():
    animals = Animal.objects.all()
    return list(animals.values('id', 'name', 'species', 'age'))

async def get_all_animals():
    return await get_all_animals_sync()

@sync_to_async
def get_all_guiders_sync():
    guiders = Guider.objects.all()
    return [
        {
            "id": guider.id,
            "name": guider.name,
            "age": guider.age,
            "service_hours": guider.service_hours
        }
        for guider in guiders
    ]

@sync_to_async
def get_all_guests_sync():
    guests = Guest.objects.all()
    return [
        {
            "id": guest.id,
            "name": guest.name,
            "visit_date": guest.visit_date,
            "guider_ids": [guider.id for guider in guest.guiders.all()]
        }
        for guest in guests
    ]