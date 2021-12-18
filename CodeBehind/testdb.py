from DAL.DBReading import DBReading
from Entities.Reading import Reading
from datetime import datetime

readings = DBReading()

my_readings = readings.select_all_readings()

print(my_readings)

now = datetime.now()

print(now.strftime('%Y-%m-%d %H:%M:%S'))

my_reading = Reading("goop", now, 10, 1, 1)

insert_response = readings.insert_reading(my_reading)

filtered_readings = readings.select_readings(True)
print()
print(filtered_readings)
print()
#insert_response = readings.insert_reading(my_reading)

#print(insert_response)
my_readings = readings.select_all_readings()

print(my_readings)


# response = readings.update_reading(True)
# print(response)

my_readings = readings.select_all_readings()
filter_out = ['reading_id', 'online']
my_readings = map(lambda r: [value for key, value in r.items() if key not in no_bueno], my_readings)

print(list(my_readings))
