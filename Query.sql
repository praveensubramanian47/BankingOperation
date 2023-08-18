SHOW DATABASES;
CREATE DATABASE bank;
USE bank;
CREATE TABLE bank_info(
AC_num INT KEY,
name VARCHAR(50),
pin VARCHAR(10),
amount INT);

INSERT INTO bank_info VALUES(2386, "Selvem.D", "ASdf", 1000);
SELECT * FROM bank_info;