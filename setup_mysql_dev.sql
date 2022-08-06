USE hbnb_dev_db;
CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
FLUSH PRIVILEGES; 
GRANT ALL PRIVILEGES ON *.* TO 'hbnb_dev'@'localhost' WITH GRANT OPTION; 
GRANT SELECT ON *.* TO 'performance_schema'@'localhost' WITH GRANT OPTION; 
FLUSH PRIVILEGES; 