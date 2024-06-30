from infrastructure.database.base_setup import BaseSetup
from infrastructure.database.constants import *
from model.DTOs.pet_dto import petDTO
from model.DTOs.user_dto import UserDTO
from utils.helper import Helper
from typing import List
import sqlite3, datetime, bcrypt

class petSetup(BaseSetup):
    
    @staticmethod
    def view(user_id: str):
        conn = BaseSetup.connect()
        
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM {} WHERE user_id = ?".format(pet_TABLE), (user_id,))
        
        rows = cur.fetchall()
        
        pets = [] 

        for row in rows:
            pet = petDTO(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            pets.append(pet.to_dict())
            
        BaseSetup.close(conn)
        
        return pets

    @staticmethod
    def delete(pet_id: str):
        conn = BaseSetup.connect()
        
        cur = conn.cursor()
        
        cur.execute("DELETE FROM {} WHERE id = ?".format(pet_TABLE), (pet_id,))

        conn.commit()
        
        BaseSetup.close(conn)
        
        return
    
    @staticmethod
    def update(updated_pet: petDTO):
        conn = BaseSetup.connect()
    
        cur = conn.cursor()
    
        query = "UPDATE {} SET name = ?, race = ?, age = ?, gender = ?, color = ? WHERE id = ?".format(pet_TABLE)
    
        values = (updated_pet.name, updated_pet.race, updated_pet.age, updated_pet.gender, updated_pet.color, updated_pet.id)
    
        cur.execute(query, values)

        conn.commit()
    
        BaseSetup.close(conn)
    
        return
   