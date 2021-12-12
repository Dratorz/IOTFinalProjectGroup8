create database iotdb;

use iotdb;
create table type(
	type_id int not null unique, 
	type_name varchar(50)
);

insert into type(type_id, type_name) 
values(1, 'temperature');

insert into type(type_id, type_name) 
values(2, 'humidity');

create table unit(
	unit_id int not null unique, 
	unit_name varchar(50),
	unit varchar(10)
);

insert into unit(unit_id, unit, unit_name) 
values(1, 'C','Celsius');

insert into unit(unit_id, unit, unit_name) 
values(2, 'F','Fahrenheit');

insert into unit(unit_id, unit, unit_name) 
values(3, 'K','Kelvin');

insert into unit(unit_id, unit, unit_name) 
values(4, '%','Relative Humidity');

create table reading(
	reading_id int not null primary key, 
	rasp_id varchar(100), 
	value float, 
	type_id int, 
	unit_id int, 
	foreign key (type_id) references type(type_id),
	foreign key (unit_id) references unit(unit_id)
);
