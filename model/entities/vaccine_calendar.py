import bcrypt
from model.DTOs.pet_dto import petDTO
from model.DTOs.vaccine_calendar_dto import VaccineCalendarDTO
from model.core.pet_setup import petSetup
from model.core.user_setup import UserSetup
from infrastructure.database.base_setup import BaseSetup
from model.common.entity import Entity
from model.core.vaccine_calendar_setup import VaccineCalendarSetup
from utils.helper import Helper
from infrastructure.database.constants import *

class VaccineCalendar(Entity):

    def __init__(self, new_id, date, description, user_id):
        self.id = new_id
        self.date = date
        self.description = description
        self.user_id = user_id
        
    def add(self):
        BaseSetup.insert(VACCINE_CALENDAR_TABLE, self)
    
    def list(user_id: str):
        return VaccineCalendarSetup.view(user_id)
    
    @staticmethod
    def delete(date_id: str):
        return VaccineCalendarSetup.delete(date_id)
    
    def update(self):
        updated_date = VaccineCalendarDTO(self.id, self.date, self.description, self.user_id)  
        
        VaccineCalendarSetup.update(updated_date)
