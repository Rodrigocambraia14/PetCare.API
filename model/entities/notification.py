from model.common.entity import Entity

#classe ainda n�o est� sendo utilizada, pois n�o estou armazenando notifica��es disparadas no SQLite

class Notification(Entity):

    def __init__(self, message, has_notification):
        self.message = message
        self.has_notification = has_notification
        
