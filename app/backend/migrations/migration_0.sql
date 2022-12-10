CREATE TABLE Sensor(
    id int(20) PRIMARY KEY,
    name VARCHAR(20),
    created_date date,
    updated_date date
);
CREATE TABLE User(
    id int(20) PRIMARY KEY,
    firstname VARCHAR(20),
    lastname VARCHAR(20),
    email VARCHAR(30),
    created_date date,
    updated_date date
);
CREATE TABLE UserLogin(
    user_id int(20) PRIMARY KEY,
    login varchar(30),
    password varchar(50),
    created_date date,
    updated_date date,
    FOREIGN KEY(user_id) REFERENCES(User.id)
);
CREATE TABLE UserSensor(
    user_id int(20) PRIMARY KEY,
    sensor_id int(20) PRIMARY KEY,
    created_date date,
    updated_date date,
    FOREIGN KEY(user_id) REFERENCES(User.id),
    FOREIGN KEY(sensor_id) REFERENCES(Sensor.id)
);
CREATE TABLE SensorData(
    sensor_id int(20) PRIMARY KEY,
    date date PRIMARY KEY,
    created_date date,
    updated_date date,
    FOREIGN KEY(sensor_id) REFERENCES(Sensor.id)
);
CREATE TABLE NumberData(
    date date PRIMARY KEY,
    sensor_id int(20) PRIMARY KEY,
    value int(10),
    created_date date,
    updated_date date,
    FOREIGN KEY(sensor_id, date) REFERENCES(SensorData.sensor_id, SensorData.date)
);
CREATE TABLE GeolocData(
    date date PRIMARY KEY,
    sensor_id int(20) PRIMARY KEY,
    long int(10),
    lat int(10),
    created_date date,
    updated_date date,
    FOREIGN KEY(sensor_id, date) REFERENCES(SensorData.sensor_id, SensorData.date)
);
CREATE TABLE SensorHost(
    sensor_id int(20) PRIMARY KEY,
    address varchar(50),
    topic varchar(50),
    port int(5),
    created_date date,
    updated_date date
);
CREATE TABLE StatisticType(
    name varchar(20) PRIMARY KEY,
    created_date date,
    updated_date date
);
CREATE TABLE MultiStatisticType(
    name varchar(20) PRIMARY KEY,
    created_date date,
    updated_date date
);
CREATE TABLE Statistic(
    id int(20) PRIMARY KEY,
    type varchar(20) PRIMARY KEY,
    name varchar(50),
    unit varchar(50),
    created_date date,
    updated_date date,
    FOREIGN KEY(type) REFERENCES(StatisticType.name)
);
CREATE TABLE SensorStatistic(
    sensor_id int(20) PRIMARY KEY,
    stat_id int(20) PRIMARY KEY,
    time_window number(30),
    created_date date,
    updated_date date,
    FOREIGN KEY(sensor_id) REFERENCES(Sensor.id),
    FOREIGN KEY(stat_id) REFERENCES(Statictic.id)
);
CREATE TABLE HueShift(
    rupture_point int(10) PRIMARY KEY,
    stat_id int(20) PRIMARY KEY,
    legend varchar(30),
    color varchar(20),
    created_date date,
    updated_date date,
    FOREIGN KEY(stat_id) REFERENCES(Statictic.sensor_id)
);
CREATE TABLE MultiStatictic(
    id int(20) PRIMARY KEY,
    type varchar(20),
    name varchar(50),
    unit varchar(50),
    created_date date,
    updated_date date,
    FOREIGN KEY(type) REFERENCES(MultiStatisticType.name)
);
CREATE TABLE SensorMultiStat(
    sensor_id int(20) PRIMARY KEY,
    multi_stat_id int(20) PRIMARY KEY,
    time_window int(30),
    created_date date,
    updated_date date,
    FOREIGN KEY(sensor_id) REFERENCES(Sensor.id),
    FOREIGN KEY(multi_stat_id) REFERENCES(MultiStatictic.id)
);
