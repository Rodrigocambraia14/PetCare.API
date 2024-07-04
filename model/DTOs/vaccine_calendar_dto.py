from model.common.entity import Entity

class VaccineCalendarDTO(Entity):

     def __init__(self, new_id, date, description, user_id):
        self.id = new_id
        self.date = date
        self.description = description
        self.user_id = user_id

     def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "description": self.description,
            "user_id": self.user_id
        }