from model.common.entity import Entity

class petDTO(Entity):

     def __init__(self, new_id, name, age, gender, color, user_id):
        self.id = new_id
        self.name = name
        self.age = age
        self.color = color
        self.gender = gender
        self.user_id = user_id

     def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "color": self.color,
            "user_id": self.user_id
        }