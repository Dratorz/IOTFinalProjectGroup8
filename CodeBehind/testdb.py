from DAL.DBReading import DBReading
from Entities.Reading import Reading

readings = DBReading()

my_readings = readings.select_all_readings()

print(my_readings)

my_reading = Reading("testonline", 10, 1, 1, True)

insert_response = readings.insert_reading(my_reading)

filtered_readings = readings.select_readings(True)
print()
print(filtered_readings)
print()
#insert_response = readings.insert_reading(my_reading)

#print(insert_response)
my_readings = readings.select_all_readings()

print(my_readings)