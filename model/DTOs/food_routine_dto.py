from model.common.entity import Entity

class FoodRoutineDTO(Entity):

     def __init__(self, new_id, name, portions, pet_id):
        self.id = new_id
        self.name = name
        self.portions = portions
        self.pet_id = pet_id
        self.portion_details = [] 
        
     def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "portions": self.portions,
            "pet_id": self.pet_id,
            "portion_details": self.portion_details

        }