import bcrypt
from model.DTOs.pet_dto import petDTO
from model.core.pet_setup import petSetup
from model.core.user_setup import UserSetup
from infrastructure.database.base_setup import BaseSetup
from model.common.entity import Entity
from utils.helper import Helper
from infrastructure.database.constants import *

class Pet(Entity):

    def __init__(self, new_id, name,  age, gender, color, user_id):
        self.id = new_id
        self.name = name
        self.age = age
        self.color = color
        self.gender = gender
        self.user_id = user_id
        
    def add(self):
        BaseSetup.insert(pet_TABLE, self)
    
    def update(self):
        
        updated_pet = petDTO(self.id, self.name, self.age, self.gender, self.color, self.user_id)  
        
        petSetup.update(updated_pet)

    def list(user_id: str):
        return petSetup.view(user_id)
    
    @staticmethod
    def delete(pet_id: str):
        return petSetup.delete(pet_id)
