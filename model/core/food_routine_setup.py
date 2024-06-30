from infrastructure.database.base_setup import BaseSetup
from infrastructure.database.constants import *
from model.DTOs.pet_dto import petDTO
from model.DTOs.food_routine_dto import FoodRoutineDTO
from model.DTOs.notification_dto import NotificationDTO
from model.DTOs.portion_detail_dto import PortionDetailDTO
from utils.helper import Helper
from typing import List
import sqlite3, bcrypt
from datetime import datetime

class FoodRoutineSetup(BaseSetup):
    
    @staticmethod
    def view(user_id: str) -> List[FoodRoutineDTO]:
        conn = BaseSetup.connect()
        cur = conn.cursor()

        cur.execute("SELECT id FROM {} WHERE user_id = ?".format(pet_TABLE), (user_id,))
        pet_rows = cur.fetchall()
        pet_ids = [row[0] for row in pet_rows]

        cur.execute("SELECT * FROM {} WHERE pet_id IN ({})".format(FOOD_ROUTINE_TABLE, ",".join(["?"] * len(pet_ids))), pet_ids)
        rows = cur.fetchall()

        food_routines = []

        for row in rows:
            food_routine = FoodRoutineDTO(row[0], row[1], row[2], row[3])

            cur.execute("""
            SELECT *
            FROM {}
            WHERE food_routine_id = ?            
            """.format(PORTION_DETAIL_TABLE), (food_routine.id,))
        
            portion_detail_rows = cur.fetchall()
            
            portion_details = []
            
            for portion_detail_row in portion_detail_rows:
                
                portion_detail = PortionDetailDTO(portion_detail_row[0], portion_detail_row[1], portion_detail_row[2], portion_detail_row[3], portion_detail_row[4])
                portion_details.append(portion_detail.to_dict())
            
            food_routine.portion_details = portion_details
            food_routines.append(food_routine.to_dict())
            
        BaseSetup.close(conn)

        return food_routines
   
    @staticmethod
    def get_notifications(user_id:str) -> NotificationDTO:
        
        current_time = datetime.now().strftime('%H:%M')  

        conn = BaseSetup.connect()
        
        cur = conn.cursor()
        
        cur.execute("""
    SELECT {}.id, {}.name, {}.portions, {}.pet_id, {}.name AS pet_name
    FROM {} 
    INNER JOIN {} ON {}.pet_id = {}.id
    WHERE {}.user_id = ?                
""".format(FOOD_ROUTINE_TABLE, FOOD_ROUTINE_TABLE, FOOD_ROUTINE_TABLE,FOOD_ROUTINE_TABLE, pet_TABLE, FOOD_ROUTINE_TABLE, pet_TABLE, FOOD_ROUTINE_TABLE, pet_TABLE, pet_TABLE), (user_id,))

        
        rows = cur.fetchall()
        
        for row in rows:
            food_routine = FoodRoutineDTO(row[0], row[1], row[2], row[3])
            
            pet_name = row[4]
            
            cur.execute("""
            SELECT *
            FROM {}
            WHERE food_routine_id = ?            
            """.format(PORTION_DETAIL_TABLE), (food_routine.id,))
        
            portion_detail_rows = cur.fetchall()
            
            for portion_detail_row in portion_detail_rows:
                portion_detail = PortionDetailDTO(portion_detail_row[0], portion_detail_row[1], portion_detail_row[2], portion_detail_row[3], portion_detail_row[4])
                

                if portion_detail.feed_time == current_time:
                    message = f"{pet_name} esta com fome, Coloque {portion_detail.grams} gramas de racao as {portion_detail.feed_time}h!"
                    return NotificationDTO(message, True).to_dict()
            
        BaseSetup.close(conn)
        
        return NotificationDTO('', False).to_dict() 