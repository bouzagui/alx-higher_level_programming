-- script that creates the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED 'user_0d_2_pwd';
GRANT SELECT ON 'htbtn_0d_2'.* TO 'user_0d_2'@'localhost';
