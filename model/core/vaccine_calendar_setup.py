from infrastructure.database.base_setup import BaseSetup
from infrastructure.database.constants import *
from model.DTOs.pet_dto import petDTO
from model.DTOs.user_dto import UserDTO
from model.DTOs.vaccine_calendar_dto import VaccineCalendarDTO
from utils.helper import Helper
from typing import List
import sqlite3, datetime, bcrypt

class VaccineCalendarSetup(BaseSetup):
    
    @staticmethod
    def view(user_id: str):
        conn = BaseSetup.connect()
        
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM {} WHERE user_id = ?".format(VACCINE_CALENDAR_TABLE), (user_id,))
        
        rows = cur.fetchall()
        
        dates = [] 

        for row in rows:
            date = VaccineCalendarDTO(row[0], row[1], row[2], row[3])
            dates.append(date.to_dict())
            
        BaseSetup.close(conn)
        
        return dates

    @staticmethod
    def delete(date_id: str):
        conn = BaseSetup.connect()
        
        cur = conn.cursor()
        
        cur.execute("DELETE FROM {} WHERE id = ?".format(VACCINE_CALENDAR_TABLE), (date_id,))

        conn.commit()
        
        BaseSetup.close(conn)
        
        return
    
    @staticmethod
    def update(updated_date: VaccineCalendarDTO):
        conn = BaseSetup.connect()
    
        cur = conn.cursor()
    
        query = "UPDATE {} SET date = ?, description = ? WHERE id = ?".format(VACCINE_CALENDAR_TABLE)
    
        values = (updated_date.date, updated_date.description, updated_date.id)
    
        cur.execute(query, values)

        conn.commit()
    
        BaseSetup.close(conn)
    
        return
   