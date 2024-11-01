-- Creates a db, and a table in it with a UUID column
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
