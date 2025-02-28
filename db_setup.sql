CREATE DATABASE cws_portal_db;
CREATE USER cws_user WITH PASSWORD 'postgres';
ALTER ROLE cws_user SET client_encoding TO 'utf8';
ALTER ROLE cws_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE cws_user SET timezone TO 'Asia/Kolkata';
GRANT ALL PRIVILEGES ON DATABASE cws_portal_db TO cws_user;
