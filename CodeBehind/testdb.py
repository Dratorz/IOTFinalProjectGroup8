from DAL.DBReading import DBReading
from Entities.Reading import Reading
from datetime import datetime

readings = DBReading()

my_readings = readings.select_all_readings()

print(my_readings)

now = datetime.now()

print(now.strftime('%Y-%m-%d %H:%M:%S'))

my_reading = Reading("tes", now, 10, 1, 1)

insert_response = readings.insert_reading(my_reading)

filtered_readings = readings.select_readings(True)
print()
print(filtered_readings)
print()
#insert_response = readings.insert_reading(my_reading)

#print(insert_response)
my_readings = readings.select_all_readings()

print(my_readings)