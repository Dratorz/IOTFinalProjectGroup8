from DAL.DB import DB
from Entities.Reading import Reading
from Entities.Unit import Unit
from Entities.Type import Type

class DBReading:
    
    dta = DB()
    
    def select_all_readings(self):
        return self.dta.execute_select_query("reading")
    
    def select_readings(self, online: bool):
        return self.dta.execute_select_query("reading", params={'online': online})
    
    def insert_reading(self, reading: Reading):
        return self.dta.execute_insert_query("iotdb", "reading", params={'rasp_id': reading.rasp_id,
                                                                         'value': reading.value,
                                                                         'type_id': reading.type_id,
                                                                         'unit_id': reading.unit_id,
                                                                         'online': reading.online})