CREATE USER 'galeria_arte'@'%' IDENTIFIED WITH caching_sha2_password BY '***';GRANT ALL PRIVILEGES ON *.* TO 'galeria_arte'@'%' WITH GRANT OPTION;ALTER USER 'galeria_arte'@'%' REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;CREATE DATABASE IF NOT EXISTS `galeria_arte`;GRANT ALL PRIVILEGES ON `galeria\_arte`.* TO 'galeria_arte'@'%';GRANT ALL PRIVILEGES ON `galeria\_arte\_%`.* TO 'galeria_arte'@'%';