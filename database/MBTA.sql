CREATE DATABASE IF NOT EXISTS MBTAdb;

USE MBTAdb;

DROP TABLE IF EXISTS mbta_buses;

CREATE TABLE mbta_buses (
    record_num INT AUTO_INCREMENT PRIMARY KEY,
    id VARCHAR(255) NOT NULL,
    latitude DECIMAL(11,8) NOT NULL,
    longitude DECIMAL(11,8) NOT NULL,
    vehicle_label VARCHAR(255),
    current_status VARCHAR(255),
    bearing INT,
    direction_id INT,
    occupancy_status VARCHAR(255)
);


