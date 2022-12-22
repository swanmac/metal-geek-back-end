-- settings.sql
CREATE DATABASE metal;
CREATE USER metaluser WITH PASSWORD 'metal';
GRANT ALL PRIVILEGES ON DATABASE metal TO metaluser;