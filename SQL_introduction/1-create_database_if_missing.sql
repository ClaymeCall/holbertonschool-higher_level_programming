#!/bin/bash
-- 1-create_database_if_missing.sql
-- Creates a database if it doesnt exist.
IF NOT EXISTS(SELECT name FROM sys.databases WHERE name = 'hbtn_0c_0')
BEGIN
        CREATE DATABASE hbtn_0c_0;
END
