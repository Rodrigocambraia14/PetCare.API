import sqlite3, datetime
from xmlrpc.client import DateTime
from infrastructure.database.constants import DB_NAME
from model.entities.user import User
from model.entities.pet import Pet
from model.entities.food_routine import FoodRoutine
from model.entities.portion_detail import PortionDetail
from model.entities.vaccine_calendar import VaccineCalendar
from utils.helper import Helper
from datetime import datetime

class Seed:
    
    @staticmethod
    def run_database_seeding():
        conn = sqlite3.connect(DB_NAME)
        
        user = User(Helper.get_new_id(), 'PUC RIO', 'tester@PUCRIO.com', 'PUC@123')
        user.add()
     
        pet = Pet(Helper.get_new_id(), 'Abigail', 1, 'F', 'Tricolor', user.id)
        pet.add()
        
        date = VaccineCalendar(Helper.get_new_id(), datetime.now(), 'Vacina contra raiva - 1 dose', user.id)
        date.add()
        
        food_routine = FoodRoutine(Helper.get_new_id(), 'alimentacao Abigail', 3, pet.id)
        food_routine.add()
        
        first_portion_detail = PortionDetail(Helper.get_new_id(), 'cafe da manha', 200, '09:00', food_routine.id)
        second_portion_detail = PortionDetail(Helper.get_new_id(), 'almoco', 200, '13:00', food_routine.id)
        third_portion_detail = PortionDetail(Helper.get_new_id(), 'janta', 230, '21:37', food_routine.id)
        fourth_portion_detail = PortionDetail(Helper.get_new_id(), 'ceia', 500, '21:57', food_routine.id)
        
        first_portion_detail.add()
        second_portion_detail.add()
        third_portion_detail.add()
        fourth_portion_detail.add()

        conn.commit()
        conn.close()
