CREATE TABLE IF NOT EXISTS crime (crime_ID varchar(50) not null,longitude varchar(50) not null,latitude varchar(50) not null,date_of varchar(50) not null,location_of varchar(50) not null,type_of varchar(50) not null,primary key (crime_ID));
CREATE TABLE IF NOT EXISTS restaurant (rest_ID varchar(50) not null,vendor_addr varchar(50) not null,location_of varchar(50) not null,zip_code varchar(50) not null,items_sold varchar(50) not null,primary key (rest_ID));
CREATE TABLE IF NOT EXISTS covid (zip_code varchar(50) not null,primary key (zip_code));
CREATE TABLE IF NOT EXISTS covid_case_count (count_ID varchar(50) not null,zip_code varchar(50) not null,date_of varchar(50) not null,amount varchar(50) not null,primary key (count_ID));
CREATE TABLE IF NOT EXISTS loc (loc_ID varchar(50) not null,loc_name varchar(50),x_loc varchar(50) not null,y_loc varchar(50) not null,primary key (loc_ID));
