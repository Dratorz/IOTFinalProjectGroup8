from datetime import datetime

class Reading:
    reading_id = 0
    rasp_id = ""
    reading_time = ""
    sensor_value = 0.0
    type_id = 0
    unit_id = 0
    online = False
    
    def __init__(self, rasp_id: str, reading_time:str, sensor_value: float, type_id: int, unit_id: int, online: bool=0):
        self.rasp_id = rasp_id
        self.reading_time = reading_time
        self.sensor_value = sensor_value
        self.type_id = type_id
        self.unit_id = unit_id
        self.online = online
        
        