--m\productversion:0.0.1
CREATE TABLE Sensor(
    id varchar(36) PRIMARY KEY,
    name VARCHAR(20),
    created_date timestamp,
    updated_date timestamp
);
CREATE TABLE User(
    id varchar(36) PRIMARY KEY,
    firstname VARCHAR(20),
    lastname VARCHAR(20),
    email VARCHAR(30),
    created_date timestamp,
    updated_date timestamp
);
CREATE TABLE UserLogin(
    user_id varchar(36) PRIMARY KEY,
    login varchar(30),
    password varchar(50),
    created_date timestamp,
    updated_date timestamp,
    FOREIGN KEY(user_id) REFERENCES User(id)
);
CREATE TABLE UserSensor(
    user_id varchar(36),
    sensor_id varchar(36),
    created_date timestamp,
    updated_date timestamp,
    FOREIGN KEY(user_id) REFERENCES User(id),
    FOREIGN KEY(sensor_id) REFERENCES Sensor(id),
    PRIMARY KEY(user_id, sensor_id)
);
CREATE TABLE SensorData(
    sensor_id varchar(36),
    date timestamp,
    created_date timestamp,
    updated_date timestamp,
    FOREIGN KEY(sensor_id) REFERENCES Sensor(id),
    PRIMARY KEY(sensor_id, date)
);
CREATE TABLE NumberData(
    date timestamp,
    sensor_id varchar(36),
    value int(10),
    created_date timestamp,
    updated_date timestamp,
    FOREIGN KEY(sensor_id, date) REFERENCES SensorData(sensor_id, date),
    PRIMARY KEY(date, sensor_id)
);
CREATE TABLE GeolocData(
    date timestamp,
    sensor_id varchar(36),
    long int(10),
    lat int(10),
    created_date timestamp,
    updated_date timestamp,
    FOREIGN KEY(sensor_id, date) REFERENCES SensorData(sensor_id, date),
    PRIMARY KEY(sensor_id, date)
);
CREATE TABLE SensorHost(
    sensor_id varchar(36) PRIMARY KEY,
    address varchar(50),
    topic varchar(50),
    port int(5),
    created_date timestamp,
    updated_date timestamp
);
CREATE TABLE StatisticType(
    name varchar(20) PRIMARY KEY,
    created_date timestamp,
    updated_date timestamp
);
CREATE TABLE MultiStatisticType(
    name varchar(20) PRIMARY KEY,
    created_date timestamp,
    updated_date timestamp
);
CREATE TABLE Statistic(
    id varchar(36) PRIMARY KEY,
    type varchar(20),
    name varchar(50),
    unit varchar(50),
    created_date timestamp,
    updated_date timestamp,
    FOREIGN KEY(type) REFERENCES StatisticType(name)
);
CREATE TABLE SensorStatistic(
    sensor_id varchar(36),
    stat_id varchar(36),
    time_window number(30),
    created_date timestamp,
    updated_date timestamp,
    FOREIGN KEY(sensor_id) REFERENCES Sensor(id),
    FOREIGN KEY(stat_id) REFERENCES Statictic(id),
    PRIMARY KEY(sensor_id, stat_id)
);
CREATE TABLE HueShift(
    rupture_point int(10),
    stat_id varchar(36),
    legend varchar(30),
    color varchar(20),
    created_date timestamp,
    updated_date timestamp,
    FOREIGN KEY(stat_id) REFERENCES Statictic(sensor_id),
    PRIMARY KEY(rupture_point, stat_id)
);
CREATE TABLE MultiStatictic(
    id varchar(36) PRIMARY KEY,
    type varchar(20),
    name varchar(50),
    unit varchar(50),
    created_date timestamp,
    updated_date timestamp,
    FOREIGN KEY(type) REFERENCES MultiStatisticType(name)
);
CREATE TABLE SensorMultiStat(
    sensor_id varchar(36),
    multi_stat_id varchar(36),
    time_window int(30),
    created_date timestamp,
    updated_date timestamp,
    FOREIGN KEY(sensor_id) REFERENCES Sensor(id),
    FOREIGN KEY(multi_stat_id) REFERENCES MultiStatictic(id),
    PRIMARY KEY(sensor_id, multi_stat_id)
);
